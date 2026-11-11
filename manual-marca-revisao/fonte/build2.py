#!/usr/bin/env python3
# Rodada 2: sobreposições de texto (p. 2, 4, 8, 17-21, 27, 30), manifesto (p. 29) e anexo de produção (p. 32).
# As sobreposições entram sobre as páginas originais; o texto antigo é removido por redação no passo seguinte (patch2.py).
import os, re, sys
B = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B)
exec(open(f"{B}/build.py", encoding="utf-8").read().split("out = {}")[0])   # reaproveita CSS, page(), symbol() e cores

OVCSS = CSS + """
html,body{background:transparent}
.t{position:absolute;white-space:nowrap}
.i{font-family:Inter;font-weight:400}
.m{font-family:Montserrat;font-weight:500}
"""
def ov(items, title="overlay"):
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{title}</title><style>{OVCSS}</style></head><body><div class="page" style="background:none">{"".join(items)}</div></body></html>'

def T(x, y, text, size, color, cls="i", h=None, extra=""):
    h = h or round(size * 1.21)
    return f'<div class="t {cls}" style="left:{x}px;top:{y}px;font-size:{size}px;line-height:{h}px;height:{h}px;color:{color};{extra}">{text}</div>'

out = {}

# ---------------------------------------------------------------- p. 2: sumário com páginas + anexos
pages_toc = ["02","03","04","05 · 06","07","08","09 · 10","11","12 · 13","14 · 15",
             "16 · 17","18 · 19","20","21","22 · 23","24","25","26 · 27","28","29 · 30"]
items = []
for k, pg in enumerate(pages_toc):
    col = 0 if k < 10 else 1
    y = 257 + 63 * (k % 10)
    xr = 1306 if col == 0 else 1800
    items.append(f'<div class="t m" style="left:{xr-160}px;top:{y+3}px;width:160px;text-align:right;font-size:15px;letter-spacing:.1em;line-height:22px;color:#5E5A52">{pg}</div>')
for k, (num, name, pg) in enumerate([("21","Quem assina","31"),("22","Produção da papelaria","32")]):
    y = 257 + 63 * (10 + k)
    items.append(f'<div class="t m" style="left:1370px;top:{y+8}px;font-size:14px;letter-spacing:.1em;line-height:18px;color:{BORDO}">{num}</div>')
    items.append(f'<div class="t m" style="left:1434px;top:{y}px;font-size:23px;line-height:28px;color:{GRAF}">{name}</div>')
    items.append(f'<div class="t m" style="left:1640px;top:{y+3}px;width:160px;text-align:right;font-size:15px;letter-spacing:.1em;line-height:22px;color:#5E5A52">{pg}</div>')
    items.append(f'<div class="t" style="left:1370px;top:{y+45}px;width:430px;height:1px;background:rgba(32,36,42,.16)"></div>')
out["ov_p02"] = ov(items, "p02")

# ---------------------------------------------------------------- p. 4: coluna I sem hífen final
items = [T(120, 860, "Preservar os dois B contrapostos e o nome por", 20, MARFIM, h=24),
         T(120, 891, "extenso. Quem conhecia a marca precisa", 20, MARFIM, h=24),
         T(120, 922, "reencontrá-la.", 20, MARFIM, h=24)]
out["ov_p04"] = ov(items, "p04")

# ---------------------------------------------------------------- p. 8: rótulo e nota didática
items = ['<div class="t m" style="left:1478px;top:703px;width:350px;text-align:center;font-size:14px;letter-spacing:.18em;line-height:18px;color:#8F021D;text-transform:uppercase">B contraposto</div>',
         T(951, 752, "Destaques didáticos sobre o símbolo oficial. Não são variantes da marca.", 16, "#5E5A52", h=22)]
out["ov_p08"] = ov(items, "p08")

# ---------------------------------------------------------------- p. 17: nota da versão contorno
items = [T(120, 974, "Contorno: o fio mede cerca de 0,3% da altura do símbolo. Para um fio de 0,25 pt na impressão, o símbolo precisa de 28 mm ou mais. Para 1 px em tela, de 320 px ou mais.", 15, "rgba(244,240,232,.72)", h=20)]
out["ov_p17"] = ov(items, "p17")

