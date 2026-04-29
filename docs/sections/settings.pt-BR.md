# Configurações

A seção **Configurações** reúne as preferências globais do DnDino. Aqui você não trabalha sobre uma aventura ou personagem específica, mas define **como o aplicativo deve se comportar como um todo**.

As configurações influenciam principalmente:

- o aspecto geral da interface
- o comportamento da barra superior
- o fluxo de `Locais`
- o comportamento do `Combate`
- a gestão de imagens, backups e snapshots
- o suporte e a parte de diagnóstico da base de dados

## Como a tela está organizada

A página é dividida em duas áreas:

- uma **barra lateral esquerda** com as categorias
- um **painel principal** à direita com as opções da seção selecionada

As categorias disponíveis são:

- `Geral`
- `Barra superior`
- `Locais`
- `Combate`
- `Mídia`
- `Tema`
- `Banco de dados`
- `Diagnóstico`
- `Suporte`
- `Licenças`

Essa estrutura separa bem as preferências de uso diário das opções mais técnicas, como backups e diagnóstico.

## Geral

A seção `Geral` reúne as preferências básicas do aplicativo.

### Perfil do DM

Aqui você pode personalizar seu perfil com:

- `Nome de usuário`
- `Gênero`

O nome também é reutilizado em outras partes do aplicativo, por exemplo na mensagem de boas-vindas da `Home`.

### Idioma da interface

Você pode decidir se quer:

- seguir o idioma do sistema
- forçar um idioma específico do aplicativo

### Confirmações globais

A opção `Pedir confirmação antes de excluir` adiciona uma confirmação antes de ações destrutivas, como remoções e exclusões.

### Metadados

Dentro de `Geral` você também encontra:

- `Mostrar metadados no aplicativo`

Essa opção decide se os painéis de metadados devem ou não ser mostrados nas telas que os suportam.

### Disposição dos painéis do dashboard da aventura

Esta parte é importante se você usa com frequência o `Dashboard da aventura`.

Você pode:

- arrastar painéis
- reordená-los dentro da coluna esquerda ou direita
- movê-los de uma coluna para a outra

### Tema ativo

Dentro de `Geral`, o **tema atualmente selecionado** também é mostrado como um resumo rápido. A troca real do tema é feita na seção `Tema`.

### Guias introdutórios

Daqui você pode restaurar o comportamento de primeiro uso do aplicativo.

O botão `Restaurar Primeiro Uso` faz com que o DnDino volte a considerar como não vistos os guias contextuais e os percursos introdutórios.

## Barra superior

A seção `Barra superior` define o comportamento das ferramentas rápidas presentes na barra superior do aplicativo. Para a descrição completa de cada botão, consulte a página `Topbar`.

### Aparência da barra superior

Você pode escolher se quer ver a barra superior:

- apenas com ícones
- ou com ícones e nome por baixo

### Dado padrão

Aqui você pode escolher o **tipo de dado padrão** do rolador rápido.

### Abertura rápida de personagens

Esta configuração controla o comportamento da abertura rápida de personagens.

Você pode decidir se o atalho deve abrir:

- uma visualização mais orientada para leitura
- ou um modo mais próximo da edição

### Abertura rápida de regras

Esta configuração controla a abertura rápida de `Regras`.

Daqui você pode decidir se esse atalho deve abrir:

- o editor completo
- ou uma janela mais compacta e orientada para consulta

### Controles da janela dos jogadores na barra superior

A opção `Mostrar controles da janela dos jogadores na barra superior` mostra controles rápidos para abrir ou fechar manualmente a `Janela dos Jogadores`.

## Locais

A seção `Locais` contém as preferências globais usadas como comportamento padrão no dashboard dos locais.

### Papel de presença padrão

Quando você adiciona uma presença a um local, o DnDino pode propor um papel inicial padrão.

### Mostrar mapas dos locais pai por padrão

Se você ativar essa opção, na tela `Locais` os mapas herdados dos locais pai já aparecem visíveis.

### Lembrar o último local visitado

Se estiver ativo, ao voltar para a tela `Locais`, o aplicativo tenta restaurar o último local selecionado para aquela aventura.

### Fechar automaticamente o local anterior

Esta configuração se aplica durante uma **sessão ao vivo ativa**.

Quando um local é marcado como `Em visita`, o local que antes estava `Em visita` é automaticamente marcado como `Visitado`.

## Combate

A seção `Combate` reúne as preferências globais do sistema de combate.

Aqui você encontra opções de apresentação e preferências que influenciam a `Janela dos Jogadores`.

### Habilitar tela de combate para os jogadores

Este é o controle principal. Se estiver desativado, o DnDino não usa a janela dos jogadores para mostrar intro, turno atual, round ou resumo final do combate, e as opções relacionadas ficam ocultas.

### Abrir a janela dos jogadores se estiver fechada

Se estiver ativo, o DnDino abre automaticamente a `Janela dos Jogadores` quando o combate começa. Se estiver desativado, a apresentação só é atualizada se a janela já estiver aberta.

### Abrir a janela dos jogadores mesmo com um único monitor

Esta opção aparece apenas se a abertura automática estiver ativa. Use quando quiser usar a `Janela dos Jogadores` mesmo sem uma segunda tela.

