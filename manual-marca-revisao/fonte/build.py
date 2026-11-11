#!/usr/bin/env python3
# Gera as páginas revisadas do manual BÍLIO & BÍLIO (1920x1080 px = 1440x810 pt).
# Símbolo: caminhos vetoriais extraídos da página 16 do PDF original (derivado, não é o arquivo-mestre).
import re, os, sys
B = os.path.dirname(os.path.abspath(__file__))
svg = open(f"{B}/simbolo_derivado_do_pdf.svg", encoding="utf-8").read()
paths = re.findall(r'<path fill="(#[0-9A-Fa-f]{6})" d="([^"]+)"', svg)
BAR_D, BODY_D = paths[0][1], paths[1][1]
VB = re.search(r'viewBox="([^"]+)"', svg).group(1)
vx, vy, vw, vh = [float(v) for v in VB.split()]

GOLD, BORDO, GRAF, PRETO, MARFIM, CREME = "#C4A46F", "#8F021D", "#20242A", "#151719", "#F4F0E8", "#F2E6CF"

def symbol(bar, body, width=None, height=None, extra_attrs=""):
    if height is not None:
        width = height * vw / vh
    h = width * vh / vw
    return (f'<svg {extra_attrs} xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" width="{width:.1f}" height="{h:.1f}">'
            f'<path fill="{bar}" d="{BAR_D}"/><path fill="{body}" d="{BODY_D}"/></svg>')

CSS = f"""
@font-face{{font-family:'Montserrat';src:url(fonts/montserrat-latin-400-normal.woff2) format('woff2');font-weight:400;font-style:normal}}
@font-face{{font-family:'Montserrat';src:url(fonts/montserrat-latin-500-normal.woff2) format('woff2');font-weight:500;font-style:normal}}
@font-face{{font-family:'Montserrat';src:url(fonts/montserrat-latin-600-normal.woff2) format('woff2');font-weight:600;font-style:normal}}
@font-face{{font-family:'Inter';src:url(fonts/inter-latin-400-normal.woff2) format('woff2');font-weight:400;font-style:normal}}
@font-face{{font-family:'Inter';src:url(fonts/inter-latin-500-normal.woff2) format('woff2');font-weight:500;font-style:normal}}
@font-face{{font-family:'Inter';src:url(fonts/inter-latin-600-normal.woff2) format('woff2');font-weight:600;font-style:normal}}
@font-face{{font-family:'Inter';src:url(fonts/inter-greek-400-normal.woff2) format('woff2');font-weight:400;unicode-range:U+0370-03FF}}
@font-face{{font-family:'Inter';src:url(fonts/inter-greek-500-normal.woff2) format('woff2');font-weight:500;unicode-range:U+0370-03FF}}
@page{{size:1920px 1080px;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1920px;height:1080px;overflow:hidden}}
body{{font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.page{{position:relative;width:1920px;height:1080px;overflow:hidden}}
.dark{{background:{PRETO};color:{MARFIM}}}
.light{{background:{MARFIM};color:{GRAF}}}
.hdr{{z-index:3;position:absolute;left:120px;top:64px;width:1680px;height:18px;display:flex;align-items:center;font-family:Montserrat;font-weight:600;font-size:14.5px;letter-spacing:.18em;text-transform:uppercase;line-height:18px}}
.hdr .n{{margin-right:25px}}
.hdr .rule{{flex:1;height:1px;margin-left:24px}}
.dark .hdr .n{{color:{GOLD}}} .dark .hdr .rule{{background:rgba(196,164,111,.28)}}
.light .hdr .n{{color:{BORDO}}} .light .hdr .rule{{background:rgba(32,36,42,.16)}}
.ftr{{z-index:3;position:absolute;left:120px;top:1013px;width:1680px;display:flex;justify-content:space-between;font-family:Montserrat;font-weight:500;font-size:12.8px;letter-spacing:.18em;line-height:15px;text-transform:uppercase}}
.dark .ftr{{color:#8A867E}} .light .ftr{{color:#6A665D}}
h1{{font-family:Montserrat;font-weight:500;font-size:67px;line-height:75px;letter-spacing:0}}
.dark h1{{color:{MARFIM}}} .light h1{{color:{GRAF}}}
p.b{{font-family:Inter;font-weight:400;font-size:24px;line-height:37px}}
.dark p.b{{color:rgba(244,240,232,.78)}} .light p.b{{color:#5E5A52}}
.k{{font-family:Montserrat;font-weight:600;font-size:14px;letter-spacing:.18em;text-transform:uppercase}}
.abs{{position:absolute}}
"""

