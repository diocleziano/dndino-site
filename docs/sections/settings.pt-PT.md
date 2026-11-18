# Definições

A secção **Definições** reúne as preferências globais do DnDino. Aqui não se trabalha sobre uma aventura ou personagem específica, mas define-se **como a aplicação se deve comportar no seu todo**.

As definições influenciam sobretudo:

- o aspeto geral da interface
- o comportamento da topbar
- o fluxo de `Locais`
- o comportamento do `Combate`
- a gestão de imagens, backups e snapshots
- o suporte e a parte de diagnóstico da base de dados

## Conteúdos, ajuda e novos temas

**Geral → Conteúdo oficial** mostra ou oculta catálogos SRD sem eliminar dados pessoais nem quebrar referências. O controlo é partilhado com as listas. Ver [Conteúdos oficiais](official-content.md).

Os botões de guia **?**, ativos por predefinição, podem ser desativados globalmente. **Halloween** junta-se aos temas; **Sistema** continua a seguir a aparência real do macOS. Barra superior, botões contextuais e menus têm disposições coerentes para manter ícones e textos legíveis.

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

### Manter o ecrã ligado

Em **Definições > Geral**, ative **Manter o ecrã ligado** para impedir que o ecrã se desligue automaticamente enquanto o DnDino está em primeiro plano. É útil durante uma sessão para consultar notas ou apresentar conteúdos sem utilizar constantemente o rato ou o teclado.

A opção está **desativada por predefinição**. Também funciona a bateria, mas aumenta o consumo de energia. A escolha é mantida entre aberturas da aplicação: ao mudar para outra aplicação, o pedido é libertado; ao regressar ao DnDino, é restabelecido se a opção continuar ativa. Pode desativá-la a qualquer momento no mesmo controlo.

Não requer permissões especiais nem altera as definições de segurança do macOS. Não impede o bloqueio manual, a suspensão pedida pelo utilizador, o fecho da tampa ou as proteções do sistema. Não garante impedir protetores de ecrã ou bloqueios impostos por políticas independentes.

Se o macOS não conseguir ativar a função, é apresentado um aviso: desative e volte a ativar a opção para tentar novamente. A reposição completa das definições também a desativa.

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

