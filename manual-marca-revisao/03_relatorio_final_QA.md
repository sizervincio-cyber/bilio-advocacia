# BÍLIO & BÍLIO · Relatório final de QA (rodadas 1 e 2)

Entregável: `BILIO_Manual_Marca_16x9_rev2.pdf` · 32 páginas · 16:9 (1440 × 810 pt).
Original preservado, sem alteração: `BILIO_Manual_Marca_16x9.pdf`, SHA-256 `3e88af55375501ab746295c407face1b7d816f673b18731e37cdcf21dab1b5cd`.

## 1. Método

Edição cirúrgica sobre o PDF original. Nas páginas corrigidas por texto, o texto antigo foi removido do PDF (não apenas coberto) e o novo foi aplicado por cima, sem tocar nos gráficos. As páginas 9 a 13, 29, 31 e 32 foram refeitas em HTML com a mesma grade e as mesmas famílias (Montserrat e Inter). As demais são as páginas originais.

## 2. Mapa final de páginas

| Páginas | Situação | O que mudou |
|---|---|---|
| 1, 3, 5, 6, 7, 14, 15, 16, 22 a 26, 28 | Original, idênticas | Nada |
| 2 | Corrigida | Sumário com números de página e dois anexos (21 e 22) |
| 4 | Corrigida | Quebra de linha com hífen eliminada na coluna "Reconhecimento" |
| 8 | Corrigida | Rótulo "B" passa a "B contraposto"; nota: destaques didáticos, não são variantes |
| 9, 10 | Refeitas (B1) | Tigre fora do símbolo: diagrama sobre o símbolo oficial e quatro regras de uso do animal |
| 11 | Refeita (B2) | Símbolo em dourado chapado, inteiro, sem halo |
| 12 | Refeita | CMYK do creme preenchido; rótulo "CMYK*" com nota de referência |
| 13 | Refeita | Regra 3:1 corrigida; blocos de rodapé atualizados |
| 17 | Corrigida | Versão contorno: fio medido (cerca de 0,3% da altura) e tamanhos mínimos derivados (28 mm ou 320 px) |
| 18, 19 | Corrigidas | Relações φ descritas só onde foram medidas; "largura do símbolo" passa a "largura da barra superior" |
| 20 | Corrigida | Mínimos impressos marcados como "(proposto)"; nota deixa de dizer "proporcionais" |
| 21 | Corrigida | Nota com três erros adicionais (recompor o nome em outra fonte, alterar a proporção, usar a marca anterior junto) |
| 27 | Corrigida | Arial como reserva no e-mail; regra de testar o favicon em 16 e 32 px reais |
| 29 | Refeita (manifesto) | Texto novo ancorado na transição real; fundo grafite (o fundo vermelho com textura foi eliminado) |
| 30 | Corrigida | Fecho novo: "O desenho ficou mais preciso. O nome e as iniciais continuam."; espaço antes do ponto final do lema removido |
| 31 (nova) | B9 | Quem assina: Luciano e Fabiano, retratos do site sem edição, marcada como pendente |
| 32 (nova) | Produção | Especificação proposta da papelaria: formatos ISO e correntes, sangria 3 mm; papel e acabamento "a definir" |

## 3. Verificações executadas

| Teste | Resultado |
|---|---|
| Páginas e formato | 32 páginas, todas 1440 × 810 pt |
| Páginas só do original | 20 de 20 idênticas ao original, pixel a pixel (66 ppi) |
| Páginas alteradas por texto | Exatamente as 11 previstas (2, 4, 8, 17, 18, 19, 20, 21, 27, 29, 30) |
| Texto antigo removido | Busca por 8 trechos antigos: nenhum encontrado nas páginas editadas |
| Fontes | 41 embutidas, todas CID TrueType, nenhuma Type 3 |
| Seleção de texto | Funciona nas páginas novas; acentos preservados |
| Cor do símbolo nas páginas refeitas | Amostra: #C4A46F uniforme (sem degradê, sem halo) |
| Contraste dos novos rodapés | 4,96:1 (escuro) e 5,03:1 (claro) |
| Favicon em pixels reais | `comparacao/favicon_teste_pixels_reais.png`: em 16 px sobram a silhueta e a barra superior; os detalhes internos se fundem. Em 24 px ainda é parcial. Em 32 px lê bem. Confirma o limite da p. 20 ("16 a 24 px, só como favicon"). |
| Contradições do diagnóstico | Resolvidas: p. 10 e 11 (símbolo), p. 13 (3:1), p. 18 e 19 (φ), p. 20 ("proporcionais") |