# ---------------------------------------------------------------- p. 18 e 19: relações φ explicitadas
items = [T(1280, 166 + 31 * i, t, 20, "#5E5A52", h=24) for i, t in enumerate([
    "A razão áurea (φ = 1,618) aparece em duas",
    "relações medidas no desenho: descritor e",
    "nome (C2 = C1 ÷ φ²) e nome e símbolo na",
    "versão vertical (ver página seguinte)."])]
out["ov_p18"] = ov(items, "p18")
items = [T(1367, 475, "A largura do nome é a largura da barra", 20, MARFIM, h=24),
         T(1367, 506, "superior do símbolo multiplicada por φ.", 20, MARFIM, h=24),
         T(663, 730, "Na reduzida horizontal, sem descritor, a proporção entre C1 e a altura do símbolo", 16, MARFIM, h=19),
         T(663, 754, "será confirmada no arquivo-mestre. A área de proteção continua sendo X = C1.", 16, MARFIM, h=19)]
out["ov_p19"] = ov(items, "p19")

# ---------------------------------------------------------------- p. 20: mínimos impressos propostos
G = "#5E5A52"
items = [T(120, 788, "Impresso: 40 mm de largura (proposto).", 17.5, G, h=21),
         T(668, 788, "Impresso: 30 mm de largura (proposto).", 17.5, G, h=21),
         T(1077, 788, "Sem descritor.", 17.5, G, h=21),
         T(1077, 815, "Impresso: 25 mm (proposto).", 17.5, G, h=21),
         T(1450, 815, "Impresso: 8 mm de altura (proposto).", 17.5, G, h=21),
         T(120, 958, "Os mínimos em pixel valem para tela. Os mínimos impressos, em milímetros, são propostos e independentes dos pixels: confirmar em prova de gráfica.", 16, G, h=20)]
out["ov_p20"] = ov(items, "p20")

# ---------------------------------------------------------------- p. 21: erros adicionais
items = [T(120, 974, "Também evitar: recompor o nome com outra fonte, alterar a proporção entre símbolo e nome e usar a marca anterior ao lado da nova.", 15, G, h=20)]
out["ov_p21"] = ov(items, "p21")

# ---------------------------------------------------------------- p. 27: reserva de fonte e teste do favicon
items = [T(120, 806, "Símbolo à esquerda, nome em Montserrat, dados em Inter.", 20, G, h=24),
         T(120, 837, "Em clientes de e-mail sem essas fontes, usar Arial como reserva.", 20, G, h=24),
         T(120, 868, "Fundo branco, sem imagens extras, frases de efeito ou cores", 20, G, h=24),
         T(120, 899, "fora da paleta.", 20, G, h=24),
         T(1000, 948, "Antes de publicar, testar o favicon em 16 e 32 px reais.", 20, G, h=24)]
out["ov_p27"] = ov(items, "p27")

# ---------------------------------------------------------------- p. 30: fecho ancorado na transição real
items = ['<div class="t m" style="left:0;top:264px;width:1920px;text-align:center;font-size:16.5px;letter-spacing:.24em;line-height:22px;color:#C4A46F">A FORÇA DA CONVICÇÃO. O EQUILÍBRIO DA JUSTIÇA.</div>',
         f'<div class="t m" style="left:0;top:374px;width:1920px;text-align:center;font-size:84px;line-height:102px;color:{MARFIM}">O desenho ficou mais preciso.</div>',
         f'<div class="t m" style="left:0;top:469px;width:1920px;text-align:center;font-size:84px;line-height:102px;color:{GOLD}">O nome e as iniciais continuam.</div>']
out["ov_p30"] = ov(items, "p30")

# ---------------------------------------------------------------- p. 29: manifesto (página nova, fundo grafite)
paras = ["Antes, dois B lado a lado. Agora, dois B contrapostos sobre uma só haste, dentro de um único contorno.",
         "O que o escritório já era continua legível: o nome, as iniciais, a sobriedade.",
         "O que mudou foi a precisão: um desenho que cabe em um carimbo e em um favicon."]
