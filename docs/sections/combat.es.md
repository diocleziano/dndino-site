# Combate

La sección **Combate** es el rastreador operativo de encuentros de DnDino. Está pensada para ser rápida, compacta y legible cuando la mesa está en el momento más intenso de la sesión.

El combate siempre nace desde un **lugar** y puede incluir a los héroes de la aventura, presencias locales, PNJ y monstruos vinculados a la escena.

Esta página explica:

- la preparación del precombate
- la introducción y ordenación de iniciativa
- la pantalla principal de combate
- los controles del turno
- ataques, daño, curación, estados y tiradas de salvación
- enlaces internos en ataques y habilidades
- resumen lateral, últimos eventos y deshacer
- Ventana de Jugadores
- resumen final y estadísticas

## Uno o Dos Monitores

El combate funciona bien en **un solo monitor**: toda la gestión del DJ permanece en la ventana principal, con rastreador de iniciativa, fichas compactas y resumen.

Con un segundo monitor también puedes usar la **Ventana de Jugadores**:

- en la pantalla del DJ quedan controles, fichas, objetivos, estados y estadísticas
- en la pantalla de jugadores aparece una presentación más limpia, con imágenes e información visible

!!! tip
    El segundo monitor es opcional. Sirve para separar la vista operativa del DJ de la presentación más narrativa para los jugadores.

## Ventana de Jugadores Durante el Combate

Cuando empieza el encuentro, DnDino puede abrir o actualizar la **Ventana de Jugadores**.

Si la presentación está activa, puede mostrar:

- introducción inicial con los participantes
- participante del turno actual
- animaciones de ataque
- resumen final

![Pantalla de jugadores durante el precombate](../images/en_combat_schermogiocatori_precombat.png){ .img-shot }

La superposición puede incluir:

- ronda
- PG actuales, máximos y temporales
- estados
- siguiente turno

![Pantalla de jugadores durante el turno de un héroe](../images/en_combat_schermogiocatori_turnoeroi.png){ .img-shot }
![Pantalla de jugadores durante el turno de un monstruo](../images/en_combat_schermogiocatori_turnomostri.png){ .img-shot }

Para héroes, PNJ y monstruos puedes decidir por separado en ajustes qué información se muestra a los jugadores.

## Ajustes Útiles

Las opciones principales están en **Ajustes**, en las secciones de Combate y Ventana de Jugadores.

Las más importantes son:

- `Abrir la Ventana de Jugadores también con un solo monitor`
- `Mostrar controles de la Ventana de Jugadores en la barra superior`
- `Mostrar introducción de combate a los jugadores`
- `Mostrar resumen final a los jugadores`
- `Mostrar ronda en la pantalla de jugadores`
- `Mostrar siguiente turno en la pantalla de jugadores`
- `Mostrar PG de los héroes en la pantalla de jugadores`
- `Mostrar condiciones de los héroes en la pantalla de jugadores`
- `Mostrar PG de PNJ a los jugadores`
- `Mostrar condiciones de PNJ a los jugadores`
- `Mostrar nombres de PNJ a los jugadores`
- `Mostrar PG de monstruos a los jugadores`
- `Mostrar condiciones de monstruos a los jugadores`
- `Mostrar nombres de enemigos a los jugadores`

Terminar un combate siempre pide confirmación, porque al cerrarlo se sincronizan estado y estadísticas.

## Dónde se Abre el Combate

El combate se crea desde un **lugar**. Una vez abierto, la pantalla cambia según el estado del encuentro:

- **Precombate**: preparas participantes, nombres e iniciativas.
- **Combate activo**: gestionas turnos, fichas, objetivos y resumen.
- **Combate concluido**: consultas el resumen final del DJ.

## Precombate

![Pantalla de precombate](../images/en_combat_precombat.png){ .img-hero }


El precombate sirve para preparar el encuentro antes del primer turno.

La pantalla usa tres áreas principales:

- **Héroes**
- **Monstruos y PNJ**
- **Orden final**

Arriba también ves el nombre del encuentro, el número de participantes y las acciones principales.

## Acciones del Precombate