## 4. Auditoria independente

Um revisor sem acesso à minha análise examinou o PDF final. O resultado e o tratamento de cada apontamento estão na seção 6.

## 5. Avisos

1. O símbolo usado nas páginas novas foi extraído do PDF (p. 16). É o mesmo desenho, em vetor, mas **não é o arquivo-mestre**. Substituir assim que o SVG ou AI oficial for enviado.
2. A leitura do tigre da p. 9 (contraformas, eixo, vértice) é proposta e está marcada "leitura a validar".
3. Retratos da p. 31: origem e autorização de uso desconhecidas; títulos e áreas são os do site.
4. Mínimos da p. 17 derivados de medição do vetor (fio de 0,175 pt em um símbolo de 55 pt); 0,25 pt é o fio mínimo usual de impressão. Confirmar em prova de gráfica.
5. Especificação da p. 32: formatos ISO e correntes; margem e sangria são proposta usual. Nada de papel ou acabamento foi inventado.
6. A relação C1 e altura do símbolo na versão reduzida horizontal (p. 19) **não foi medida** e a página agora diz isso.
7. Os rodapés das páginas originais continuam com o contraste do original (cerca de 4,1:1). Só as páginas refeitas têm o rodapé mais escuro.
8. Versão 9:16 não foi atualizada.

## 6. Pendências que dependem do cliente

| # | Item | Bloqueia |
|---|---|---|
| 1 | Arquivos-mestre do monograma e das assinaturas (SVG, AI ou PDF vetorial) | Substituir o símbolo derivado, medir p. 19 |
| 2 | Fotos reais da fachada, do interior e dos sócios, com autorização | Páginas 26, 28 e 31 |
| 3 | Origem e autorização dos retratos do site | Página 31 |
| 4 | Pasta `06_REDUZIDA` e `favicon.ico` | Página 27 |
| 5 | Prova de gráfica (papel, acabamento, cor) | Páginas 12, 13, 20, 22 a 24, 32 |
| 6 | OAB/GO, título e endereço confirmados | Páginas 23 e 27 |
| 7 | Marca-d'água em petição e parecer: aceitável? | Página 24 |
| 8 | Validar a leitura do tigre (p. 9) | Página 9 |
| 9 | Confirmar o lema "A força da convicção. O equilíbrio da justiça." | Todo o manual |
| 10 | Decidir se o site segue o manual (logotipo, fontes) | Site publicado |
| 11 | Decidir se a versão 9:16 será mantida e atualizada | Versão 9:16 |

A direção para produzir o que falta está em `04_direcao_fotografica_p22-24_p26_p28.md`.

## 7. Arquivos

- `BILIO_Manual_Marca_16x9_rev2.pdf`: manual revisado.
- `comparacao/`: antes e depois de todas as páginas alteradas, página nova 32, manifesto novo e teste de favicon.
- `fonte/`: HTML, scripts (`build.py`, `build2.py`, `render.js`, `patch2.py`), retratos, fontes e o símbolo derivado.
- `ativos_derivados/`: símbolo em SVG (derivado do PDF).
- `evidencias/`: recortes da Etapa A.
- Relatórios: `01_diagnostico_etapas_A_B.md`, `02_relatorio_etapa_C_QA.md` (rodada 1, histórico), este arquivo e a direção fotográfica.

Como remontar: `build.py`, `render.js` para as páginas 9 a 13, 31, `pdfunite` com as páginas originais (rev1), depois `build2.py`, `render.js` e `patch2.py`.
