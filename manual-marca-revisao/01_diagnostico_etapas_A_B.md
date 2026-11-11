# BÍLIO & BÍLIO · Revisão do Manual de Identidade Visual
## Etapa A (Diagnóstico) e Etapa B (Proposta de intervenção)

Arquivos analisados: `BILIO_Manual_Marca_16x9.pdf` (30 páginas, 1440 × 810 pt) e `BILIO_Manual_Marca_9x16.pdf` (30 páginas). O texto das duas versões é idêntico, só muda o reflow (única diferença: a quebra de linha "reencontrá-la"). Toda a análise visual foi feita na versão 16:9.

Status: **Etapas A e B concluídas. Etapa C parcial (B1, B2, B9 e correções das p. 12 e 13) entregue: ver `02_relatorio_etapa_C_QA.md`. O restante aguarda aprovação e os ativos da seção 7.**

---

## 1. TL;DR

1. **A base é boa e deve ser preservada.** Monograma, assinaturas, paleta, tipografia, tabela de transformação (p. 6), geometria (p. 7), erros de uso (p. 21) e a metodologia WCAG (p. 13) estão corretos e consistentes. As proporções declaradas nas páginas 18 e 19 foram confirmadas por medição no vetor.
2. **O problema está nas imagens e em três contradições internas.** As páginas 10 e 11 mostram o símbolo com degradê metálico e brilho, o que o próprio manual proíbe nas páginas 6 e 21. A página 10 mostra o tigre dentro do símbolo, o que a legenda nega. As páginas 26 e 28 usam cenas com aparência de montagem sintética.
3. **O manual não descreve o site que está no ar.** O site publicado usa outro logotipo (serifado azul-marinho, com fios laterais) e fontes serifadas (Playfair Display). Isso contradiz as páginas 15, 21 e 26.
4. **As especificações de produção não existem.** Faltam dimensões, papel, acabamento e sangria na papelaria (p. 22 a 24). Os tamanhos mínimos impressos (p. 20) não seguem proporção constante, apesar de a página declará-los "proporcionais".
5. **Nada nas imagens permite afirmar origem por IA.** O que há são indícios observáveis de aparência artificial e a ausência de crédito ou fonte em todas as imagens fotográficas. Detalhes na seção 4.

---

## 2. O que deve permanecer (não tocar)

| Elemento | Páginas | Por quê |
|---|---|---|
| Monograma dos dois B contrapostos, assinaturas horizontal e vertical | 5, 16, 17 | São os ativos oficiais, em vetor. |
| Tabela Antes/Agora | 6 | Texto preciso, ancorado em fatos verificáveis. |
| Construção do símbolo e regra de "não reconstruir" | 7 | Evita derivações não autorizadas. |
| Paleta (valores HEX/RGB) e sem Pantone inventado | 12 | Honesto: CMYK marcado como referência. |
| Contrastes WCAG | 13 | Recalculei os 8 pares: todos batem (diferença máxima de 0,05). |
| Montserrat e Inter, com fontes embutidas no PDF | 14, 15 | Verificado com `pdffonts`: 6 fontes, todas embutidas. |
| Proporções φ medidas | 18, 19 | Ver seção 5. |
| Página de erros de uso | 21 | Boa pedagogia. Só precisa de acréscimos pontuais. |
| Voz "não promete resultado" | 28 | Alinhada à ética da OAB (Provimento 205/2021). |
| Marca anterior "reproduzida do arquivo original" | 3 | Documenta a origem e preserva a transição histórica. |

---

## 3. Matriz página × problema × gravidade × correção

Gravidade: **C** crítica (contradiz o próprio manual ou compromete a identidade), **A** alta, **M** média, **B** baixa.