def page(cls, num, label, body, pageno, title="Manual"):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head>
<body><div class="page {cls}">
<div class="hdr"><span class="n">{num}</span><span>{label}</span><span class="rule"></span></div>
{body}
<div class="ftr"><span>BÍLIO &amp; BÍLIO · MANUAL DE IDENTIDADE VISUAL</span><span>{pageno}</span></div>
</div></body></html>"""

out = {}

# ---------------------------------------------------------------- P09 (B1) leitura simbólica
sw = 520
sh = sw * vh / vw
ox, oy = 120, 170   # origem do símbolo dentro do SVG do diagrama (900 x 800)
def fx(f): return ox + f * sw
def fy(f): return oy + f * sh
eyeL = (fx(.278), fy(.26)); eyeR = (fx(.768), fy(.26)); tip = (fx(.50), fy(1.0))
diagram = f"""
<svg class="abs" style="left:880px;top:100px" width="960" height="880" viewBox="0 0 960 880" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate({ox},{oy})">
    <svg width="{sw}" height="{sh:.1f}" viewBox="{VB}"><path fill="{CREME}" d="{BAR_D}"/><path fill="{GOLD}" d="{BODY_D}"/></svg>
  </g>
  <!-- eixo -->
  <line x1="{fx(.5):.1f}" y1="{oy-52}" x2="{fx(.5):.1f}" y2="{oy+sh+20:.1f}" stroke="{CREME}" stroke-opacity=".55" stroke-width="1.2" stroke-dasharray="5 6"/>
  <text x="{fx(.5):.1f}" y="{oy-62}" fill="{GOLD}" font-family="Montserrat" font-weight="600" font-size="12" letter-spacing="2.2" text-anchor="middle">EIXO DE SIMETRIA</text>
  <!-- olhar -->
  <line x1="{eyeL[0]:.1f}" y1="{eyeL[1]:.1f}" x2="{eyeR[0]:.1f}" y2="{eyeR[1]:.1f}" stroke="{PRETO}" stroke-opacity=".0"/>
  <circle cx="{eyeL[0]:.1f}" cy="{eyeL[1]:.1f}" r="6" fill="{CREME}" stroke="{PRETO}" stroke-width="2"/>
  <circle cx="{eyeR[0]:.1f}" cy="{eyeR[1]:.1f}" r="6" fill="{CREME}" stroke="{PRETO}" stroke-width="2"/>
  <polyline points="{eyeL[0]:.1f},{eyeL[1]:.1f} {eyeL[0]:.1f},{oy-95} 60,{oy-95}" fill="none" stroke="{CREME}" stroke-opacity=".7" stroke-width="1.2"/>
  <polyline points="{eyeR[0]:.1f},{eyeR[1]:.1f} {eyeR[0]:.1f},{oy-95} {eyeL[0]:.1f},{oy-95}" fill="none" stroke="{CREME}" stroke-opacity=".7" stroke-width="1.2"/>
  <text x="60" y="{oy-112}" fill="{GOLD}" font-family="Montserrat" font-weight="600" font-size="12" letter-spacing="2.2">CONTRAFORMAS SUPERIORES</text>
  <text x="60" y="{oy-72}" fill="{MARFIM}" fill-opacity=".8" font-family="Inter" font-size="17">Lembram o olhar.</text>
  <!-- focinho -->
  <circle cx="{tip[0]:.1f}" cy="{tip[1]-8:.1f}" r="6" fill="{CREME}" stroke="{PRETO}" stroke-width="2"/>
  <polyline points="{tip[0]:.1f},{tip[1]-8:.1f} {tip[0]:.1f},{tip[1]+40:.1f} {ox+sw+90:.1f},{tip[1]+40:.1f}" fill="none" stroke="{CREME}" stroke-opacity=".7" stroke-width="1.2"/>
  <text x="{ox+sw+100:.1f}" y="{tip[1]+36:.1f}" fill="{GOLD}" font-family="Montserrat" font-weight="600" font-size="12" letter-spacing="2.2">VÉRTICE</text>
  <text x="{ox+sw+100:.1f}" y="{tip[1]+60:.1f}" fill="{MARFIM}" fill-opacity=".8" font-family="Inter" font-size="17">Lembra o focinho.</text>
