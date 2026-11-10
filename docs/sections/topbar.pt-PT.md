# Topbar

![Topbar](../images/en_topbar.png){ .img-hero }


A **topbar** é a zona de atalhos globais do DnDino. Mantém por perto as ferramentas mais usadas durante a preparação ou condução de uma aventura.

Pode mostrar só ícones ou ícones com nome por baixo, conforme a preferência escolhida em **Definições**.

## Comportamento Geral

Os botões à esquerda são atalhos globais. Alguns abrem uma secção completa, outros mostram um painel rápido para consultar algo sem sair do ecrã actual.

## Início

`Início` volta à página inicial da aplicação.

Usa-o para regressar à visão geral ou recomeçar a partir da entrada principal.

## Aventuras

`Aventuras` muda de comportamento conforme o contexto.

No **Início** ou em secções não ligadas a uma aventura específica, abre a lista de aventuras.

Dentro de um **painel de aventura**, dos **locais** ou de um **combate** ligado a uma aventura, volta ao painel dessa aventura.

## Personagens

Cada resultado tem dois botões circulares à direita: **Visualizar** abre a ficha compacta e **Editar** abre o editor. A linha por si só já não abre a ficha e não existe uma preferência global entre as ações.

## Equipamento

`Equip.` abre a pesquisa rápida de equipamento.

Pesquisa em:

- armas
- armaduras
- ferramentas
- equipamento de aventura

Podes pesquisar por nome, categoria, CA, dano, propriedades, utilização ou descrição. Os resultados abrem numa janela de consulta e os botões inferiores abrem as secções completas.

## Regras

`Regras` abre a pesquisa rápida de regras.

Pesquisa em:

- talentos
- glossário
- magias

Podes pesquisar por nome, categoria, pré-requisitos, tipo de regra, escola ou descrição. As magias abrem numa janela dedicada; talentos e glossário podem abrir em consulta ou modificação conforme as definições.

## Ferramentas Rápidas

`Ferramentas rápidas` reúne as ferramentas que podes precisar de imediato durante a preparação ou a sessão.

Daqui podes abrir:

- o **lançador rápido de dados**
- o **gerador de nomes**
- os **temporizadores rápidos**

### Lançador de dados

O lançador de dados permite escolher número de dados, tipo de dado e modificador.

O dado predefinido é configurado em **Definições**. O resultado mostra cada dado e o total, útil para testes rápidos e lançamentos improvisados.

### Gerador de nomes

Escolhe espécie, género e **nome completo** ou **apenas nome próprio**. Bloqueia nome próprio ou apelido para gerar novamente só a outra parte, ou regenera uma proposta individual. Copia um resultado ou recupera-o do histórico recente, partilhado com o acesso rápido. O histórico pode ser limpo.

### Temporizadores rápidos

Os temporizadores rápidos ajudam a controlar tempos de mesa sem sair do ecrã atual.

Podes dar um nome ao temporizador, escolher a duração com um controlo ao estilo macOS e executar até quatro temporizadores ao mesmo tempo. Cada temporizador pode ser pausado, retomado, parado ou removido.

## Definições

`Definições` abre as preferências da aplicação: idioma, tema, topbar, painéis, combate, Janela dos Jogadores, base de dados, diagnóstico e suporte.

## Sessão em direto na barra inferior {#live-session-control}

Numa página da aventura, abre **Sessão em direto** na **barra inferior**, à esquerda do Hero. Clica em **Iniciar** e confirma para começar uma sessão da aventura atual.

Se houver uma sessão aberta, o controlo continua acessível fora da aventura. Não é possível iniciar uma segunda em paralelo. [Guia da sessão em direto](live-session.md#live-session-bottom-bar).

## Janela dos Jogadores ao Centro

Se a opção estiver activa, o centro da topbar também mostra os controlos da **Janela dos Jogadores**.

Servem para abrir ou fechar manualmente a janela dos jogadores, útil para mostrar imagens, combates ou resumos num segundo ecrã.

## Quando Usar

Usa a topbar para:

- voltar rapidamente dos locais ao painel da aventura
- pesquisar uma regra sem mudar de ecrã
- consultar uma personagem ou item rapidamente
- fazer um lançamento rápido, iniciar um temporizador ou gerar um nome improvisado
- gerir uma sessão live a partir da secção actual

## Preencher a janela principal {#fill-main-window}

Se a ação de duplo clique na barra de título do macOS for **Preencher**, faz duplo clique numa zona vazia da barra. A janela ocupa a área visível sem entrar em ecrã completo. Repete para repor o tamanho anterior.

<!-- guide-coverage: MOD-023 MOD-024 MOD-025 MOD-034 MOD-038 MOD-039 MOD-044 MOD-045 MOD-048 MOD-054 MOD-067 MOD-069 -->

## Barra inferior e janelas abertas

A barra inferior aparece com janelas de trabalho ou atalhos de regresso; a Janela dos Jogadores fica de fora. Título e ícone distinguem **Editar** e **Visualizar**: clica para trazer/restaurar a janela ou X para fechar. Fichas e editores de personagens são independentes e minimizáveis; Condições e Ataque completo não são.

Sair de um combate por concluir coloca-o em pausa e mantém um atalho **primeiro à esquerda**, com faixa colorida. Clica para regressar. O X apenas oculta o atalho: não termina nem elimina o combate. Durante esse combate fica oculto, mas as outras janelas continuam listadas.

Os chats recebidos de Hero aparecem mesmo com a janela fechada, sem te interromper; um ponto indica mensagens não lidas. Abrir e ler a conversa remove o indicador. À direita, a área Hero mantém jogadores contactados durante esta execução da app mesmo após desligarem: estado, teste, chat, download da ficha, live e desligar. Consulta o [guia Hero](hero-sync.md).