| Pág. | Problema e evidência observável | Grav. | Impacto | Correção proposta |
|---|---|---|---|---|
| 1 | Fundo é JPEG 1920 × 1080 a 96 ppi com monograma gigante recortado. Serve para tela, não para ampliação. Slogan "A força da convicção. O equilíbrio da justiça." precisa de confirmação de que é o lema aprovado. | B | Repetição de composição (ver 11, 25, 29) | Manter. Trocar o fundo por vetor do próprio monograma. Confirmar o lema. |
| 2 | Sumário numera seções (01 a 20), não páginas. Rodapé em cinza: contraste medido de cerca de 4,1:1, abaixo dos 4,5:1 que a p. 13 exige para texto. | M | Navegação e coerência com a regra própria | Acrescentar número de página ao sumário. Escurecer o rodapé até pelo menos 4,5:1. |
| 3 | Marca anterior sobre retângulo de branco ligeiramente diferente do fundo. | B | Acabamento | Recortar o raster com fundo transparente. |
| 4 | Quebra de linha com hífen em "reencontrá-/la". Textos pequenos sobre fundo escuro. | B | Microtipografia | Reescrever a frase sem hífen final. Subir o corpo mínimo. |
| 5 | Mesmo retângulo de fundo na marca antiga. | B | Acabamento | Igual à p. 3. |
| 6 | Sem problema. Observação: "cores chapadas" é violada pelas p. 10 e 11. | n/a | n/a | Manter. Resolver nas p. 10 e 11. |
| 7 | Diagrama didático correto. | n/a | n/a | Manter. Validar as linhas-guia contra o vetor oficial na Etapa C. |
| 8 | Três recortes do símbolo com opacidades diferentes ("B espelhado", "eixo comum", "B"). Parecem variantes de marca. O rótulo "B" é ambíguo. | M | Risco de uso indevido como variante | Legendar como "destaque didático, não é variante". Renomear o terceiro rótulo. |
| 9 | Foto frontal de tigre (1080 × 1920, 129 ppi), sem crédito. Composição de "retrato de fera" remete a esporte e entretenimento. Texto "Força que observa antes de agir" é cliché de branding. | A | Desloca a marca do registro jurídico | Substituir por diagrama sobre o símbolo oficial (proposta B1). |
| 10 | **Contradição interna.** O tigre aparece pelas áreas vazadas do símbolo, mas a legenda diz que ele "nunca é desenhado dentro do símbolo". O símbolo está em degradê laranja metálico: cor média medida RGB (161, 105, 21), contra o oficial #C4A46F = (196, 164, 111). Viola "cores chapadas" (p. 6) e "aplicar degradê ou brilho" (p. 21). A imagem é raster 1920 × 1080 a 96 ppi, portanto o símbolo aqui **não é o arquivo-mestre**. Legenda cita "quadro do filme da marca" sem fonte. | C | Quebra a regra central do manual | Remover a imagem. Reaproveitar a página (proposta B1). |
| 11 | O símbolo está em bronze com **halo luminoso** na borda: cor média RGB (131, 92, 30). Raster 1920 × 1080. Mesma violação da p. 21. O tom é dramático; o texto diz "sóbrio, nunca sentimental". | C | Contradição visual e textual | Refazer com o vetor oficial em dourado chapado (proposta B2). |
| 12 | CMYK de todas as cores reproduz exatamente a fórmula simples RGB para CMYK (verificado). Portanto não são valores de prova. Preto com K = 90 ficaria cinza em impressão. Creme tem CMYK "a definir", mas Marfim tem valor, embora ambos sejam calculáveis pelo mesmo método. Só o bordô é marcado como provisório, mas a origem do dourado também não é documentada. | M | Risco de impressão fora da cor | Marcar todos os CMYK como "referência, pendente de prova". Preencher o creme pelo mesmo método (0 · 5 · 14 · 5) com a mesma ressalva. Documentar a origem de cada HEX. **Sem Pantone.** |
| 13 | A legenda diz que gráficos grandes pedem 3:1, mas rotula 2,1:1 (dourado sobre marfim) como "só em tamanho grande". 2,1 é menor que 3. Falta incluir o par dourado sobre creme (1,9:1) e os pares de texto pequeno usados no próprio manual. | A | Regra inconsistente | Reescrever: "abaixo de 3:1, não usar para texto. O logotipo é isento da WCAG". Acrescentar os pares que faltam. |
| 14 | Sem problema. | n/a | n/a | Manter. |
| 15 | Regra "só sem serifa" está correta, mas o site publicado usa Playfair Display, Spline Sans e IBM Plex Mono. | A | Manual e site divergem | Decidir qual vale (seção 6, item D1). |
| 16 | Assinaturas em vetor. Sem problema. | n/a | n/a | Manter. |
| 17 | A versão "contorno" em fio fino cinza sobre branco é fraca em pequeno. | M | Leitura em dimensão pequena | Definir tamanho mínimo da versão contorno e espessura mínima de fio. |
| 18 | Medi o vetor. Descritor ÷ nome = 41 ÷ 109 = 0,376, contra 0,382 esperado (1/φ²). Largura do descritor = largura do nome. Confirmado. A frase "a razão áurea relaciona nome, descritor e símbolo" generaliza: só duas relações foram confirmadas. | B | Afirmação mais ampla que a prova | Reescrever listando apenas as relações medidas. |
| 19 | Vertical: largura do nome 948 ÷ largura da barra superior 584 = 1,623, contra φ = 1,618 (erro de 0,3%). Confirmado **se a "largura do símbolo" for a da barra superior** (o corpo mede 552). A relação da reduzida horizontal (C1 = altura do símbolo ÷ φ²) **não foi medida** (ver seção 5). | M | A regra precisa dizer qual largura | Explicitar "largura da barra superior". Medir a reduzida na Etapa C com o arquivo-mestre. |
| 20 | Tamanhos impressos: 240 px = 40 mm, 160 px = 30 mm, 120 px = 25 mm, 32 px = 8 mm. A razão mm/px é 0,167, 0,188, 0,208, 0,250. Não é constante, apesar de a nota dizer "estimativas proporcionais". A 96 ppi, 240 px seriam 63,5 mm. Mistura de unidades de tela e impressão. | A | Especificação de impressão sem base | Definir mínimos impressos em mm, medidos no arquivo, e mínimos de tela em px, separados. Confirmar em prova. |
| 21 | Bom. Faltam exemplos para a versão vertical e para o símbolo isolado. | B | Cobertura | Acrescentar 2 a 4 erros (nome recomposto em fonte, desproporção símbolo/nome, mistura com a marca antiga). |
| 22 | Mockup em composição plana: sombras suaves e uniformes, sem espessura de papel nem textura visível. | M | Não é demonstração material | Fotografia de estúdio ou render com sombras plausíveis (B3). |
| 23 | Cartão e papéis com marcadores honestos, mas "Sócio fundador" e o endereço não estão marcados como pendentes. Faltam dimensões, papel, acabamento e sangria. | A | Dados não sinalizados e sem especificação | Ficha técnica por peça (B3). Marcar o que não foi confirmado. |
| 24 | Marca-d'água do símbolo parece sobreposta às linhas finais do texto em petição e parecer (conferir em zoom na Etapa C). Em petição eletrônica pode ser indesejável. | M | Legibilidade e regras do tribunal | Verificar com o escritório. Propor versão sem marca-d'água para peças a protocolar. |
| 25 | Quarta ocorrência da composição "símbolo gigante recortado em fundo escuro" (p. 1, 11, 25, 29). | M | Repetição sistemática | Variar uma ou duas ocorrências. |
| 26 | **Hero.** Composição com estátua da Justiça em primeiro plano, obelisco com três figuras (lembra o Monumento às Três Raças, de Goiânia), ponte em arco, prédio art déco e linhas de projeto arquitetônico sobrepostas. Indícios de montagem: escala incoerente entre estátua e monumento, luz da estátua e do céu em direções diferentes, graduação dourada uniforme. A própria legenda diz "composição montada". Raster 1672 × 941 a 162 ppi. | C | Ponto de maior risco de artificialidade | Direção fotográfica nova (B4). |
| 27 | Ícones de 16 a 24 px aparecem ampliados na página, o que pode sugerir mais legibilidade do que existe em tela real (a p. 20 limita 16 a 24 px a favicon). Falta teste em 16 e 32 px reais. Fontes das assinaturas de e-mail (Montserrat) não existem em clientes de e-mail. Os arquivos `06_REDUZIDA` citados não foram fornecidos. | A | Pode sugerir legibilidade maior que a real | Testar em 16 e 32 px reais. Definir fonte de reserva. Receber os arquivos (B5). |
| 28 | Painel de 4 fotos: caneta-tinteiro, estátua rachada com tigre, borda de livro e textura vermelha. Estátua e tigre em escala impossível, com partículas flutuando. Borda de livro com geometria incoerente. A textura vermelha lê como carne crua, não como "veludo". O rótulo da seção e o rodapé correm sobre as fotos. | C | Associações improváveis e sintéticas | Painel material com papel, metal, madeira, fotografia real (B6). |
| 29 | Fundo vermelho desfocado (a mesma textura da p. 28). Texto repete a estrutura "X encontra Y" três vezes. | A | Clichê e repetição sintática | Manifesto novo (B7). |
| 30 | "Não mudamos aquilo que nos define. Demos forma ao que nos move." Fórmula de efeito, sem ancoragem factual. Verificar espaço antes do ponto em "JUSTIÇA ." | M | Genérico | Texto ancorado na transição real do símbolo (B7). |

