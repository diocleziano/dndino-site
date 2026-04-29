# Definições

A secção **Definições** reúne as preferências globais do DnDino. Aqui não se trabalha sobre uma aventura ou personagem específica, mas define-se **como a aplicação se deve comportar no seu todo**.

As definições influenciam sobretudo:

- o aspeto geral da interface
- o comportamento da topbar
- o fluxo de `Locais`
- o comportamento do `Combate`
- a gestão de imagens, backups e snapshots
- o suporte e a parte de diagnóstico da base de dados

## Como o ecrã está organizado

A página está dividida em duas áreas:

- uma **barra lateral esquerda** com as categorias
- um **painel principal** à direita com as opções da secção selecionada

As categorias disponíveis são:

- `Geral`
- `Topbar`
- `Locais`
- `Combate`
- `Média`
- `Tema`
- `Base de dados`
- `Diagnóstico`
- `Suporte`
- `Licenças`

Esta estrutura separa bem as preferências de uso diário das opções mais técnicas, como backups e diagnóstico.

## Geral

A secção `Geral` reúne as preferências base da aplicação.

### Perfil do DM

Aqui podes personalizar o teu perfil com:

- `Nome de utilizador`
- `Género`

O nome é reutilizado noutras partes da aplicação, por exemplo na mensagem de boas-vindas da `Home`.

### Língua da interface

Podes decidir se queres:

- seguir a língua do sistema
- forçar uma língua específica da aplicação

### Confirmações globais

A opção `Pedir confirmação para eliminações` adiciona uma confirmação antes de ações destrutivas, como remoções e eliminações.

### Metadados

Em `Geral` encontras também:

- `Mostrar metadados na aplicação`

Esta opção decide se os painéis de metadados devem ou não ser mostrados nos ecrãs que os suportam.

### Disposição dos painéis da dashboard da aventura

Esta parte é importante se usas com frequência a `Dashboard da aventura`.

Podes:

- arrastar painéis
- reordená-los dentro da coluna esquerda ou direita
- movê-los de uma coluna para a outra

### Tema ativo

Em `Geral` também é mostrado o **tema atualmente selecionado** como resumo rápido. A alteração real do tema faz-se na secção `Tema`.

### Guias introdutórios

A partir daqui podes restaurar o comportamento de primeira utilização da aplicação.

O botão `Restaurar Primeiro Uso` faz com que o DnDino volte a considerar como não vistos os guias contextuais e os percursos introdutórios.

## Topbar

A secção `Topbar` define o comportamento das ferramentas rápidas presentes na barra superior da aplicação. Para a descrição completa de cada botão, consulta a página `Topbar`.

### Aspeto da topbar

Podes escolher se queres ver a topbar:

- apenas com ícones
- ou com ícones e nome por baixo

### Dado predefinido

Aqui podes escolher o **tipo de dado predefinido** do lançador de dados rápido.

### Abertura rápida de personagens

Esta definição controla o comportamento da abertura rápida de personagens.

Podes decidir se o atalho deve abrir:

- uma visualização mais orientada para leitura
- ou um modo mais próximo da edição

### Abertura rápida de regras

Esta definição controla a abertura rápida das `Regras`.

Daqui podes decidir se esse atalho deve abrir:

- o editor completo
- ou uma janela mais compacta e orientada para consulta

### Controlos da janela dos jogadores na topbar

A opção `Mostrar controlos da janela dos jogadores na topbar` mostra controlos rápidos para abrir ou fechar manualmente a `Janela dos Jogadores`.

## Locais

A secção `Locais` contém as preferências globais usadas como comportamento por defeito na dashboard dos locais.

### Papel de presença predefinido

Quando adicionas uma presença a um local, o DnDino pode propor um papel inicial predefinido.

### Mostrar mapas dos locais pai por defeito

Se ativares esta opção, no ecrã `Locais` os mapas herdados dos locais pai ficam logo visíveis.

### Memorizar o último local visitado

Se estiver ativo, quando regressas ao ecrã `Locais`, a aplicação tenta restaurar o último local selecionado para essa aventura.

### Fechar automaticamente o local anterior

Esta definição aplica-se durante uma **sessão live ativa**.

Quando um local é marcado como `Em visita`, o local que antes estava `Em visita` é automaticamente marcado como `Visitado`.

## Combate

A secção `Combate` reúne as preferências globais do sistema de combate.

Aqui encontras opções de apresentação e preferências que influenciam a `Janela dos Jogadores`.

### Ativar ecrã de combate para os jogadores

Este é o controlo principal. Se estiver desligado, o DnDino não usa a janela dos jogadores para mostrar intro, turno atual, round ou resumo final do combate, e as opções relacionadas ficam ocultas.

### Abrir a janela dos jogadores se estiver fechada

Se estiver ativo, o DnDino abre automaticamente a `Janela dos Jogadores` quando o combate começa. Se estiver desligado, a apresentação só é atualizada se a janela já estiver aberta.

### Abrir a janela dos jogadores mesmo com um só monitor

