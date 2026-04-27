# Regras e equipamento

Esta seção reúne as áreas de consulta do app: **Regras**, **Talentos**, **Glossário**, **Magias** e **Equipamento**.

Os campos são livres, para se adaptarem à sua campanha. Ainda assim, para filtros mais precisos e agrupamentos mais claros, vale usar valores limpos e coerentes.

## Como funciona a busca

A busca rápida da topbar verifica vários campos ao mesmo tempo.

Para **regras**, busca em:

- nome
- categoria
- pré-requisitos
- tipo de regra
- escola
- descrição

Para **equipamento**, busca em:

- nome
- categoria
- CA
- dano
- propriedades
- uso
- descrição

## Talentos

Nos talentos, o campo mais útil para organizar conteúdo é **categoria**.

Exemplos:

- `Origem`
- `Geral`
- `Combate`
- `Magia`

Os **pré-requisitos** ajudam a entender rapidamente quem pode usar o talento. Mantenha-os curtos, por exemplo `Nível 4`, `Força 13+`, `Conjurador`.

## Glossário

O glossário serve para termos, condições, regras recorrentes e lembretes de mesa.

Use **tipo de regra** ou **categoria** para agrupar entradas semelhantes.

Exemplos:

- `Condição`
- `Ação`
- `Movimento`
- `Teste de resistência`

A descrição deve ser clara e direta, para continuar útil durante a sessão.

## Magias

As magias são mais estruturadas, porque também são usadas em combate quando associadas a personagens.

Para obter agrupamentos eficazes:

- para **truques**, escolha `Truque` no menu de nível
- para outras magias, escolha um nível de `1` a `9`
- em **classes**, separe os nomes por vírgulas, por exemplo `Mago, Clérigo, Druida`
- em **escola**, escreva apenas o nome da escola, por exemplo `Conjuração`

Evite valores como `Conjuração de nível 3` no campo escola: o nível já tem seu próprio campo e a escola funciona melhor quando está limpa.

### Campos úteis

Preencha com cuidado:

- **tempo de lançamento**
- **alcance**
- **componentes**
- **duração**
- **descrição**
- **níveis superiores**

Esses dados aparecem na janela de detalhe da magia e ajudam a consultá-la sem abrir livros externos.

## Magias em combate

Se você associar magias a um personagem, durante o combate elas aparecem na ficha, agrupadas por nível.

A seção também mostra informações de conjuração quando existirem, como bônus de ataque de magia, CD do teste de resistência e espaços disponíveis.

Para **NPCs e monstros**, o botão `Usar` na magia aumenta o contador de espaços usados daquele nível. É um lembrete para o Mestre: não bloqueia o lançamento, mas mostra claramente quando o máximo previsto foi atingido.

Os truques não consomem espaços.

## Equipamento

O equipamento é dividido em:

- armas
- armaduras
- ferramentas
- equipamento de aventura

Também aqui os campos são livres, mas dados coerentes tornam a busca muito mais eficaz.

## Armas

Para armas, os campos mais importantes são **categoria**, **dano** e **propriedades**.

Exemplos:

- categoria: `Simples`, `Marcial`, `À distância`
- dano: `1d8 perfurante`
- propriedades: `Versátil, Arremesso`

Se você reutilizar os mesmos nomes de propriedades, será mais fácil encontrar armas com características comuns.

## Armaduras

Para armaduras, use **categoria** e **CA** de forma organizada.

Exemplos:

- categoria: `Leve`, `Média`, `Pesada`, `Escudo`
- CA: `14 + Des máx. 2`

A descrição pode conter notas, requisitos, desvantagens ou regras especiais.

## Ferramentas e equipamento

Para ferramentas e equipamento de aventura, os campos mais úteis são **categoria**, **uso** e **descrição**.

Exemplos:

- categoria: `Ferramentas de artesão`
- uso: `Testes de Destreza ou Inteligência`
- categoria: `Equipamento de exploração`
- uso: `Viagem, masmorra, sobrevivência`

Prefira categorias curtas e reutilizáveis em vez de frases longas.

## Boas práticas

Para manter o banco de dados legível:

- use os mesmos nomes para categorias semelhantes
- separe listas de valores com vírgulas quando quiser que sejam lidas como grupos
- evite duplicar no texto informações que já têm um campo dedicado
- mantenha descrições completas, mas campos de filtro curtos e limpos