</svg>"""
body = f"""
<h1 class="abs" style="left:120px;top:200px;width:720px">Uma leitura,<br>não um<br>personagem.</h1>
<p class="b abs" style="left:120px;top:465px;width:690px">Visto de frente, o monograma lembra o rosto de um tigre. A semelhança é intencional e discreta: uma leitura simbólica, nunca uma ilustração.</p>
<p class="b abs" style="left:120px;top:612px;width:690px">O animal não faz parte do símbolo e não aparece dentro dele. A página seguinte fixa as regras de uso.</p>
<div class="abs" style="left:120px;top:800px;width:690px;border-top:1px solid rgba(244,240,232,.16);padding-top:18px">
  <span class="k" style="color:{GOLD}">Leitura a validar</span>
  <p class="abs" style="left:0;top:48px;width:690px;font-size:15px;line-height:23px;color:rgba(244,240,232,.78)">Correspondência proposta entre as formas do símbolo e a leitura simbólica. O desenho oficial não é alterado: as marcações são sobrepostas apenas para leitura.</p>
</div>
{diagram}
"""
out["p09_tigre_leitura"] = page("dark", "07", "O tigre", body, "09", "Manual · 07 O tigre · leitura")

# ---------------------------------------------------------------- P10 (B1) regras de uso
rules = [
 ("01", "Dentro do símbolo", "Nem desenhado, nem visível por transparência através das áreas vazadas."),
 ("02", "Sobre a assinatura", "A marca não é aplicada sobre o rosto ou o corpo do animal (ver Como nunca usar)."),
 ("03", "Efeitos no símbolo", "Sem brilho, degradê, metalização ou halo, mesmo em peças de campanha."),
 ("04", "Origem da imagem", "Toda foto ou vídeo do animal tem fonte, crédito e autorização registrados antes do uso."),
]
rows = "".join(f"""<div style="display:flex;gap:34px;padding:26px 0;border-top:1px solid rgba(244,240,232,.16)">
<span class="k" style="color:{GOLD};width:34px;flex:none;padding-top:5px">{n}</span>
<div><div class="k" style="color:{MARFIM};font-size:15px">{t}</div><p style="margin-top:12px;font-family:Inter;font-size:21px;line-height:31px;color:rgba(244,240,232,.74);width:610px">{d}</p></div></div>""" for n,t,d in rules)
body = f"""
<h1 class="abs" style="left:120px;top:200px;width:800px">O tigre fica<br>fora do símbolo.</h1>
<p class="b abs" style="left:120px;top:400px;width:690px">O animal pode aparecer na comunicação do escritório como imagem de apoio. Nunca como parte da marca.</p>
<div class="abs" style="left:120px;top:640px;display:flex;align-items:flex-end;gap:34px">
  {symbol(CREME, GOLD, height=250)}
  <p style="font-family:Inter;font-size:15px;line-height:23px;color:rgba(244,240,232,.78);width:330px;padding-bottom:4px">Versão negativa oficial, em cores chapadas. As áreas vazadas ficam sempre em fundo sólido.</p>
</div>
<div class="abs" style="left:1060px;top:196px;width:740px">{rows}<div style="border-top:1px solid rgba(244,240,232,.16)"></div></div>
"""
out["p10_tigre_regras"] = page("dark", "07", "O tigre", body, "10", "Manual · 07 O tigre · regras de uso")

# ---------------------------------------------------------------- P11 (B2) coração, sem halo
hsz = 820
body = f"""
<div class="abs" style="left:110px;top:130px">{symbol(CREME, GOLD, height=hsz)}</div>
<h1 class="abs" style="left:1027px;top:231px;width:760px">No contorno,<br>um coração.</h1>
<p class="b abs" style="left:1027px;top:422px;width:700px">A base do símbolo se fecha em duas curvas que convergem para um vértice. O desenho protege como um escudo e, ao mesmo tempo, lembra um coração.</p>
<p class="b abs" style="left:1027px;top:555px;width:700px">É o lugar das pessoas na marca. Por trás de cada processo há uma vida, uma família ou um projeto. A técnica existe para servir a isso.</p>
<div class="abs" style="left:1027px;top:700px;width:680px">
  {"".join(f'<div style="display:flex;justify-content:space-between;align-items:center;height:57px;border-top:1px solid rgba(244,240,232,.16)"><span class="k" style="color:{GOLD};font-size:13px">{a}</span><span style="font-family:Inter;font-size:19px;color:{MARFIM}">{b}</span></div>' for a,b in (("Leitura","Compromisso humano"),("Forma","Curvas inferiores e vértice"),("Tom","Sóbrio, nunca sentimental")))}
  <div style="border-top:1px solid rgba(244,240,232,.16)"></div>