## Apresentação do combate

Esta subseção controla as informações gerais mostradas aos jogadores durante o confronto:

- `Mostrar intro do combate aos jogadores`
- `Mostrar resumo final aos jogadores`
- `Mostrar round na tela dos jogadores`
- `Mostrar duração do encontro na tela dos jogadores`
- `Mostrar próximo turno na tela dos jogadores`

A duração do encontro é mostrada como um temporizador legível; se o combate estiver em pausa, a contagem para.

## Informações dos heróis

Estas opções valem quando o participante ativo é um herói ou aliado. Um NPC ou monstro marcado como `Aliado` também usa essas configurações. Você pode decidir se mostra:

- PV atuais, máximos e temporários
- condições ativas

## Informações dos NPCs

Estas opções valem apenas quando o participante ativo é um NPC não aliado. NPCs marcados como `Aliado` usam as configurações de heróis/aliados. Você pode decidir separadamente se mostra:

- PV atuais, máximos e temporários
- condições ativas
- o nome real do NPC

Se os nomes dos NPCs estiverem ocultos, a `Janela dos Jogadores` usa o nome genérico `NPC`.

## Informações dos monstros

Estas opções valem apenas quando o participante ativo é um monstro não aliado. Monstros marcados como `Aliado` usam as configurações de heróis/aliados. Você pode decidir separadamente se mostra:

- PV atuais, máximos e temporários
- condições ativas
- o nome real dos inimigos

Se os nomes dos monstros/inimigos estiverem ocultos, a `Janela dos Jogadores` usa o nome genérico `Inimigo`.

## Mídia

A seção `Mídia` reúne as preferências para a gestão de imagens e da janela de apresentação.

### Imagens dos jogadores em ecrã inteiro

Se estiver ativa, as imagens mostradas aos jogadores são abertas em modo fullscreen.

### Imagens do DM no monitor principal

Esta opção faz com que a janela do DM seja aberta por padrão no primeiro ecrã disponível.

### Lembrar tamanho da janela do DM

Se estiver ativa, quando você reabre uma nova imagem para o DM, a janela mantém:

- o último tamanho
- a última posição

## Manutenção de mídia

A seção `Manutenção de mídia` cobre o lado mais técnico da gestão de imagens.

A partir daqui você pode lançar `Limpar mídia não utilizada`, que verifica os ficheiros de imagem guardados pela aplicação e remove aqueles que já não estão ligados a nenhuma entidade.

## Tema

A seção `Tema` permite escolher a **paleta global** do aplicativo.

Cada tema mostra uma pequena pré-visualização com as cores principais, para que você perceba logo como o aspeto geral da interface vai mudar.

## Banco de dados

A seção `Banco de dados` é uma das mais importantes para a segurança dos dados.

Aqui você encontra:

- o caminho da pasta de dados
- o caminho da base SQLite
- o caminho da pasta de backups
- informações sobre os snapshots mais recentes

### Backup automático

Você pode escolher:

- a frequência do backup automático
- o número máximo de snapshots automáticos a manter

### Snapshots na nuvem

O DnDino também gere o comportamento dos snapshots na nuvem.

Daqui você pode escolher como os guardados na nuvem se devem comportar e ver o estado atual através do texto de resumo apresentado na tela.

### Ações principais

No painel `Banco de dados` você encontra os principais botões de manutenção:

- `Abrir pasta de dados`
- `Abrir pasta de backups`
- `Criar snapshot...`
- `Restaurar snapshot...`
- `Restaurar a partir do iCloud`

### Redefinição do aplicativo

A função `Redefinir dados do aplicativo` apaga:

- a base de dados do aplicativo
- a mídia do aplicativo

mas mantém os backups já criados.

### Últimos snapshots

Na parte inferior da seção `Banco de dados`, o DnDino também mostra a lista dos últimos snapshots encontrados.

Para cada um são mostrados:

- nome do ficheiro
- data
- tamanho

## Diagnóstico

A seção `Diagnóstico` serve para controlar o estado técnico da base de dados SQLite usada pela aplicação.

Aqui você pode:

- atualizar os dados de diagnóstico
- ver o caminho da base de dados
- confirmar se o ficheiro existe
- verificar tamanho e data de modificação
- ver a versão do SQLite

### Tabelas

O diagnóstico também mostra a lista das tabelas encontradas na base de dados, juntamente com o número de registos presentes em cada uma.

## Suporte

A seção `Suporte` reúne os canais rápidos para contactar quem desenvolve o aplicativo.

Aqui você encontra:

- o email de suporte
- o botão `Pedir suporte`
- o botão `Enviar uma sugestão`
- o botão `Copiar email`

## Licenças

A seção `Licenças` reúne as referências legais e de atribuição usadas pelo aplicativo.

Atualmente inclui, em especial, a parte relativa ao **System Reference Document 5.2** de Dungeons & Dragons, com referências:

- ao documento SRD
- à licença `CC-BY-4.0`

!!! tip
    Se você está configurando o DnDino pela primeira vez, as seções mais úteis para verificar logo são `Geral`, `Barra superior`, `Combate` e `Banco de dados`. Normalmente são as que mais influenciam o uso diário e a segurança dos dados.
