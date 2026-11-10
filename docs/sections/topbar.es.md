# Barra Superior

![Barra superior](../images/en_topbar.png){ .img-hero }


La **barra superior** es la zona de accesos rápidos globales de DnDino. Mantiene a mano las herramientas que más se usan al preparar o dirigir una aventura.

Puede mostrarse solo con iconos o con icono y nombre debajo, según la preferencia elegida en **Ajustes**.

## Comportamiento General

Los botones de la izquierda son accesos rápidos globales. Algunos abren una sección completa y otros muestran un panel rápido para consultar algo sin abandonar la pantalla actual.

## Inicio

`Inicio` vuelve a la página inicial de la aplicación.

Úsalo para regresar a la vista general o empezar de nuevo desde la entrada principal.

## Aventuras

`Aventuras` cambia de comportamiento según el contexto.

Desde el **Inicio** o desde secciones no vinculadas a una aventura concreta, abre la lista de aventuras.

Desde una **dashboard de aventura**, los **lugares** o un **combate** ligado a una aventura, vuelve a la dashboard de esa aventura.

## Personajes

Cada resultado tiene dos botones circulares a la derecha: **Ver** abre la ficha compacta y **Editar** el editor. La fila ya no abre la ficha por sí sola y no existe una preferencia global para elegir entre ambas acciones.

## Equipo

`Equipo` abre la búsqueda rápida de equipamiento.

Busca en:

- armas
- armaduras
- herramientas
- equipo de aventura

Puedes buscar por nombre, categoría, CA, daño, propiedades, uso o descripción. Los resultados se abren en una ventana de consulta y los botones inferiores abren las secciones completas.

## Reglas

`Reglas` abre la búsqueda rápida de reglas.

Busca en:

- dotes
- glosario
- conjuros

Puedes buscar por nombre, categoría, prerrequisitos, tipo de regla, escuela o descripción. Los conjuros se abren en una ventana dedicada; dotes y glosario pueden abrirse en consulta o modificación según los ajustes.

## Herramientas Rápidas

`Herramientas rápidas` reúne las herramientas que puedes necesitar de inmediato durante la preparación o la sesión.

Desde aquí puedes abrir:

- el **lanzador rápido de dados**
- el **generador de nombres**
- los **temporizadores rápidos**

### Lanzador de dados

El lanzador de dados permite elegir número de dados, tipo de dado y modificador.

El dado predeterminado se configura en **Ajustes**. El resultado muestra cada dado y el total, útil para pruebas rápidas y tiradas improvisadas.

### Generador de nombres

Elige especie, género y **nombre completo** o **solo nombre**. Bloquea nombre o apellido para regenerar únicamente la otra parte, o regenera una propuesta concreta. Copia un resultado o recupéralo del historial reciente, compartido con el acceso rápido. El historial se puede vaciar.

### Temporizadores rápidos

Los temporizadores rápidos sirven para controlar tiempos de mesa sin salir de la pantalla actual.

Puedes darles un nombre, elegir la duración con un control de estilo macOS y ejecutar hasta cuatro temporizadores a la vez. Cada temporizador puede pausarse, reanudarse, detenerse o eliminarse.

## Ajustes

`Ajustes` abre las preferencias de la app: idioma, tema, barra superior, paneles, combate, Ventana de Jugadores, base de datos, diagnóstico y soporte.

## Sesión en directo en la barra inferior {#live-session-control}

En una página de la aventura, abre **Sesión en vivo** en la **barra inferior**, a la izquierda de Hero. Pulsa **Iniciar** y confirma para empezar una sesión de la aventura actual.

Si hay una sesión abierta, el control sigue disponible fuera de la aventura. No se puede iniciar una segunda sesión a la vez. [Guía de la sesión en directo](live-session.md#live-session-bottom-bar).

## Ventana de Jugadores en el Centro

Si la opción está activa, el centro de la barra superior también muestra los controles de la **Ventana de Jugadores**.

Sirven para abrir o cerrar manualmente la ventana para jugadores, útil para mostrar imágenes, combates o resúmenes en una segunda pantalla.

## Cuándo Usarla

Usa la barra superior para:

- volver rápido desde lugares a la dashboard de aventura
- buscar una regla sin cambiar de pantalla
- consultar un personaje u objeto al vuelo
- hacer una tirada rápida, iniciar un temporizador o generar un nombre improvisado
- gestionar una sesión en vivo desde la sección actual

## Rellenar la ventana principal {#fill-main-window}

Si la acción de doble clic en la barra de título de macOS es **Rellenar**, haz doble clic en una zona vacía de la barra. La ventana ocupa el área visible sin pasar a pantalla completa. Repite para restaurar el tamaño anterior.

<!-- guide-coverage: MOD-023 MOD-024 MOD-025 MOD-034 MOD-038 MOD-039 MOD-044 MOD-045 MOD-048 MOD-054 MOD-067 MOD-069 -->

## Barra inferior y ventanas abiertas

La barra inferior aparece cuando hay ventanas de trabajo o enlaces de retorno; excluye la Ventana de Jugadores. Título e icono distinguen **Editar** y **Ver**: pulsa para traer/restaurar la ventana o X para cerrarla. Las fichas y editores de personajes son independientes y minimizables; Condiciones y Ataque completo no lo son.

Salir de un combate sin terminar lo pausa y deja un enlace **primero a la izquierda**, con una franja de color. Pulsa para volver. Su X solo oculta el enlace: no termina ni elimina el combate. Se oculta durante ese combate, pero las otras ventanas siguen visibles.

Los chats recibidos de Hero aparecen aunque la ventana esté cerrada, sin interrumpirte; un punto indica mensajes sin leer. Abrir y leer la conversación quita el indicador. A la derecha, el área Hero conserva los jugadores contactados durante esta apertura de la app incluso tras desconectarse: estado, prueba, chat, descarga de ficha, live y desconexión. Consulta la [guía Hero](hero-sync.md).