</div>
"""
p11 = page("dark", "08", "O coração", body, "11", "Manual · 08 O coração")
out["p11_coracao"] = p11

# ---------------------------------------------------------------- P12 cores (CMYK creme preenchido, rótulo CMYK ref.)
cols = [
 (0,411,GOLD,"Principal","Dourado fosco","#C4A46F","196 · 164 · 111","0 · 16 · 43 · 23",["Monograma, nome e descritor. Uso contido."],"d"),
 (412,411,BORDO,"Acento","Bordô","#8F021D","143 · 2 · 29","0 · 99 · 80 · 44",["Traço superior, “&” e pequenas ênfases.","Valor provisório."],"l"),
 (824,274,GRAF,"Base","Grafite","#20242A","32 · 36 · 42","24 · 14 · 0 · 84",["Fundos escuros e texto principal."],"l"),
 (1098,273,PRETO,"Base","Preto","#151719","21 · 23 · 25","16 · 8 · 0 · 90",["Fundos profundos."],"l"),
 (1371,275,MARFIM,"Base","Marfim","#F4F0E8","244 · 240 · 232","0 · 2 · 5 · 4",["Papel e fundos claros."],"d"),
 (1646,274,CREME,"Acento claro","Creme","#F2E6CF","242 · 230 · 207","0 · 5 · 14 · 5",["Traço e “&” na versão negativa."],"d"),
]
cells = ""
for x,w,bg,kick,name,hexv,rgb,cmyk,notes,tone in cols:
    fg = GRAF if tone=="d" else MARFIM
    line = "rgba(32,36,42,.28)" if tone=="d" else "rgba(244,240,232,.28)"
    dim = "rgba(32,36,42,.88)" if tone=="d" else "rgba(244,240,232,.88)"
    notes_html = "".join(f'<div style="font-size:15.5px;line-height:22px;color:{fg}">{n}</div>' for n in notes)
    rowdefs = (("HEX",hexv),("RGB",rgb),("CMYK*",cmyk))
    rws = "".join(f'<div style="display:flex;align-items:center;height:40px;border-top:1px solid {line}"><span style="font-family:Montserrat;font-weight:600;font-size:11px;letter-spacing:.18em;color:{dim};width:66px">{a}</span><span style="font-family:Inter;font-size:16.5px;color:{fg}">{b}</span></div>' for a,b in rowdefs)
    cells += f"""<div class="abs" style="left:{x}px;top:0;width:{w}px;height:1080px;background:{bg}">
<div class="abs" style="left:44px;top:667px;right:44px">
<div style="font-family:Montserrat;font-weight:600;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:{dim};height:27px">{kick}</div>
<div style="font-family:Montserrat;font-weight:500;font-size:34px;line-height:41px;color:{fg};height:57px">{name}</div>
{rws}<div style="border-top:1px solid {line}"></div>
<div style="margin-top:20px">{notes_html}</div></div></div>"""
p12 = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Manual · 09 Cores</title><style>{CSS}</style></head>
<body><div class="page light" style="background:{MARFIM}">{cells}
<div class="abs" style="left:44px;top:965px;width:340px;font-size:14px;line-height:20px;color:rgba(32,36,42,.92)">* CMYK de referência, calculado a partir do RGB. Confirmar em prova de gráfica.</div>
<div class="hdr" style="z-index:2"><span class="n" style="color:{GRAF}">09</span><span style="color:{GRAF}">Cores</span><span class="rule" style="background:rgba(32,36,42,.22)"></span></div>
<div class="ftr" style="z-index:2;justify-content:flex-end"><span style="color:#6A665D">12</span></div>
</div></body></html>"""
out["p12_cores"] = p12

