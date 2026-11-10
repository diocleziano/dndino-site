# Topbar

![Topbar](../images/en_topbar.png){ .img-hero }


A **topbar** é a área de atalhos globais do DnDino. Ela mantém por perto as ferramentas mais usadas durante a preparação ou condução de uma aventura.

Pode mostrar só ícones ou ícones com nome abaixo, conforme a preferência escolhida em **Configurações**.

## Comportamento Geral

Os botões à esquerda são atalhos globais. Alguns abrem uma seção completa, outros mostram um painel rápido para consultar algo sem sair da tela atual.

## Início

`Início` volta à página inicial do aplicativo.

Use quando quiser retornar à visão geral ou recomeçar a partir da entrada principal.

## Aventuras

`Aventuras` muda de comportamento conforme o contexto.

Na **Home** ou em seções não ligadas a uma aventura específica, abre a lista de aventuras.

Dentro de um **painel de aventura**, dos **locais** ou de um **combate** ligado a uma aventura, volta ao painel dessa aventura.

## Personagens

Cada resultado tem dois botões circulares à direita: **Visualizar** abre a ficha compacta e **Editar** abre o editor. A linha sozinha não abre mais a ficha e não há preferência global escolhendo entre as ações.

## Equipamento

`Equip.` abre a busca rápida de equipamento.

Busca em:

- armas
- armaduras
- ferramentas
- equipamento de aventura

Você pode buscar por nome, categoria, CA, dano, propriedades, uso ou descrição. Os resultados abrem em uma janela de consulta e os botões inferiores abrem as seções completas.

## Regras

`Regras` abre a busca rápida de regras.

Busca em:

- talentos
- glossário
- magias

Você pode buscar por nome, categoria, pré-requisitos, tipo de regra, escola ou descrição. As magias abrem em uma janela dedicada; talentos e glossário podem abrir em consulta ou modificação conforme as configurações.

## Ferramentas Rápidas

`Ferramentas rápidas` reúne as ferramentas que você pode precisar na hora durante a preparação ou a sessão.

Daqui você pode abrir:

- o **rolador rápido de dados**
- o **gerador de nomes**
- os **temporizadores rápidos**

### Rolador de dados

O rolador de dados permite escolher número de dados, tipo de dado e modificador.

O dado padrão é configurado em **Configurações**. O resultado mostra cada dado e o total, útil para testes rápidos e rolagens improvisadas.

### Gerador de nomes

Escolha espécie, gênero e **nome completo** ou **apenas nome**. Bloqueie nome ou sobrenome para gerar novamente só a outra parte, ou regenere uma proposta individual. Copie um resultado ou recupere-o do histórico recente, compartilhado com o acesso rápido. O histórico pode ser limpo.

### Temporizadores rápidos

Os temporizadores rápidos ajudam a controlar tempos de mesa sem sair da tela atual.

Você pode dar um nome ao temporizador, escolher a duração com um controle no estilo macOS e executar até quatro temporizadores ao mesmo tempo. Cada temporizador pode ser pausado, retomado, parado ou removido.

## Configurações

`Configurações` abre as preferências do aplicativo: idioma, tema, topbar, painéis, combate, Janela dos Jogadores, banco de dados, diagnóstico e suporte.

## Sessão ao vivo na barra inferior {#live-session-control}

Em uma página da aventura, abra **Sessão ao vivo** na **barra inferior**, à esquerda do Hero. Clique em **Iniciar** e confirme para começar uma sessão da aventura atual.

Se uma sessão já estiver aberta, o controle continua disponível fora da aventura. Não é possível iniciar uma segunda em paralelo. [Guia da sessão ao vivo](live-session.md#live-session-bottom-bar).

## Janela dos Jogadores no Centro

Se a opção estiver ativa, o centro da topbar também mostra os controles da **Janela dos Jogadores**.

Eles servem para abrir ou fechar manualmente a janela dos jogadores, útil para mostrar imagens, combates ou resumos em uma segunda tela.

## Quando Usar

Use a topbar para:

- voltar rapidamente dos locais ao painel da aventura
- buscar uma regra sem mudar de tela
- consultar um personagem ou item rapidamente
- fazer uma rolagem rápida, iniciar um temporizador ou gerar um nome improvisado
- gerenciar uma sessão live a partir da seção atual

## Preencher a janela principal {#fill-main-window}

Se a ação de clique duplo na barra de título do macOS estiver em **Preencher**, clique duas vezes em uma área vazia da barra. A janela ocupa a área visível sem entrar em tela cheia. Repita para restaurar o tamanho anterior.

<!-- guide-coverage: MOD-023 MOD-024 MOD-025 MOD-034 MOD-038 MOD-039 MOD-044 MOD-045 MOD-048 MOD-054 MOD-067 MOD-069 -->

## Barra inferior e janelas abertas

A barra inferior aparece com janelas de trabalho ou atalhos de retorno; a Janela dos Jogadores fica de fora. Título e ícone distinguem **Editar** e **Visualizar**: clique para trazer/restaurar a janela ou X para fechar. Fichas e editores de personagens são independentes e minimizáveis; Condições e Ataque completo não são.

Sair de um combate não concluído o pausa e mantém um atalho **primeiro à esquerda**, com faixa colorida. Clique para voltar. Seu X apenas esconde o atalho: não encerra nem exclui o combate. Durante esse combate ele fica oculto, mas as outras janelas continuam listadas.

Chats recebidos de Hero aparecem mesmo com a janela fechada, sem interromper você; um ponto indica mensagens não lidas. Abrir e ler a conversa remove o indicador. À direita, a área Hero mantém jogadores contatados durante esta execução do app mesmo após desconexão: estado, teste, chat, download da ficha, live e desconexão. Veja o [guia Hero](hero-sync.md).