Las acciones principales son:

- `Añadir`
- `Iniciar encuentro`
- `Init PNJ/Monstruos`, en la columna de monstruos y PNJ

`Añadir` abre el selector de participantes.

`Iniciar encuentro` comienza el combate. Si al menos un participante tiene iniciativa `0`, DnDino pide confirmación.

`Init PNJ/Monstruos` tira automáticamente la iniciativa solo para monstruos y PNJ. Los héroes están pensados para entrada manual, porque su valor suele venir de la mesa.

## Modificar Nombres e Iniciativa

En precombate puedes corregir:

- nombre mostrado del participante
- iniciativa

Esto es especialmente útil para monstruos, por ejemplo:

- Goblin 1
- Goblin 2
- Capitán goblin

La iniciativa se recoge mientras escribes, sin tener que salir del campo. Las columnas de trabajo no se reordenan continuamente mientras introduces valores: el orden definitivo se aplica al iniciar el combate.

## Orden Final

![Orden de iniciativa preparado](../images/en_combat_precombat_valorizzato.png){ .img-hero }


El panel **Orden final** muestra una vista previa siempre actualizada del orden que se usará al iniciar.

El orden se calcula así:

1. iniciativa más alta
2. en caso de empate, modificador de Destreza más alto
3. si el empate continúa, desempate aleatorio

Este panel permite revisar el resultado sin molestar la fase de entrada.

## De Dónde Vienen los Participantes

El panel de añadido puede proponer:

- `Héroes`
- `Presencias del lugar`
- `Globales`

Los héroes ya vinculados a la aventura solo pueden entrar una vez en el mismo combate.

Las presencias del lugar reutilizan su estado local si está disponible.

Los monstruos globales pueden añadirse varias veces, porque suelen representar varias copias de la misma criatura.

## Combate Activo

![Combate activo](../images/en_combat_main.png){ .img-hero }


Al iniciar el encuentro, la pantalla pasa a la gestión operativa.

Se divide en tres zonas:

- a la izquierda, el **rastreador de iniciativa**
- en el centro, las fichas compactas del **turno actual** y del **seleccionado**
- a la derecha, el **resumen** de salud, daño y eventos

El objetivo es ver la mayor cantidad de información útil posible sin abrir paneles enormes.

## Controles del Turno

Los controles principales están arriba.

A la izquierda:

- `Anterior`
- `Pausa` / `Reanudar`
- `Siguiente`
- `Deshacer evento`

A la derecha:

- `Añadir`
- `Ordenar`
- `Fin combate`

`Anterior` y `Siguiente` cambian el turno.

`Pausa` detiene el temporizador del combate. Cuando está en pausa se convierte en `Reanudar`.

`Deshacer evento` restaura uno de los últimos eventos anulables.

`Añadir` inserta más participantes incluso con el combate empezado.

`Ordenar` reconstruye el orden de iniciativa.

`Fin combate` cierra el encuentro tras confirmación.

## Rastreador de Iniciativa

La columna izquierda muestra todos los participantes de forma compacta.

Cada fila muestra:

- iniciativa
- nombre
- CA
- PG
- PG temporales
- indicador de estado, si existe
- color de rol

El color lateral ayuda a distinguir:

- héroes
- aliados
- neutrales
- enemigos

Al hacer clic en una fila:

- el participante se abre como **seleccionado**
- si ya estaba seleccionado, se cierra la columna del seleccionado

El botón de papelera elimina el participante del combate.

## Fichas del Turno y del Seleccionado

En el centro puedes ver hasta dos fichas:

- el participante del turno
- el participante seleccionado en la lista

Las fichas tienen anchura fija y desplazamiento vertical propio, para que la página se mantenga estable incluso con textos largos.

En la parte superior aparecen:

- nombre
- tipo, linaje o subtipo
- idiomas, si existen
- valor de desafío y PX, si existen
- vista previa de imagen
- botones operativos

## Campos Rápidos

En la ficha puedes modificar directamente:

- PG actuales
- PG temporales
- iniciativa

La CA se muestra como un valor compacto con icono de escudo.