# ---------------------------------------------------------------- P13 contraste (regra 3:1 corrigida)
cards = [
 ("Recomendado","7,6:1","Dourado sobre preto",PRETO,GOLD,"rgba(244,240,232,.6)",GOLD),
 ("Recomendado","6,6:1","Dourado sobre grafite",GRAF,GOLD,"rgba(244,240,232,.6)",GOLD),
 ("Recomendado","14,5:1","Creme sobre preto",PRETO,CREME,"rgba(244,240,232,.6)",CREME),
 ("Recomendado","8,4:1","Bordô sobre marfim",MARFIM,BORDO,BORDO,BORDO),
 ("Recomendado","13,7:1","Grafite sobre marfim",MARFIM,GRAF,BORDO,GRAF),
 ("Recomendado","7,7:1","Creme sobre bordô",BORDO,CREME,"rgba(244,240,232,.72)",CREME),
 ("Abaixo de 3:1","2,1:1","Dourado sobre marfim. Nunca em texto. Só o logotipo é isento.",MARFIM,GOLD,BORDO,"#5E5A52"),
 ("Não usar","1,9:1","Bordô sobre preto. Na negativa, o acento é o creme.",PRETO,BORDO,"rgba(244,240,232,.6)",CREME),
]
cx = [120,545,970,1395]; cy = [269,505]
ch = ""
for i,(k,r,n,bg,rc,kc,nc) in enumerate(cards):
    x=cx[i%4]; y=cy[i//4]
    bd = "border:1px solid rgba(32,36,42,.16);" if bg==MARFIM else ""
    ch += f"""<div class="abs" style="left:{x}px;top:{y}px;width:405px;height:216px;background:{bg};{bd}">
<div class="abs" style="left:25px;top:23px;font-family:Montserrat;font-weight:600;font-size:11.3px;letter-spacing:.18em;text-transform:uppercase;color:{kc}">{k}</div>
<div class="abs" style="left:25px;top:68px;font-family:Montserrat;font-weight:500;font-size:40px;line-height:50px;color:{rc}">{r}</div>
<div class="abs" style="left:25px;top:158px;right:25px;font-size:15px;line-height:21px;color:{nc}">{n}</div></div>"""
blocks = [
 ("Bordô provisório","O valor #8F021D foi medido na imagem original da marca. Deve ser confirmado em prova antes de virar padrão definitivo. A origem dos demais HEX será documentada."),
 ("CMYK de referência","Todos os valores CMYK, inclusive o do creme, foram calculados a partir do RGB e servem de ponto de partida. Toda impressão exige prova de gráfica."),
 ("Dourado físico","Em papel, o dourado pede tinta especial ou hot stamping fosco, com especificação acertada com a gráfica."),
]
bx = [120,699,1277]
bl = "".join(f'<div class="abs" style="left:{bx[i]}px;top:840px;width:520px"><div style="font-family:Montserrat;font-weight:600;font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:{BORDO};height:39px">{t}</div><div style="font-size:18px;line-height:28px;color:#5E5A52">{d}</div></div>' for i,(t,d) in enumerate(blocks))
body = f"""
<h1 class="abs" style="left:120px;top:145px">Contraste medido.</h1>
<p class="abs" style="left:1160px;top:160px;width:640px;font-size:19px;line-height:31px;color:#5E5A52">Razões calculadas pela fórmula WCAG 2. Texto corrente pede 4,5:1 ou mais. Elementos gráficos grandes pedem 3:1. O logotipo e os filetes decorativos são isentos.</p>
{ch}
<div class="abs" style="left:120px;top:818px;width:1680px;height:1px;background:rgba(32,36,42,.16)"></div>
{bl}
"""
out["p13_contraste"] = page("light", "09", "Cores", body, "13", "Manual · 09 Cores · contraste")

# ---------------------------------------------------------------- P31 (B9) anexo: quem assina
def person(x, img, nome, kick, areas):
    return f"""<div class="abs" style="left:{x}px;top:190px;width:476px">
<img src="{img}" style="display:block;width:476px;height:650px;object-fit:cover;object-position:top">
<div style="margin-top:22px"><div class="k" style="color:{GOLD};font-size:12px">{kick}</div>
<div style="margin-top:10px;font-family:Montserrat;font-weight:500;font-size:25px;line-height:31px;color:{MARFIM}">{nome}</div>
<div style="margin-top:8px;font-size:16px;line-height:22px;color:rgba(244,240,232,.7)">{areas}</div></div></div>"""
body = f"""
<h1 class="abs" style="left:120px;top:200px;width:620px">Quem<br>assina.</h1>
<p class="b abs" style="left:120px;top:370px;width:580px">Luciano da Silva Bílio e Fabiano da Silva Bílio, sócios do escritório.</p>
<div class="abs" style="left:120px;top:770px;width:600px;border-top:1px solid rgba(196,164,111,.5);padding-top:18px">
<span class="k" style="color:{GOLD};font-size:16px">Pendente</span>
<p style="margin-top:12px;font-size:19px;line-height:29px;color:rgba(244,240,232,.9)">Retratos dos arquivos do site, sem edição. Origem, autorização de uso e títulos a confirmar com os sócios antes de qualquer reprodução.</p></div>
{person(824,"luciano.jpg","Luciano da Silva Bílio","Sócio fundador","Processo Civil · Tributário")}
{person(1324,"fabiano.jpg","Fabiano da Silva Bílio","Sócio","Trabalhista · Responsabilidade Civil")}
"""
out["p31_quem_assina"] = page("dark", "21", "Quem assina", body, "31", "Manual · 21 Quem assina")

for name, html in out.items():
    open(f"{B}/{name}.html", "w", encoding="utf-8").write(html)
print("ok", list(out))
