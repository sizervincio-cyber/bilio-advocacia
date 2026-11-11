# Decisões finais (tomadas em nome do cliente, com justificativa)

O cliente pediu que as três pendências fossem decididas sem nova consulta. Abaixo, a escolha, o porquê e o que ela implica. Qualquer uma pode ser revertida.

## 1. Site publicado: o manual é a referência

**Decisão:** o manual de identidade visual (monograma dos dois B, Montserrat e Inter, paleta oficial) prevalece sobre o logotipo serifado azul-marinho e as fontes serifadas hoje no site.

**Por quê:**
- O manual é o documento aprovado e descreve a evolução da marca antiga; o logotipo azul-marinho do site não aparece no manual nem na marca anterior documentada. Duas identidades em uso enfraquecem as duas.
- O logotipo do site usa fios laterais, que a página 21 do manual proíbe.

**O que NÃO foi feito, de propósito:** não alterei o site no ar. Faltam os arquivos-mestre do monograma e das assinaturas; colocar em produção o símbolo extraído do PDF seria publicar um ativo não oficial. O hero atual também tem aparência de montagem e depende de fotografia real.

**Plano de migração (quando os arquivos-mestre chegarem):**
1. Trocar `assets/logo-bilio.png` (11815 × 3620 px, 10 MB) pela assinatura horizontal oficial em SVG.
2. Trocar Playfair Display, Spline Sans e IBM Plex Mono por Montserrat (títulos) e Inter (texto).
3. Aplicar a paleta oficial (dourado #C4A46F, bordô #8F021D, grafite #20242A, preto #151719, marfim #F4F0E8, creme #F2E6CF).
4. Substituir o hero pelas fotografias reais descritas em `04_direcao_fotografica_p22-24_p26_p28.md`.
5. Comprimir as imagens (hoje cerca de 40 MB).

## 2. Versão 9:16: suspensa; o 16:9 é o formato oficial

**Decisão:** a versão `BILIO_Manual_Marca_9x16.pdf` original fica suspensa e não deve ser distribuída. O arquivo oficial é `BILIO_Manual_Marca_16x9_v1.1.pdf`.

**Por quê:**
- O formato editorial 16:9 é o definido como base do manual.
- As páginas de fotografia (22 a 24, 26 e 28) vão mudar quando as fotos chegarem. Refazer a 9:16 agora obrigaria a refazê-la de novo.
- A versão 9:16 existente tem o mesmo texto da 16:9 antes das correções; mantê-la em circulação espalharia as contradições já corrigidas.

**Quando refazer:** depois de entregues os arquivos-mestre e as fotos reais, regenerar a 9:16 a partir dos mesmos arquivos-fonte (`fonte/`).

## 3. Capa: fica chapada, sem o símbolo-fantasma

**Decisão:** a capa (e a página 25) permanecem sem o fundo em imagem. Na página 25 há um símbolo-fantasma chapado, tom sobre tom; na capa, fundo liso.

**Por quê:**
- O fundo antigo tinha degradê dourado-marrom e reflexo, o que o próprio manual proíbe para o símbolo (páginas 6, 10 e 21).
- Um símbolo-fantasma atrás da assinatura exigiria sobrepor um vetor ao logotipo oficial; com opacidade baixa ele alteraria levemente a cor da assinatura. Capa limpa é mais fiel às cores oficiais.

## Observação de segurança do repositório

O repositório `sizervincio-cyber/bilio-advocacia` é **público**. A branch `ccr-bbd6c056-j6vtbi` contém o manual em revisão com os retratos dos sócios e dados de contato. Recomendo manter essa branch fora da `main` (que alimenta o site publicado) e, se o conteúdo for confidencial, tornar o repositório privado em Settings. Não alterei a visibilidade.