Para héroes de la aventura puede aparecer también el botón de **Inspiración heroica**.

Los cambios de PG se mantienen sincronizados con la lista izquierda y el resumen derecho.

## Acciones del Participante

Cada ficha puede mostrar:

- `Atacar`
- `Daño`
- `Curar`
- `TS`
- `Estados`
- `Notas DJ`
- `Modificar`

`Atacar` abre una ventana con el atacante y la lista de objetivos.

![Ventana Atacar](../images/en_combat_attaccosemplice.png){ .img-shot }

`Daño` aplica daño directo al participante.

![Ventana Daño](../images/en_combat_danni.png){ .img-detail }

`Curar` aplica curación directa.

![Ventana Curar](../images/en_combat_cura.png){ .img-detail }

`TS` abre las tiradas de salvación disponibles.

![Ventana tirada de salvación](../images/en_combat_tirosalvezza.png){ .img-detail }

`Estados` abre una ventana dedicada a gestionar estados.

`Notas DJ` guarda apuntes sobre el participante. Las notas no forman parte de deshacer.

`Modificar` abre el editor completo del participante.

## Lista de Objetivos

Las listas de objetivos se ordenan según el atacante.

Si el atacante es un enemigo:

- primero héroes y aliados
- luego neutrales
- luego enemigos

Si el atacante es un héroe, aliado o neutral:

- primero enemigos
- luego neutrales
- luego héroes y aliados

Dentro de cada grupo, los nombres se ordenan alfabéticamente.

La línea lateral de color ayuda a reconocer el rol del objetivo.

## Ataques, Habilidades y Enlaces Internos

Las secciones principales son:

- `Estados`
- `Ataques`
- `Habilidades especiales`
- `Habilidades`
- `Conjuros`
- `Descripción`

Las secciones son plegables y usan un ligero degradado coherente con el color del título.

Los textos de ataques, habilidades especiales y habilidades pueden contener enlaces internos creados durante la creación o modificación del personaje.

Durante el combate, esos enlaces abren ventanas dedicadas para resolver la acción con más espacio.

Los enlaces más útiles son:

- `Ataque completo`
- `1d20 + MOD`
- tirada libre
- tirada de daño
- enlaces a entidades internas

## Ataque Completo

![Ventana Ataque completo](../images/en_combat_attaccocompleto.png){ .img-shot }
![Creación de enlace Ataque completo](../images/en_combat_attaccocompleto_link.png){ .img-shot }


`Ataque completo` está pensado para textos de ataque de monstruos, PNJ o héroes.

Se prepara en la pantalla de creación o modificación del personaje: seleccionas el texto del ataque y creas un enlace de tipo `Ataque completo`. Durante el combate, ese texto se convierte en una acción lista para abrir y resolver.

Cuando lo usas en combate:

- la ventana muestra el nombre del ataque
- el atacante queda indicado claramente
- puedes elegir uno o más objetivos
- puedes gestionar varias líneas de daño
- aplicas el daño seleccionado a los objetivos elegidos

Al crear el enlace, el daño es modular: con el botón `+` añades filas y solo se muestran las que tienen valores.

## Conjuros

Si el participante tiene conjuros, la ficha muestra la sección `Conjuros`.

Los conjuros se agrupan por nivel.

Para monstruos y PNJ, la fila del nivel también puede mostrar el contador de espacios usados, por ejemplo:

- `0/3`
- `2/3`
- `3/3`

El botón `Usar` en cada conjuro incrementa el contador de ese nivel.

El contador no bloquea el uso al llegar al máximo: solo sirve como recordatorio para el DJ.

Los trucos no usan espacios.

## Estados

![Ventana Estados](../images/en_combat_condizioni.png){ .img-shot }


La ventana `Estados` permite:

- añadir estados
- eliminar estados
- elegir duración
- vincular la expiración al turno de un participante
- gestionar notas relacionadas

Cuando se aplica un estado, DnDino muestra feedback visual en la pantalla y en la fila afectada.

## Héroes a 0 PG o Menos

Los héroes siguen una regla distinta a monstruos y PNJ.

Un héroe puede bajar de `0` PG.