### Problemas transversais

| Tema | Evidência | Grav. |
|---|---|---|
| Vocabulário repetido | No texto das 30 páginas: "força" 9 vezes, "justiça" 6, "convicção" 4, "equilíbrio" 4, "razão" 2, "coragem" 1. | M |
| Sem crédito nem fonte em nenhuma foto | Páginas 9, 10, 11, 26, 28. Os metadados do PDF não trazem origem. O PDF foi gerado por Chrome (Skia/PDF) a partir de HTML. | A |
| Imagens de baixa resolução | Páginas 1, 9, 10, 11, 25, 26, 28 em 96 a 195 ppi. | M |
| Sem especificação de produção | PDF só em RGB, sem sangria nem marcas de corte. Aceitável para apresentação, não para gráfica. | M |
| Manual versus site | O site usa logotipo serifado azul-marinho com fios laterais (proibidos na p. 21), fontes serifadas e a mesma cena do hero da p. 26. O manual não menciona essa identidade. | A |
| Fabiano Bílio e Luciano Bílio | Só Luciano aparece (cartão e e-mail). Fabiano não aparece em nenhuma página. | M |

---

## 4. Sobre origem das imagens (regra de prudência)

Não declaro que nenhuma imagem foi gerada por IA. O que o PDF permite afirmar:

| Nível | Imagens | Base |
|---|---|---|
| **Origem não documentada** | Tigre (p. 9, 10, 21, 28), estátua e hero (p. 26, 28), painel (p. 28) | Nenhum crédito, nenhuma fonte, nenhum arquivo original no PDF |
| **Aparência artificial** (indício, não prova) | Hero da p. 26, estátua com tigre da p. 28, textura vermelha da p. 28 | Escala e luz incoerentes, partículas, geometria inconsistente |
| **Manipulação digital comprovada** | Símbolo nas p. 10 e 11 | Cor e halo medidos, diferentes do vetor oficial |
| **Origem comprovada** | Marca anterior (p. 3, 5), assinaturas vetoriais | Legenda cita o arquivo original e os dados são vetoriais |

---

## 5. Auditoria matemática (o que foi medido)

| Item | Medido | Esperado | Resultado |
|---|---|---|---|
| Contraste dourado/preto, dourado/grafite, creme/preto, bordô/marfim, grafite/marfim, creme/bordô, dourado/marfim, bordô/preto | 7,61 · 6,60 · 14,54 · 8,42 · 13,71 · 7,74 · 2,08 · 1,88 | 7,6 · 6,6 · 14,5 · 8,4 · 13,7 · 7,7 · 2,1 · 1,9 | Confirmado |
| C2 ÷ C1 (horizontal, p. 16 a 18) | 41 ÷ 109 = 0,376 | 1/φ² = 0,382 | Confirmado (diferença de 1,5%) |
| Largura do descritor ÷ do nome | igual | igual | Confirmado |
| Largura do nome ÷ largura da barra superior (vertical) | 948 ÷ 584 = 1,623 | φ = 1,618 | Confirmado (0,3%) |
| Largura do nome ÷ largura do corpo do símbolo | 948 ÷ 552 = 1,717 | φ | Não confere. A regra depende de qual largura se mede. |
| Reduzida horizontal: C1 = altura do símbolo ÷ φ² | **não medido** | n/a | Pendente de arquivo-mestre |
| CMYK × fórmula simples | coincidem | n/a | São valores de referência, não de prova |
| mm/px nos mínimos impressos (p. 20) | 0,167 · 0,188 · 0,208 · 0,250 | constante | Não confere |

Observação: as medidas de largura e altura foram feitas por contagem de pixels em renderização de 200 dpi do PDF. Para a Etapa C, repito sobre o vetor-mestre.

---

## 6. Etapa B · Decisões editoriais propostas

Regra de ouro: nenhuma proposta altera o monograma, as assinaturas, a paleta ou as fontes. Variantes ópticas, se necessárias, saem em documento separado.

**B1. Tigre (p. 9 e 10).** Decisão: o tigre vira leitura conceitual, não personagem.
- P. 9: troca a foto por um diagrama sobre o símbolo oficial (linhas-guia, como na p. 7) que marca os "olhos" e o "focinho". Mantém o parágrafo curto, sem a lista de quatro virtudes.
- P. 10: deixa de mostrar o tigre sob o símbolo. Passa a tratar das **regras de uso do tigre na comunicação**: nunca dentro do símbolo, nunca com brilho, nunca em primeiro plano sobre a assinatura.
- Se o escritório tiver autorização e fonte documentada para uma foto, entra uma única imagem pequena, com crédito na legenda.
- Justificativa: elimina a contradição da p. 10 e mantém as 30 páginas.

**B2. Coração (p. 11).** Mesmo texto, símbolo oficial em vetor, dourado chapado, sem halo, sem recorte agressivo. Corrige a violação da p. 21.

**B3. Papelaria (p. 22 a 24).** Fotografia de estúdio ou render com sombras plausíveis. Ficha técnica de cada peça: dimensão final, margens, papel, acabamento, sangria, cor. Tudo que não estiver confirmado vai como "a definir com a gráfica". Dados de contato só os confirmados.

