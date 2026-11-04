# Ligar o DnDino Hero: guia do mestre

Receba as fichas dos jogadores na aventura e gira os valores de jogo a partir do Mac. A ligação é local, sem servidor externo. Consulte também o [guia do jogador Hero](../companion/dndino-sync.md).

!!! info "Disponibilidade"
    Esta página descreve também a nova comparação de dados, preparada para a próxima atualização. Exige versões do **DnDino e do DnDino Hero que a suportem**. As versões anteriores podem ter opções e comportamento inicial diferentes.

## Preparação

Abra a aventura correta. Utilizem a mesma rede local, autorizem o acesso à rede local e mantenham Wi-Fi e Bluetooth ativos, com os dispositivos próximos. Cada jogador deve selecionar a personagem correta no Hero.

A sincronização em direto exige **iOS/iPadOS 26 ou posterior** no Hero. Nos sistemas anteriores está disponível **apenas o envio manual da ficha**, mesmo fora do combate. **Ligado não significa sincronizado.**

## Primeira ligação

1. No painel **Sessão live** do painel da aventura, inicie a ligação na área **DnDino Hero**. Não precisa de iniciar uma sessão de jogo.
2. O jogador abre **Definições → Ligação DnDino**, procura o DnDino e escolhe a aventura.
3. Autorize o dispositivo depois de verificar o nome e a personagem.
4. Importe uma nova ficha ou associe uma existente. Verifique a confirmação de substituição para não substituir a ficha errada.
5. Ative a **Sincronização automática** para esse dispositivo. **Só o mestre controla a ativação**; o Hero apresenta o estado, sem um segundo interruptor a ativar.

A associação utiliza identificadores, não apenas nomes. Mudar o nome da personagem não exige outra cópia.

## Que dados conservar?

**O Hero fornece a estrutura da ficha:** níveis, características, descrições, feitiços e configuração das progressões são responsabilidade do jogador.

Com as novas versões, o Hero envia a ficha completa ao ligar ou voltar a ligar, antes das trocas em direto. Reativar a sincronização também exige alinhamento. Se os valores coincidirem, não surge comparação.

Caso sejam diferentes, a janela compara **PV atuais, máximos e temporários, CA, inspiração heroica, condições, recursos restantes e espaços de feitiço utilizados**. Escolha o valor DnDino ou Hero para cada diferença. **O Hero está pré-selecionado**. As ações globais escolhem todos os valores de uma das aplicações; confirme e aguarde o resultado.

Exemplo: conserve os 18 PV do DnDino em vez dos 24 do Hero, mas escolha as condições do Hero. As condições são escolhidas **como conjunto completo**, nunca unidas automaticamente.

Os máximos e a configuração dos recursos continuam a vir do Hero. As combinações incompatíveis são assinaladas. Só esse dispositivo fica em espera; os outros jogadores continuam. Se os dados mudarem, reveja a comparação atualizada. Tentar novamente pede dados novos. Fechar a janela ou interromper a ligação desliga o dispositivo. **Confirmar não ativa a sincronização em direto por si só.**

## Durante o jogo

O modo em direto troca valores suportados: PV atuais/máximos/temporários, CA, inspiração e condições. No combate é considerado o participante associado.

| Informação | Utilização |
| --- | --- |
| Progressões consumíveis | Restantes/Total; menos para gastar, mais para repor |
| Progressões fixas do nível atual | Cartões de consulta, sem botões de consumo |
| Espaços de feitiço | Totais e utilizados, separados por origem quando necessário |

Os contadores também são guardados no DnDino. O Hero confirma os comandos suportados do mestre. Se houver alterações simultâneas, confira o resultado antes de tentar novamente; não assuma que um clique sem confirmação foi aplicado. Novos níveis e configurações exigem uma **ficha completa**, não apenas contadores.

## Transferir ficha, conversar e barra inferior

O botão de transferência à direita do chat pede a ficha já associada sem outro envio manual do jogador. Exige Hero compatível, ligado e autorizado; está indisponível durante o alinhamento e não ativa o modo em direto.

A área Hero da barra inferior conserva os dispositivos ligados durante a abertura atual do DnDino, mesmo após perderem a ligação. Permite verificar identidade e estado, testar a ligação, abrir o chat, gerir a sincronização e desligar. O teste não importa dados. O **chat privado exige sincronização em direto ativa**; as mensagens não lidas são assinaladas na barra.

## Voltar a ligar e resolver problemas

Por predefinição, o mestre reativa a sincronização a cada nova ligação. Pode escolher o arranque automático para dispositivos autorizados nas definições; o novo alinhamento continua a ser necessário.

- **Mac não encontrado:** verifique aventura à escuta, rede partilhada, permissões de Rede local e aplicações abertas.
- **Ligado sem atualizar:** verifique autorização, associação, iOS/iPadOS 26+, alinhamento concluído e ativação pelo mestre.
- **Ligação perdida:** mantenha o Hero em primeiro plano. Ao regressar pode voltar a ligar; o botão de religação também permite tentar.
- Desligar termina a ligação atual sem eliminar a ficha importada.
- Remover a associação revoga autorização e associações nesta aventura; esquecer o dispositivo abrange todas as aventuras. As fichas importadas são conservadas.

Antes da sessão, teste uma pequena alteração de PV com cada jogador e verifique nas duas aplicações.