La regla es:

- entre `0` y `-(PG máximos - 1)` está **Inconsciente**
- a `-PG máximos` o menos muere
- también muere con 3 fallos en las tiradas de salvación contra muerte

Cuando un héroe está a `0` PG o menos pero no ha muerto, la ficha muestra las **tiradas de salvación contra muerte**.

Con 3 éxitos vuelve a `1` PG.

## PNJ y Monstruos a 0 PG

Para PNJ y monstruos la regla es más simple:

- a `0` PG o menos se consideran muertos
- quedan excluidos del ciclo de turnos
- el resumen puede mostrarlos como muertos

## Resumen Lateral

La columna derecha muestra el **Resumen**.

Incluye:

- ronda
- duración
- turno actual
- salud de héroes y aliados
- salud de PNJ y monstruos
- daño infligido
- daño recibido
- últimos 5 eventos

Es una vista de control: sirve para leer la situación de un vistazo.

Los PG cambian de color:

- normal si el participante está bien
- amarillo por debajo del 50 %
- naranja por debajo del 10 %
- rojo a 0 o menos

Para héroes, los PG se tachan solo cuando el personaje ha muerto de verdad, no solo por estar bajo 0 PG.

## Últimos 5 Eventos y Deshacer

El combate conserva los últimos eventos anulables.

Deshacer puede incluir:

- ataques
- daño aplicado por ataques
- curación, si se gestiona como evento anulable
- estados aplicados o modificados

Las `Notas DJ` no se deshacen.

Deshacer también restaura las estadísticas vinculadas, para que daño infligido y recibido sigan siendo coherentes.

## Feedback Visual

Cuando ocurre algo en combate, DnDino muestra feedback inmediato:

- banner superior
- animación en la fila del participante afectado
- efecto en el botón `Aplicar`, cuando corresponde
- actualización del resumen lateral

Así queda claro que el comando se ha recibido.

## Resumen Final del Encuentro

![Resumen final del combate](../images/en_combat_postcombat.png){ .img-hero }

![Resumen final en la pantalla de jugadores](../images/en_combat_schermogiocatori_postcombat.png){ .img-shot }

Cuando confirmas el fin del combate, el encuentro deja de ser modificable.

La pantalla final muestra:

- rondas totales
- duración
- enemigos derrotados
- daño infligido
- daño recibido
- estado final de los participantes

Los PG finales y los estados se sincronizan con los registros vinculados.

## Sincronización Final

Al cerrar el combate, DnDino sincroniza los datos necesarios.

Para héroes de la aventura:

- PG actuales
- PG temporales
- estados
- estado final

Para presencias del lugar con estado local:

- PG actuales
- PG temporales
- estados
- estado final

El combate también puede alimentar los datos de la **sesión en vivo** y las estadísticas.

## Estadísticas

DnDino usa los combates concluidos para alimentar estadísticas y gráficos.

Las estadísticas pueden incluir:

- daño infligido
- daño recibido
- duración de encuentros
- número de combates
- enemigos derrotados
- evolución del daño por día
- duración media de sesiones

En el panel de la aventura está disponible **Estadísticas de Aventura**, que reúne combates completados, incluso fuera de una sesión en vivo concreta, y los agrupa de forma consultable.

El resumen de sesión en vivo puede mostrar gráficos de los combates completados durante esa sesión.

## Cuándo Rinde Mejor

El combate de DnDino funciona mejor cuando:

1. preparas bien el precombate
2. asignas iniciativas y nombres antes de empezar
3. usas el rastreador izquierdo para no perder la visión general
4. mantienes abierta la ficha del turno y, si hace falta, la del objetivo seleccionado
5. aprovechas los enlaces en ataques y habilidades
6. usas el resumen lateral para salud, daño y eventos recientes
7. terminas el combate solo cuando estás seguro, para mantener limpias estadísticas y sincronización

!!! tip
    Aunque DnDino automatiza muchas operaciones, puedes seguir tirando dados físicos. En ese caso, usa el combate sobre todo para aplicar daño, curación y estados rápidamente, sin recalcular PG y estadísticas a mano cada vez.
