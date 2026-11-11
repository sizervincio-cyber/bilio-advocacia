# BÍLIO & BÍLIO · Etapa C (implementação) e QA

Entregável: `BILIO_Manual_Marca_16x9_rev1.pdf` (31 páginas, 16:9, 1440 × 810 pt).
Base: `BILIO_Manual_Marca_16x9.pdf` original (SHA-256 `3e88af55375501ab746295c407face1b7d816f673b18731e37cdcf21dab1b5cd`), preservado sem alteração.

## 1. O que foi feito

Método cirúrgico: as páginas não tocadas são as páginas originais do PDF, copiadas sem recomposição. Só as páginas abaixo foram refeitas em HTML (mesma grade, mesmas famílias Montserrat e Inter) e encaixadas no lugar.

| Pág. | Decisão | O que mudou |
|---|---|---|
| 9 | B1 | Foto do tigre removida. Entra um diagrama sobre o símbolo oficial (eixo de simetria, contraformas superiores, vértice) e a marca "leitura a validar". Sai a lista "coragem, vigilância, autocontrole, estratégia". |
| 10 | B1 | Deixa de mostrar o tigre sob o símbolo. Passa a fixar quatro regras de uso do animal na comunicação (nunca dentro do símbolo, nunca sob a assinatura, sem efeitos, fonte e autorização registradas). |
| 11 | B2 | Mesmo texto. Símbolo em dourado chapado, inteiro, sem halo e sem recorte. Resolve a contradição com a p. 6 ("cores chapadas") e a p. 21 ("degradê ou brilho"). |
| 12 | Matriz | CMYK do creme preenchido (0 · 5 · 14 · 5, mesmo método dos demais). Rótulo "CMYK*" com nota: referência calculada do RGB, a confirmar em prova. |
| 13 | Matriz | O par 2,1:1 deixa de ser "só em tamanho grande" (era menor que os 3:1 da própria página). Agora: "abaixo de 3:1, nunca em texto, só o logotipo é isento". Blocos de rodapé atualizados (origem dos HEX, CMYK de referência). |
| 31 (nova) | B9 | Anexo "Quem assina": Luciano da Silva Bílio e Fabiano da Silva Bílio, com retratos e dados dos arquivos do site, sem edição. Marcado como pendente de origem, autorização e títulos. |

Por que 31 páginas: não existia página para os sócios. Inserir no meio deslocaria os números de rodapé das páginas originais 14 a 30, que não foram tocadas. O anexo no fim mantém todos os números e o sumário intactos.

Ajustes transversais nas páginas novas: o rodapé ficou mais escuro (contraste 4,96:1 no escuro e 5,03:1 no claro, contra cerca de 4,1:1 no original) e os pretos puros das p. 10 e 11 passaram ao Preto oficial #151719.

## 2. Verificação executada

| Teste | Resultado |
|---|---|
| Número de páginas e formato | 31 páginas, todas 1440 × 810 pt |
| Páginas não tocadas (1 a 8 e 14 a 30) | 25 de 25 idênticas ao original, pixel a pixel a 66 ppi |
| Fontes embutidas | 81 de 81 embutidas; todas CID TrueType (nenhuma Type 3) |
| Texto selecionável nas páginas novas | Sim (acentos preservados) |
| Cor do símbolo nas p. 9 a 11 | Amostrada: (196, 164, 111) = #C4A46F, uniforme |
| Contrastes do rodapé novo | 4,96:1 e 5,03:1 |
| Renderização visual das páginas novas | Conferida uma a uma; corrigidos rótulo coberto (p. 11), texto cortado (p. 9), rótulo CMYK quebrado (p. 12) |

Limite desta verificação: foi feita por mim, não por revisor independente. A Etapa D completa pede outra pessoa ou outra sessão confrontando o PDF com os arquivos-mestre.

## 3. Avisos importantes

1. **O símbolo usado nas páginas novas foi extraído do PDF original (p. 16), não é o arquivo-mestre.** O desenho é o mesmo, em vetor, mas deve ser substituído pelo SVG ou AI oficial assim que ele for enviado. Arquivos em `ativos_derivados/`, marcados como derivados.
2. **Diagrama da p. 9 (leitura do tigre).** A correspondência "contraformas = olhar, vértice = focinho" é proposta minha, derivada da imagem antiga da p. 10. Está marcada "leitura a validar" e precisa da confirmação do escritório ou de quem criou o símbolo.
3. **Retratos da p. 31.** Vieram do repositório do site. Não sei a origem nem a autorização de uso, e o retrato de Luciano tem acabamento que pode ter sido tratado digitalmente. Não foram alterados. Títulos e áreas usados são os do site.
4. Fontes: Montserrat e Inter em versão estática (Fontsource, licença SIL OFL). O nome interno de alguns pesos aparece como "MontserratThin-Medium", é só rótulo do arquivo de fonte; os pesos renderizados estão corretos.
5. Tamanho do arquivo: 5,5 MB (original 3,6 MB), pelos dois retratos.

## 4. O que NÃO foi feito (continua pendente)

| Página | Item | Depende de |
|---|---|---|
| 2, 4, 5, 8, 17, 18, 19, 20, 21 | Correções menores da matriz (sumário com páginas, hífen, rótulos, mínimos impressos em mm, relações φ explicitadas, mais exemplos de erro) | Aprovação; p. 19 e 20 também do arquivo-mestre |
| 22 a 24 | Papelaria: fotografia ou render com sombras plausíveis e ficha técnica | Dimensões, papel e acabamento da gráfica; dados confirmados |
| 26 | Hero | Fotografias reais do escritório |
| 27 | Teste em 16 e 32 px reais, fonte de reserva do e-mail | Pasta `06_REDUZIDA` |
| 28 | Painel de experiência da marca | Fotografias reais de materiais |
| 29 e 30 | Manifesto (B7) | Sua aprovação do rascunho do relatório 01 |
| Versão 9:16 | Não foi refeita | Decisão sobre manter as duas versões |
| Sumário (p. 2) | Não inclui o anexo da p. 31 | Decisão de editar a p. 2 |

## 5. Arquivos

- `BILIO_Manual_Marca_16x9_rev1.pdf`: manual revisado.
- `comparacao/antes_depois_p09-13.png`: antes (esquerda) e depois (direita), p. 9 a 13. `comparacao/p31_nova_pagina.png`: página nova.
- `fonte/`: HTML, `build.py` e `render.js` (geram as páginas e o PDF), retratos e fontes.
- `ativos_derivados/`: símbolo em SVG extraído do PDF, nas cores bordô e dourado, creme (negativa), dourado e grafite.
- `evidencias/`: recortes da Etapa A.

Como remontar: `python3 fonte/build.py`, depois `node fonte/render.js p09_tigre_leitura ...` e `pdfunite` com as páginas originais (`pdfseparate`).
