# BÍLIO & BÍLIO · Relatório final de QA (rodadas 1 e 2)

Entregável: `BILIO_Manual_Marca_16x9_v1.1.pdf` · 32 páginas · 16:9 (1440 × 810 pt).
Original preservado, sem alteração: `BILIO_Manual_Marca_16x9.pdf`, SHA-256 `3e88af55375501ab746295c407face1b7d816f673b18731e37cdcf21dab1b5cd`.

## 1. Método

Edição cirúrgica sobre o PDF original. Nas páginas corrigidas por texto, o texto antigo foi removido do PDF (não apenas coberto) e o novo foi aplicado por cima, sem tocar nos gráficos. As páginas 9 a 13, 29, 31 e 32 foram refeitas em HTML com a mesma grade e as mesmas famílias (Montserrat e Inter). As demais são as páginas originais.

## 2. Mapa final de páginas

| Páginas | Situação | O que mudou |
|---|---|---|
| 6, 7, 14, 16, 24 | Originais | Só o rodapé ficou mais escuro (contraste 4,5:1); conteúdo visualmente idêntico |
| 1 | Corrigida | Fundo raster com degradê e reflexo removido (cover flat); "VERSÃO 1.1 · 2026" |
| 2 | Corrigida | Sumário com números de página e dois anexos (21 e 22) |
| 3 | Corrigida | "Dois B contrapostos" do símbolo antigo passa a "Dois B espelhados, lado a lado" |
| 4 | Corrigida | Hífen final eliminado; texto sem "contrapostos" (o termo fica só para a marca nova) |
| 8 | Corrigida | Rótulo "B" vira "B contraposto"; nota: destaques didáticos, não são variantes |
| 9, 10 | Refeitas (B1) | Tigre fora do símbolo: diagrama sobre o símbolo oficial (versão negativa, traço creme) e quatro regras de uso do animal |
| 11 | Refeita (B2) | Símbolo em versão negativa, dourado chapado, inteiro, sem halo |
| 12, 13 | Refeitas | CMYK do creme preenchido, rótulo "CMYK*"; regra 3:1 corrigida; blocos de rodapé atualizados |
| 17 | Corrigida | Versão contorno: fio medido e mínimos derivados; "fundo creme" corrigido para "fundo marfim" |
| 18, 19 | Corrigidas | Relações φ descritas só onde foram medidas; "barra superior"; ressalva explícita sobre a reduzida horizontal; φ agora em fonte sem serifa (Inter) |
| 20 | Corrigida | Mínimos impressos marcados "(proposto)"; nota sobre a margem incluída nas larguras; "proporcionais" removido |
| 21 | Corrigida | Erros adicionais, exceção do comparativo histórico, aviso de origem da foto do tigre |
| 23 | Corrigida | Nota: telefone, e-mail e endereço seguem o site do escritório e devem ser confirmados |
| 25 | Corrigida | Fundo raster com degradê e reflexo removido; símbolo-fantasma chapado, tom sobre tom |
| 27 | Corrigida | Arial como reserva no e-mail; teste do favicon em 16 e 32 px |
| 28 | Nota | "Imagens ilustrativas, origem a documentar. Substituição prevista." (fotos continuam, pendentes) |
| 29 | Refeita (manifesto) | Texto novo; fundo grafite; símbolo branco oficial; filete dourado |
| 30 | Corrigida | Fecho novo; espaço antes do ponto do lema removido |
| 31 (nova) | B9 | Quem assina: retratos do site sem edição, pendência em destaque |
| 32 (nova) | Produção | Especificação proposta da papelaria |

## 3. Verificações executadas

| Teste | Resultado |
|---|---|
| Páginas e formato | 32 páginas, todas 1440 × 810 pt |
| Páginas só do original | Nenhuma é idêntica byte a byte: todas as páginas editadas foram reescritas pela remoção do texto antigo. Conferi 6, 7, 14, 16 e 24 em recorte ampliado: iguais ao original, exceto o rodapé |
| Texto antigo removido | Busca de trechos antigos nas páginas editadas: nenhum restante |
| Fontes | Todas embutidas, CID TrueType, nenhuma Type 3, nenhuma fonte serifada de reserva |
| Seleção de texto | Funciona nas páginas novas e nas editadas |
| Cor do símbolo nas páginas refeitas | Amostra #C4A46F uniforme (sem degradê, sem halo) |
| Bordô sobre fundo escuro | Removido das páginas 9, 10 e 11 (usam a versão negativa, traço creme) |
| Contraste dos novos rodapés | 4,96:1 (escuro) e 5,03:1 (claro) |
| Favicon em pixels reais | `comparacao/favicon_teste_pixels_reais.png`: em 16 px sobram a silhueta e a barra; em 24 px é parcial; em 32 px lê bem |