ptxt = "".join(f'<p style="font-family:Montserrat;font-weight:500;font-size:37px;line-height:52px;color:{CREME};margin-bottom:38px">{t}</p>' for t in paras)
body = f"""
<div class="abs" style="left:200px;top:330px">{symbol(CREME, CREME, height=380)}</div>
<div class="abs" style="left:780px;top:322px;width:1px;height:430px;background:{BORDO}"></div>
<div class="abs" style="left:846px;top:310px;width:900px">{ptxt}</div>
"""
p29 = page("dark", "20", "Manifesto final", body, "29", "Manual · 20 Manifesto final")
p29 = p29.replace(f".dark{{background:{PRETO};color:{MARFIM}}}", f".dark{{background:{GRAF};color:{MARFIM}}}")
out["p29_manifesto"] = p29

# ---------------------------------------------------------------- p. 32: produção da papelaria (proposta)
hdrs = ["Peça", "Formato final", "Sangria", "Margem de segurança", "Papel", "Acabamento"]
rows = [
 ("Cartão de visita", "90 × 50 mm", "3 mm", "5 mm", "a definir", "a definir"),
 ("Envelope DL", "110 × 220 mm", "3 mm", "5 mm", "a definir", "a definir"),
 ("Papel timbrado A4", "210 × 297 mm", "3 mm", "a definir", "a definir", "a definir"),
 ("Capa de documento A4", "210 × 297 mm", "3 mm", "a definir", "a definir", "a definir"),
 ("Pasta A4", "a definir (depende da faca)", "a definir", "a definir", "a definir", "a definir"),
]
th = "".join(f'<th style="text-align:left;font-family:Montserrat;font-weight:600;font-size:12.5px;letter-spacing:.16em;text-transform:uppercase;color:{BORDO};padding:0 18px 14px 0;white-space:nowrap">{h}</th>' for h in hdrs)
def cell(v, first=False):
    pend = v.startswith("a definir")
    style = (f"font-family:Montserrat;font-weight:500;font-size:20px;color:{GRAF}" if first else
             (f"font-family:Inter;font-size:18px;color:#8A867E;font-style:normal" if pend else f"font-family:Inter;font-size:18px;color:{GRAF}"))
    return f'<td style="padding:17px 18px 17px 0;border-top:1px solid rgba(32,36,42,.16);vertical-align:top;{style}">{v}</td>'
trs = "".join("<tr>" + "".join(cell(v, i == 0) for i, v in enumerate(r)) + "</tr>" for r in rows)
body = f"""
<h1 class="abs" style="left:120px;top:145px;width:1000px">Papelaria: o que a gráfica precisa saber.</h1>
<p class="abs" style="left:1260px;top:158px;width:540px;font-family:Inter;font-size:19px;line-height:30px;color:#5E5A52">Proposta de especificação. Formatos conforme normas e usos correntes. Tudo o que está “a definir” depende da gráfica escolhida e de prova de cor.</p>
<table class="abs" style="left:120px;top:320px;width:1680px;border-collapse:collapse"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody>
<tfoot><tr><td colspan="6" style="border-top:1px solid rgba(32,36,42,.16)"></td></tr></tfoot></table>
<div class="abs" style="left:120px;top:760px;width:1680px;display:flex;gap:70px">
 <div style="width:520px"><div class="k" style="color:{BORDO};font-size:13px">Cor</div><p style="margin-top:10px;font-family:Inter;font-size:17px;line-height:27px;color:#5E5A52">Valores oficiais nas páginas 12 e 13. CMYK é referência calculada do RGB. Prova de cor obrigatória antes da tiragem.</p></div>
 <div style="width:520px"><div class="k" style="color:{BORDO};font-size:13px">Dourado</div><p style="margin-top:10px;font-family:Inter;font-size:17px;line-height:27px;color:#5E5A52">Tinta especial ou hot stamping fosco, com especificação acertada com a gráfica. Nenhum Pantone foi adotado.</p></div>
 <div style="width:520px"><div class="k" style="color:{BORDO};font-size:13px">Dados de contato</div><p style="margin-top:10px;font-family:Inter;font-size:17px;line-height:27px;color:#5E5A52">Só dados confirmados pelo profissional. Campos entre colchetes nos modelos são marcadores.</p></div>
</div>
"""
out["p32_producao"] = page("light", "22", "Produção da papelaria", body, "32", "Manual · 22 Produção da papelaria")

for name, html in out.items():
    open(f"{B}/{name}.html", "w", encoding="utf-8").write(html)
print("ok", list(out))