**B4. Hero (p. 26).** Substituir a cena por direção fotográfica plausível: fachada ou interior real do escritório (o Edifício Euro Working Concept é citado no site), retratos reais, detalhe de material. A assinatura vertical negativa permanece como está. Sem fotografias: entrego a direção de arte e a lista de pendências, não a imagem final.

**B5. Digital (p. 27).** Testes em 16, 32 e 48 px reais. Fonte de reserva na assinatura de e-mail. Receber o pacote `06_REDUZIDA`.

**B6. Experiência da marca (p. 28).** Painel de materiais reais: papel, metal fosco, madeira, arquitetura. Sem estátua com tigre. Sem textura que lembre carne.

**B7. Manifesto (p. 29 e 30).** Texto novo, ancorado na transição real: dois B separados, depois contrapostos em um eixo, contorno único, dourado chapado. Sem tricolon repetitivo e com pelo menos um fato verificável por frase. Rascunho abaixo.

> Antes, dois B lado a lado. Agora, dois B contrapostos sobre uma só haste, dentro de um único contorno.
> O que o escritório já era continua legível: o nome, as iniciais, a sobriedade.
> O que mudou foi a precisão: um desenho que cabe em um carimbo e em um favicon.

Texto de trabalho, para revisão do cliente. Não afirmo datas nem conquistas.

**B8. Cores (p. 12 e 13) e mínimos (p. 20).** Correções da matriz. Nenhum valor oficial alterado.

**B9. Protagonistas.** Acrescentar uma página (substituindo a repetição da p. 25) com **Luciano Bílio e Fabiano Bílio**, só com retratos confirmados. O repositório do site tem `team-luciano.png` e `team-fabiano.png`. Preciso da sua confirmação do direito de uso e dos títulos corretos.

---

## 7. Pendências que dependem do cliente

| # | Item | Bloqueia |
|---|---|---|
| 1 | Arquivos-mestre do monograma e das assinaturas (SVG, AI ou PDF vetorial) | Medições finais (p. 19), exportar pacote de ativos |
| 2 | Pasta `06_REDUZIDA` com ícones e `favicon.ico` | P. 27 |
| 3 | Origem e autorização do tigre, do "filme da marca" e das cenas das p. 26 e 28 | P. 9, 10, 26, 28 |
| 4 | Fotos reais: fachada e interior do escritório, Luciano e Fabiano | P. 26, 28, nova página dos sócios |
| 5 | Confirmação dos títulos ("Sócio fundador"), números da OAB e endereço (sala) | P. 23, 27 |
| 6 | Prova de gráfica para CMYK, dourado e papel | P. 12, 13, 20, 22 a 24 |
| 7 | Decisão sobre o site: o manual vale ou o logotipo serifado azul-marinho? | P. 15, 26, 27 |
| 8 | Marca-d'água em peças judiciais: permitida? | P. 24 |
| 9 | Confirmar o lema "A força da convicção. O equilíbrio da justiça." | Todo o manual |

---

## 8. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Reconstruir o PDF e alterar o que está aprovado | Trabalhar só nas páginas listadas. Comparar antes e depois página por página. Preservar os originais (hash SHA-256 do 16:9: `3e88af55…b5cd`). |
| Substituir imagens sem ter fotos reais | Entregar direção de arte e pendência, não imagem inventada. |
| Mudar o símbolo "sem querer" | Usar só os arquivos-mestre. Nenhuma recriação. |
| Rótulo "provisório" ficar para sempre | Lista de pendências com responsável. |

---

## 9. Próximos passos

1. **Você:** aprova ou ajusta as decisões B1 a B9 e responde às pendências 1, 3, 4 e 7.
2. **Etapa C:** reconstruo as páginas alteradas (HTML para PDF, mesma base técnica do original), mantendo as 30 páginas e o 16:9.
3. **Etapa D:** auditoria do PDF final, com comparação antes e depois e relatório de QA.

Sem os itens 1 e 4, a Etapa C entrega as páginas de texto, cores, medidas e papelaria, e deixa as páginas de fotografia marcadas como pendentes.

---

## Anexo · Evidências (pasta `evidencias/`)

- `p09-12_folha.png`: páginas 9 a 12 lado a lado.
- `p10_tigre_monograma.png`, `p11_coracao_halo.png`: base das medições de cor.
- `p26_hero_composicao.png`, `p28_painel_experiencia.png`: recortes ampliados.
- `site_hero-justica_reduzido.jpg`, `site_logo-bilio_reduzido.jpg`: ativos do site publicado, em versão reduzida.
