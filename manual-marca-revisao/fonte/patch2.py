#!/usr/bin/env python3
# Aplica as correções sobre BILIO_Manual_Marca_16x9_rev1.pdf e gera a rev2.
import warnings; warnings.filterwarnings("ignore")
import pymupdf, sys
import os; B = os.path.dirname(os.path.abspath(__file__))
SRC, DST = f"{B}/BILIO_Manual_Marca_16x9_rev1.pdf", f"{B}/BILIO_Manual_Marca_16x9_rev2.pdf"
doc = pymupdf.open(SRC)
K = 0.75  # px (1920) -> pt (1440)
REDACT = {  # página (1-based): retângulos em px
    4:  [(110, 855, 670, 952)],
    8:  [(1625, 698, 1685, 726)],
    18: [(1270, 160, 1795, 226)],
    19: [(1360, 470, 1770, 536), (655, 726, 1320, 778)],
    20: [(115, 784, 455, 812), (665, 784, 1045, 812), (1072, 784, 1355, 812), (1445, 811, 1725, 840), (115, 954, 915, 982)],
    27: [(115, 800, 825, 868)],
    30: [(640, 262, 1285, 292), (175, 370, 1750, 575)],
}
OVERLAY = {2: "ov_p02", 4: "ov_p04", 8: "ov_p08", 17: "ov_p17", 18: "ov_p18", 19: "ov_p19", 20: "ov_p20", 21: "ov_p21", 27: "ov_p27", 30: "ov_p30"}

for pn, rects in REDACT.items():
    pg = doc[pn - 1]
    for (x0, y0, x1, y1) in rects:
        pg.add_redact_annot(pymupdf.Rect(x0 * K, y0 * K, x1 * K, y1 * K), fill=False)
    pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
for pn, name in OVERLAY.items():
    ov = pymupdf.open(f"{B}/{name}.pdf")
    doc[pn - 1].show_pdf_page(doc[pn - 1].rect, ov, 0, overlay=True)
# p. 29 substituída
new29 = pymupdf.open(f"{B}/p29_manifesto.pdf")
doc.delete_page(28)
doc.insert_pdf(new29, from_page=0, to_page=0, start_at=28)
# p. 32 nova
doc.insert_pdf(pymupdf.open(f"{B}/p32_producao.pdf"), from_page=0, to_page=0)
doc.set_metadata({"title": "BÍLIO & BÍLIO · Manual de identidade visual", "subject": "Revisão 2", "creator": "Revisão sobre o PDF original", "producer": "PyMuPDF"})
doc.save(DST, garbage=4, deflate=True)
print("salvo", DST, "páginas:", len(doc))
