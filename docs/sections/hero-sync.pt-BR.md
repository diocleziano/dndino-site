# Conectar o DnDino Hero: guia do mestre

Receba as fichas dos jogadores na aventura e gerencie valores de jogo pelo Mac. A conexão é local, sem servidor externo. Consulte também o [guia do jogador Hero](../companion/dndino-sync.md).

!!! info "Disponibilidade"
    Esta página também descreve a nova comparação de dados, preparada para a próxima atualização. Ela exige versões do **DnDino e do DnDino Hero que ofereçam esse suporte**. Versões anteriores podem ter outras opções e comportamento inicial.

## Preparação

Abra a aventura correta. Usem a mesma rede local, permitam o acesso à rede local e mantenham Wi-Fi e Bluetooth ativos, com os dispositivos próximos. Cada jogador deve selecionar o personagem correto no Hero.

A sincronização ao vivo exige **iOS/iPadOS 26 ou posterior** no Hero. Sistemas anteriores permitem **apenas o envio manual da ficha**, mesmo fora do combate. **Conectado não significa sincronizado.**

## Primeira conexão

1. No painel **Sessão ao vivo** do painel da aventura, inicie a conexão na área **DnDino Hero**. Não é necessário iniciar uma sessão de jogo.
2. O jogador abre **Ajustes → Conexão DnDino**, procura o DnDino e escolhe a aventura.
3. Autorize o dispositivo após conferir nome e personagem.
4. Importe uma ficha nova ou associe uma existente. Confira a confirmação de substituição para não sobrescrever a ficha errada.
5. Ative a **Sincronização automática** para esse dispositivo. **Somente o mestre controla a ativação**; o Hero mostra o estado, sem outro botão que o jogador precise ativar.

A associação usa identificadores, não apenas nomes. Renomear o personagem não exige criar outra cópia.

## Quais dados conservar?

**O Hero fornece a estrutura da ficha:** níveis, atributos, descrições, magias e configuração das progressões são responsabilidade do jogador.

Com as novas versões, o Hero envia a ficha completa ao conectar ou reconectar, antes das trocas ao vivo. Reativar a sincronização também exige alinhamento. Se os valores coincidirem, a comparação não aparece.

Caso sejam diferentes, a janela compara **PV atuais, máximos e temporários, CA, inspiração heroica, condições, recursos restantes e espaços de magia utilizados**. Escolha o valor do DnDino ou do Hero para cada diferença. **O Hero vem pré-selecionado**. As ações globais escolhem todos os valores de um dos aplicativos; confirme e aguarde o resultado.

Exemplo: conserve os 18 PV do DnDino em vez dos 24 do Hero, mas escolha as condições do Hero. As condições são escolhidas **como conjunto completo**, nunca unidas automaticamente.

Os máximos e a configuração dos recursos continuam vindo do Hero. Combinações incompatíveis são avisadas. Apenas esse dispositivo fica em espera; os outros jogadores continuam. Se os dados mudarem, revise a comparação atualizada. Tentar novamente solicita dados novos. Fechar a janela ou interromper a conexão desconecta o dispositivo. **Confirmar não ativa a sincronização ao vivo por si só.**

## Durante o jogo

O modo ao vivo troca valores compatíveis: PV atuais/máximos/temporários, CA, inspiração e condições. No combate, o participante associado é considerado.

| Informação | Uso |
| --- | --- |
| Progressões consumíveis | Restantes/Total; menos para gastar, mais para restaurar |
| Progressões fixas do nível atual | Cartões de consulta, sem controles de consumo |
| Espaços de magia | Totais e utilizados, separados por origem quando necessário |

Os contadores também são salvos no DnDino. O Hero confirma os comandos compatíveis do mestre. Se houver mudanças simultâneas, confira o resultado antes de tentar novamente; não presuma que um clique sem confirmação foi aplicado. Novos níveis e configurações exigem uma **ficha completa**, não apenas contadores.

## Baixar ficha, chat e barra inferior

O botão de download à direita do chat solicita a ficha já associada sem outro envio manual do jogador. Exige Hero compatível, conectado e autorizado; fica indisponível durante o alinhamento e não ativa o modo ao vivo.

A área Hero da barra inferior mantém os dispositivos conectados durante a abertura atual do DnDino, mesmo após desconexão. Permite conferir identidade e estado, testar a conexão, abrir o chat, controlar a sincronização e desconectar. O teste não importa dados. O **chat privado exige sincronização ao vivo ativa**; mensagens não lidas são sinalizadas na barra.

## Reconexão e problemas comuns

Por padrão, o mestre deve reativar a sincronização a cada nova conexão. Pode escolher início automático para dispositivos autorizados nos ajustes; o novo alinhamento continua necessário.

- **Mac não encontrado:** confira aventura recebendo conexões, rede, permissões de Rede local e aplicativos abertos.
- **Conectado sem atualizar:** confira autorização, associação, iOS/iPadOS 26+, alinhamento concluído e ativação pelo mestre.
- **Conexão perdida:** mantenha o Hero em primeiro plano. Ao voltar, ele pode reconectar; o botão Reconectar também permite tentar.
- Desconectar encerra a conexão atual sem apagar a ficha importada.
- Remover a associação revoga autorização e associações nesta aventura; esquecer o dispositivo afeta todas as aventuras. As fichas importadas são mantidas.

Antes da sessão, teste uma pequena mudança de PV com cada jogador e confira nos dois aplicativos.