Gerencie os guias em [Repor aplicação e guias](#app-and-guide-reset): reabrir a introdução e repor guias contextuais são comandos separados, sem eliminação de dados.

## Topbar

A secção `Topbar` define o comportamento das ferramentas rápidas presentes na barra superior da aplicação. Para a descrição completa de cada botão, consulta a página `Topbar`.

### Aspeto da topbar

Podes escolher se queres ver a topbar:

- apenas com ícones
- ou com ícones e nome por baixo

### Dado predefinido

Aqui podes escolher o **tipo de dado predefinido** do lançador de dados em `Ferramentas rápidas`.

### Abertura rápida de personagens

Cada resultado tem dois botões circulares à direita: **Visualizar** abre a ficha compacta e **Editar** abre o editor. A linha por si só já não abre a ficha e não existe uma preferência global entre as ações. [Topbar](topbar.md).

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

As preferências de apresentação e visibilidade definem os **valores iniciais dos novos combates**. Para alterar um combate, usa [a gestão do segundo ecrã e a visibilidade](combat.md#player-screen-options), também com ações em grupo. As escolhas guardadas nos outros combates não são substituídas.

A ativação do ecrã dos jogadores e a abertura das janelas mantêm-se globais. Os combates anteriores não concluídos guardam os valores iniciais uma única vez, na primeira abertura.

### Ativar ecrã de combate para os jogadores

Estes controlos aparecem apenas se **Ativar ecrã de combate para os jogadores** estiver ativo em **Definições > Combate**. Desativar esta opção oculta os controlos na preparação e durante o combate, sem apagar as escolhas guardadas. Não é necessário ter um segundo monitor ligado nem a janela dos jogadores já aberta.

### Abrir a janela dos jogadores se estiver fechada

Se estiver ativo, o DnDino abre automaticamente a `Janela dos Jogadores` quando o combate começa. Se estiver desligado, a apresentação só é atualizada se a janela já estiver aberta.

### Abrir a janela dos jogadores mesmo com um só monitor

Esta opção aparece apenas se a abertura automática estiver ativa. Serve para usar a `Janela dos Jogadores` mesmo sem um segundo ecrã.

## Apresentação do combate

Estas opções definem os valores iniciais de apresentação dos novos combates; podes alterá-los num combate sem mudar as definições:

- `Mostrar intro do combate aos jogadores`
- `Mostrar resumo final aos jogadores`
- `Mostrar round no ecrã dos jogadores`
- `Mostrar duração do encontro no ecrã dos jogadores`
- `Mostrar próximo turno no ecrã dos jogadores`

A duração do encontro é mostrada como um temporizador legível; se o combate estiver em pausa, a contagem pára.

## Informações dos heróis

Estas opções definem a visibilidade inicial dos participantes do tipo herói nos novos combates. Podes decidir se mostras:

- PV atuais, máximos e temporários
- condições ativas

## Informações dos PNJ

Estas opções definem a visibilidade inicial dos PNJ nos novos combates, mesmo quando têm o papel de Aliado. Podes decidir separadamente se mostras:

- PV atuais, máximos e temporários
- condições ativas
- o nome real do PNJ

Se os nomes dos PNJ estiverem ocultos, a `Janela dos Jogadores` usa o nome genérico `PNJ`.

## Informações dos monstros

Estas opções definem a visibilidade inicial dos monstros nos novos combates. Os seus PV e condições seguem estas opções mesmo quando são aliados; os nomes dos monstros não inimigos ficam inicialmente visíveis. Podes decidir separadamente se mostras:

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
## Novidades da versão 1.4

A secção `Base de dados` agora é `Base de dados e multimédia`.

Nas versões de lançamento, DnDino já não mostra caminhos técnicos internos. Em vez disso, a secção foca-se em informações úteis: tamanho da base de dados, número de imagens guardadas, tamanho total das imagens, instantâneos, exportação de backup e exportação de multimédia.

Instantâneos e multimédia da app podem ser exportados para uma localização escolhida pelo utilizador usando o painel padrão de guardar do macOS. A multimédia continua copiada dentro da sandbox da app, para que DnDino não perca referências caso os ficheiros originais sejam movidos ou apagados.

A secção Diagnóstico fica reservada para builds de debug e não aparece na versão de lançamento.

<!-- guide-coverage: MOD-042 MOD-043 MOD-049 MOD-051 MOD-060 MOD-061 MOD-062 MOD-070 MOD-071 MOD-073 MOD-077 MOD-078 MOD-079 MOD-080 MOD-086 MOD-088 MOD-145 MOD-146 MOD-147 MOD-148 MOD-163 MOD-164 MOD-168 MOD-170 -->

## Temas, fundos e opacidade

**Sistema** aparece primeiro e segue o macOS. Os outros temas são agrupados em **Paletas de cores**, **Especiais** e **Estações**. Especiais inclui **Inferno** e **Magia**; as quatro estações têm paisagens de fantasia ilustradas com aventureiros. Hero oferece os mesmos temas e imagens.

Desative o fundo decorativo ou importe um **fundo personalizado**. Apenas uma imagem é mantida; uma nova substitui a anterior. Trocar o tema desativa o fundo pessoal, mas não o apaga.

O controlo de opacidade atualiza imediatamente painéis compatíveis, incluindo títulos e pesquisa de locais, cabeçalho da aventura, cartões de heróis e sessões. Essas superfícies mantêm uma tonalidade mais escura ou transparência atenuada para leitura; textos, imagens e controlos não ficam transparentes. Outros painéis permanecem opacos. **Predefinido** restaura as opacidades originais e a posição correta do controlo, não um valor comum de 50%.

Mudar o tema recria o ecrã principal e volta a **Definições → Tema**. As janelas secundárias abertas e rascunhos não guardados ficam intactos; a barra inferior segue o tema. Botões principais e seleção lateral usam cores do tema com texto adaptado ao contraste. **Sistema** mantém os controlos nativos do macOS.

Consulta [Ligação ao Hero](hero-sync.md) para autorizações, histórico, início live automático opcional e diferenças entre desligar, remover associação e esquecer.

## Notificações e som {#notification-settings}

Em **Definições → Dispositivos Hero**, oculte o histórico inferior sem desativar avisos. Outro interruptor, ativo por predefinição, controla o som de **novas mensagens e pedidos de associação**. Alterações Live, ligações/desligações e alertas de combate são silenciosos. Veja [Notificações](topbar.md#notification-history).

## Repor aplicação e guias {#app-and-guide-reset}

Essas operações têm efeitos diferentes. Leia a explicação antes de confirmar.

- **Abrir guia introdutório** reabre a introdução sem apagar dados nem repor guias contextuais. A introdução 2.0.0 aparece também para quem concluiu a anterior.
- **Mostrar guias contextuais novamente** repõe os guias dos ecrãs, não a introdução. Deslocam-se até áreas fora de vista e abrem secções necessárias.
- **Repor dados**, também em Base de dados e Multimédia, apaga arquivo e multimédia, preservando perfil, preferências, guias e cópias de segurança locais/iCloud.
- **Eliminar cópias de segurança locais** remove cópias manuais e automáticas geridas pelo DnDino, não dados atuais nem ficheiros exportados.
- **Eliminar cópia iCloud** remove apenas o snapshot da aplicação, quando disponível. Cópias de segurança futuras podem recriá-lo se permanecerem ativas.
- **Reposição completa**, separada no final com confirmação dupla, apaga dados, multimédia, cópias de segurança geridas, fundo pessoal, credenciais Hero, perfil, preferências e guias, e fecha a aplicação. Ficheiros exportados em outros locais ficam intactos.

Feche a sessão live e janelas secundárias antes de operações no arquivo. Sem iCloud, escolha explicitamente a reposição local; se a eliminação cloud solicitada falhar, os dados locais não são apagados. Essas ações não podem ser desfeitas: exporte antes o que deseja manter.