## 4. Auditoria independente

Um revisor sem acesso à minha análise examinou o PDF (versão anterior a estas correções) e deu **7/10** em acabamento editorial. Tratamento de cada apontamento:

| Apontamento | Gravidade | Tratamento |
|---|---|---|
| Bordô sobre preto nas p. 9 a 11 (viola a p. 13) | Alta | **Corrigido**: versão negativa, traço creme |
| Degradê e reflexo no fundo da p. 25 (e da capa) | Alta | **Corrigido**: imagens removidas; p. 25 com símbolo chapado tom sobre tom |
| Dados de contato sem marcador (p. 23, 27) | Alta | **Esclarecido**: coincidem com os dados do site do escritório (não são fictícios). Nota na p. 23 diz isso e pede confirmação. Nada foi trocado por colchetes sem decisão do cliente |
| "Contrapostos" serve à marca antiga e à nova (p. 3, 4, 6) | Média | **Corrigido** |
| Pendências abertas em "versão 1.0" | Média | **Corrigido**: versão 1.1; ressalva na p. 19. Pendências listadas na seção 6 |
| Pendência da p. 31 pouco visível | Média | **Corrigido** |
| Foto do tigre sem crédito (p. 21, 28) | Média | **Sinalizado** nas duas páginas; resolução depende da origem |
| Amostras da p. 20 não batem com "tamanho real" | Média | **Esclarecido**: as larguras incluem a margem dos arquivos oficiais (nota nova) |
| p. 22: painel raster, régua do cabeçalho sobre a imagem, texto ilegível | Média | **Pendente**: exige novo mockup fotográfico (ver 04_direcao) |
| p. 28: cabeçalho e rodapé sobre fotos, baixa resolução | Média | **Pendente**: as fotos serão substituídas (ver 04_direcao) |
| φ em fonte serifada (p. 18, 19) | Baixa | **Corrigido** (Inter, glifo grego) |
| p. 5: ANTES e AGORA desalinhados, logo antigo em raster | Baixa | **Mantido**: preserva o arquivo original do escritório; alinhar exige novo layout |
| p. 29, 30: Montserrat no texto, símbolo creme, filete fraco | Baixa | **Corrigido** o símbolo (branco oficial) e o filete (dourado). Montserrat mantida: é texto de display, não texto corrente |
| p. 17, 21: legenda apertada, "creme" vs "marfim" | Baixa | **Corrigido** o nome da cor; legenda mantida com nota curta |
| p. 16, 17: descrições em rosa claro, fundo branco puro | Baixa | **Mantido** (páginas originais); registrado |
| Texto de 7 a 8,5 pt (p. 12, 13, 19, 27) | Baixa | **Mantido** nas originais; registrado |
| Régua do cabeçalho sobre faixas (p. 12, 14); tons rosados fora da paleta (p. 8) | Baixa | **Mantido**; registrado |
| p. 21 proíbe a marca antiga ao lado da nova | Baixa | **Corrigido**: exceção para comparativo histórico |
| p. 9: segundo olho sem chamada | Baixa | **Corrigido** |
| p. 32: título apertado contra a tabela | Baixa | **Corrigido** |
| Grid e ritmo vertical entre páginas vizinhas | Baixa | **Mantido** |

Depois destas correções não houve nova rodada de auditoria independente. A nota 7/10 refere-se à versão anterior.

## 4b. Rodada 3 (segunda auditoria independente)

Um segundo revisor, sem acesso ao primeiro relatório, deu **7,0/10** à versão anterior. Corrigi o que podia ser corrigido no PDF:

| Página | Correção |
|---|---|
| 4 | Coluna I com a mesma opacidade das colunas II e III |
| 8 | Rótulos neutros "B esquerdo", "Eixo comum", "B direito" (acaba o conflito "espelhado/contraposto") |
| 12 | Rótulos dos swatches com contraste maior; nota do CMYK mais escura |
| 13 | Regra: "o logotipo e os filetes decorativos são isentos" (cobre a linha bordô das peças escuras) |
| 15 | Exceção declarada: em e-mail, Arial como reserva |
| 20 | Margem das larguras passa para a nota inferior (sem apertar os cartões) |
| 22 | Regra alinhada ao exemplo da p. 24: marca centralizada na pasta e no cartão; capa de documento com marca reduzida no topo |
| 26 | Texto alinhado ao mockup: a horizontal vale no cabeçalho e, fora do hero, em telas estreitas |
| 27 | Texto dos ícones corrigido (amostra de 16 a 180 px; pacote de 16 a 512 px); aviso de origem dos dados do e-mail |
| 30 | Ponto final do lema colado à última letra |
| 32 | "a definir" com contraste 5:1 |
| 9, 10 | Legendas mais escuras |
| Rodapés | 22 páginas originais com rodapé mais escuro (4,5:1 ou mais) |
| Documento | 22 marcadores de navegação, 22 links no sumário, metadado "Versão 1.1 · 2026" |

Não corrigidos (dependem do cliente ou de arquivo-fonte): fotografias sem origem (p. 21, 26, 28, 31), logo antigo em baixa resolução (p. 3, 5), mockups raster de 105 ppi (p. 22, 28), marca-d'água sobre texto (p. 24), proporção do cartão no mockup (p. 23), enquadramento dos retratos (p. 31), círculo bordô da seta (p. 5), fundos fora da paleta (p. 22, 25, 26, 28), texto espaçado por letras que o Chrome gravou com espaços (limite do PDF original), PDF em RGB sem sangria (é de apresentação, não de gráfica).

Não houve terceira auditoria. A nota 7,0 refere-se à versão anterior a estas correções; as pendências restantes são as da seção 6.

## 5. Avisos

1. O símbolo usado nas páginas novas foi extraído do PDF (p. 16). É o mesmo desenho, em vetor, mas **não é o arquivo-mestre**. Substituir assim que o SVG ou AI oficial for enviado.
2. A leitura do tigre da p. 9 (contraformas, eixo, vértice) é proposta e está marcada "leitura a validar".
3. Retratos da p. 31: origem e autorização de uso desconhecidas; títulos e áreas são os do site.
4. Mínimos da p. 17 derivados de medição do vetor (fio de 0,175 pt em um símbolo de 55 pt); 0,25 pt é o fio mínimo usual de impressão. Confirmar em prova de gráfica.
5. Especificação da p. 32: formatos ISO e correntes; margem e sangria são proposta usual. Nada de papel ou acabamento foi inventado.
6. A relação C1 e altura do símbolo na versão reduzida horizontal (p. 19) **não foi medida** e a página agora diz isso.
7. Os rodapés das páginas originais continuam com o contraste do original (cerca de 4,1:1). Só as páginas refeitas têm o rodapé mais escuro.
9. A capa e a p. 25 perderam o fundo em imagem (degradê e reflexo). A capa ficou chapada, sem o símbolo-fantasma; se o escritório quiser o fantasma de volta, ele precisa ser refeito em vetor chapado.
8. Versão 9:16 não foi atualizada e está suspensa (ver `05_decisoes_finais.md`).

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
| 10 | ~~Decidir se o site segue o manual~~ Decidido: o manual é a referência; o site migra quando houver arquivo-mestre (ver `05_decisoes_finais.md`) | Site publicado |
| 11 | ~~Decidir sobre a versão 9:16~~ Decidido: 16:9 é o formato oficial; a 9:16 fica suspensa (ver `05_decisoes_finais.md`) | Versão 9:16 |

A direção para produzir o que falta está em `04_direcao_fotografica_p22-24_p26_p28.md`.

## 7. Arquivos

- `BILIO_Manual_Marca_16x9_v1.1.pdf`: manual revisado.
- `comparacao/`: antes e depois de todas as páginas alteradas, página nova 32, manifesto novo e teste de favicon.
- `fonte/`: HTML, scripts (`build.py`, `build2.py`, `render.js`, `patch2.py`), retratos, fontes e o símbolo derivado.
- `ativos_derivados/`: símbolo em SVG (derivado do PDF).
- `evidencias/`: recortes da Etapa A.
- Relatórios: `01_diagnostico_etapas_A_B.md`, `02_relatorio_etapa_C_QA.md` (rodada 1, histórico), este arquivo e a direção fotográfica.

Como remontar: `build.py`, `render.js` para as páginas 9 a 13, 31, `pdfunite` com as páginas originais (rev1), depois `build2.py`, `render.js` e `patch2.py`.
