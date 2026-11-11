#!/usr/bin/env python3
# Aplica as correções sobre BILIO_Manual_Marca_16x9_rev1.pdf e gera a rev2.
import warnings; warnings.filterwarnings("ignore")
import pymupdf, sys
import os; B = os.path.dirname(os.path.abspath(__file__))
SRC, DST = f"{B}/BILIO_Manual_Marca_16x9_rev1.pdf", f"{B}/BILIO_Manual_Marca_16x9_rev2.pdf"
doc = pymupdf.open(SRC)
K = 0.75  # px (1920) -> pt (1440)
REDACT = {  # página (1-based): retângulos em px
    1:  [(1640, 1010, 1800, 1031)],
    3:  [(585, 734, 785, 766)],
    4:  [(110, 855, 670, 952)],
    8:  [(935, 698, 1100, 726), (1625, 698, 1685, 726)],
    22: [(150, 664, 745, 727)],
    26: [(115, 687, 660, 762)],
    18: [(1270, 160, 1795, 226)],
    17: [(240, 498, 342, 520)],
    19: [(1360, 470, 1770, 536), (655, 726, 1320, 802)],
    20: [(115, 784, 455, 812), (665, 784, 1045, 812), (1072, 784, 1355, 812), (1445, 811, 1725, 840), (115, 954, 915, 982)],
    23: [(115, 934, 1040, 962)],
    27: [(115, 800, 825, 868), (995, 882, 1775, 945)],
    30: [(640, 262, 1285, 292), (175, 370, 1750, 575)],
}
FOOT_PAGES = [2,3,4,5,6,7,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,30]
OVERLAY = {1: ["ov_p01"], 2: ["ov_p02"], 3: ["ov_p03"], 4: ["ov_p04"], 8: ["ov_p08"], 17: ["ov_p17", "ov_p17b"], 18: ["ov_p18"], 19: ["ov_p19"], 20: ["ov_p20"], 21: ["ov_p21"], 23: ["ov_p23"], 25: ["ov_p25"], 27: ["ov_p27"], 28: ["ov_p28"], 30: ["ov_p30"]}
IMG_REMOVE = [1, 25]
for n in FOOT_PAGES:
    REDACT.setdefault(n, []).extend([(115, 1008, 545, 1032), (1765, 1008, 1805, 1032)])
    OVERLAY.setdefault(n, []).append(f'ov_f{n:02d}')
for n, nm in ((15, 'ov_p15'), (22, 'ov_p22'), (26, 'ov_p26')):
    OVERLAY.setdefault(n, []).append(nm)   # fundos raster com degradê e reflexo (contradizem as regras de uso do símbolo)

for pn in IMG_REMOVE:   # remove só as imagens da página; texto e vetores ficam
    pg = doc[pn - 1]
    pg.add_redact_annot(pg.rect, fill=False)
    pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_REMOVE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE, text=pymupdf.PDF_REDACT_TEXT_NONE)
for pn, rects in REDACT.items():
    pg = doc[pn - 1]
    for (x0, y0, x1, y1) in rects:
        pg.add_redact_annot(pymupdf.Rect(x0 * K, y0 * K, x1 * K, y1 * K), fill=False)
    pg.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
for pn, names in OVERLAY.items():
    for name in names:
        ov = pymupdf.open(f"{B}/{name}.pdf")
        doc[pn - 1].show_pdf_page(doc[pn - 1].rect, ov, 0, overlay=True)
# p. 29 substituída
new29 = pymupdf.open(f"{B}/p29_manifesto.pdf")
doc.delete_page(28)
doc.insert_pdf(new29, from_page=0, to_page=0, start_at=28)
# p. 32 nova
doc.insert_pdf(pymupdf.open(f"{B}/p32_producao.pdf"), from_page=0, to_page=0)
SEC = [("Abertura",2),("O legado",3),("O desafio",4),("A transformação",5),("A geometria",7),("A identidade preservada",8),("O tigre",9),("O coração",11),("Cores",12),("Tipografia",14),("Assinaturas oficiais",16),("Construção e proteção",18),("Reduções mínimas",20),("Como nunca usar",21),("Papelaria",22),("Materiais institucionais",24),("O símbolo como marca",25),("Identidade digital",26),("A experiência da marca",28),("Manifesto final",29),("Quem assina",31),("Produção da papelaria",32)]
doc.set_toc([[1, f"{i+1:02d} {nm}", pg] for i, (nm, pg) in enumerate(SEC)])
pg2 = doc[1]
for i, (nm, pg) in enumerate(SEC):
    col, k = (0, i) if i < 10 else (1, i - 10)
    x0, x1 = (876, 1306) if col == 0 else (1370, 1800)
    y0 = 257 + 63 * k
    pg2.insert_link({"kind": pymupdf.LINK_GOTO, "from": pymupdf.Rect(x0 * K, y0 * K, x1 * K, (y0 + 30) * K), "page": pg - 1, "to": pymupdf.Point(0, 0)})
doc.set_metadata({"title": "BÍLIO & BÍLIO · Manual de identidade visual", "subject": "Versão 1.1 · 2026", "keywords": "identidade visual; manual de marca; BÍLIO & BÍLIO", "creator": "Revisão sobre o PDF original", "producer": "PyMuPDF"})
doc.save(DST, garbage=4, deflate=True)
print("salvo", DST, "páginas:", len(doc))