Esta opção aparece apenas se a abertura automática estiver ativa. Serve para usar a `Janela dos Jogadores` mesmo sem um segundo ecrã.

## Apresentação do combate

Esta subsecção controla as informações gerais mostradas aos jogadores durante o confronto:

- `Mostrar intro do combate aos jogadores`
- `Mostrar resumo final aos jogadores`
- `Mostrar round no ecrã dos jogadores`
- `Mostrar próximo turno no ecrã dos jogadores`

## Informações dos heróis

Estas opções aplicam-se quando o participante ativo é um herói ou aliado. Um NPC ou monstro marcado como `Aliado` também usa estas definições. Podes decidir se mostras:

- PV atuais, máximos e temporários
- condições ativas

## Informações dos PNJ

Estas opções aplicam-se apenas quando o participante ativo é um PNJ não aliado. PNJ marcados como `Aliado` usam as definições de heróis/aliados. Podes decidir separadamente se mostras:

- PV atuais, máximos e temporários
- condições ativas
- o nome real do PNJ

Se os nomes dos PNJ estiverem ocultos, a `Janela dos Jogadores` usa o nome genérico `PNJ`.

## Informações dos monstros

Estas opções aplicam-se apenas quando o participante ativo é um monstro não aliado. Monstros marcados como `Aliado` usam as definições de heróis/aliados. Podes decidir separadamente se mostras:

- PV atuais, máximos e temporários
- condições ativas
- o nome real dos inimigos

Se os nomes dos monstros/inimigos estiverem ocultos, a `Janela dos Jogadores` usa o nome genérico `Inimigo`.

## Média

A secção `Média` reúne as preferências para a gestão de imagens e da janela de apresentação.

### Imagens dos jogadores em ecrã inteiro

Se estiver ativa, as imagens mostradas aos jogadores são abertas em modo fullscreen.

### Imagens do DM no monitor principal

Esta opção faz com que a janela do DM seja aberta por defeito no primeiro ecrã disponível.

### Memorizar tamanho da janela do DM

Se estiver ativa, quando reabres uma nova imagem para o DM, a janela mantém:

- a última dimensão
- a última posição

## Manutenção de média

A secção `Manutenção de média` cobre o lado mais técnico da gestão de imagens.

A partir daqui podes lançar `Limpar média não utilizada`, que verifica os ficheiros de imagem guardados pela aplicação e remove aqueles que já não estão ligados a nenhuma entidade.

## Tema

A secção `Tema` permite escolher a **paleta global** da aplicação.

Cada tema mostra uma pequena pré-visualização com as cores principais, para que percebas logo como vai mudar o aspeto geral da interface.

## Base de dados

A secção `Base de dados` é uma das mais importantes para a segurança dos dados.

Aqui encontras:

- o caminho da pasta de dados
- o caminho da base de dados SQLite
- o caminho da pasta de backups
- informação sobre os snapshots mais recentes

### Backup automático

Podes escolher:

- a frequência do backup automático
- o número máximo de snapshots automáticos a manter

### Snapshots cloud

O DnDino também gere o comportamento dos snapshots cloud.

Daqui podes escolher como os guardados cloud se devem comportar e ver o estado atual através do texto de resumo mostrado no ecrã.

### Ações principais

No painel `Base de dados` encontras os principais botões de manutenção:

- `Abrir pasta de dados`
- `Abrir pasta de backups`
- `Criar snapshot...`
- `Restaurar snapshot...`
- `Restaurar a partir do iCloud`

### Reposição da aplicação

A função `Repor dados da aplicação` apaga:

- a base de dados da aplicação
- os média da aplicação

mas mantém os backups já criados.

### Últimos snapshots

Na parte inferior da secção `Base de dados`, o DnDino mostra também a lista dos últimos snapshots encontrados.

Para cada um são mostrados:

- nome do ficheiro
- data
- tamanho

## Diagnóstico

A secção `Diagnóstico` serve para controlar o estado técnico da base de dados SQLite usada pela aplicação.

Aqui podes:

- atualizar os dados de diagnóstico
- ver o caminho da base de dados
- confirmar se o ficheiro existe
- verificar tamanho e data de modificação
- ver a versão de SQLite

### Tabelas

O diagnóstico mostra também a lista das tabelas encontradas na base de dados, juntamente com o número de registos presentes em cada uma.

## Suporte

A secção `Suporte` reúne os canais rápidos para contactar quem desenvolve a aplicação.

Aqui encontras:

- o email de suporte
- o botão `Pedir suporte`
- o botão `Enviar uma sugestão`
- o botão `Copiar email`

## Licenças

A secção `Licenças` reúne as referências legais e de atribuição usadas pela aplicação.

Atualmente inclui, em particular, a parte relativa ao **System Reference Document 5.2** de Dungeons & Dragons, com referências:

- ao documento SRD
- à licença `CC-BY-4.0`

!!! tip
    Se estás a configurar o DnDino pela primeira vez, as secções mais úteis para verificar logo são `Geral`, `Topbar`, `Combate` e `Base de dados`. Normalmente são as que mais influenciam o uso diário e a segurança dos dados.
