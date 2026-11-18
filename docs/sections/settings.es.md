# Ajustes

La sección **Ajustes** reúne las preferencias globales de DnDino. Aquí no se trabaja sobre una aventura o un personaje concreto, sino que se define **cómo debe comportarse la aplicación en su conjunto**.

Los ajustes influyen sobre todo en:

- el aspecto general de la interfaz
- el comportamiento de la barra superior
- el flujo de `Lugares`
- el comportamiento del `Combate`
- la gestión de imágenes, copias y snapshots
- el soporte y la parte diagnóstica de la base de datos

## Contenido, ayuda y temas adicionales

**General → Contenido oficial** muestra u oculta catálogos SRD sin eliminar datos personales ni romper referencias. El control se comparte con las listas. Véase [Contenido oficial](official-content.md).

Los botones guía **?**, activos por defecto, pueden desactivarse globalmente. **Halloween** se añade a los temas; **Sistema** sigue la apariencia real de macOS. Barra superior, botones contextuales y menús tienen disposiciones coherentes para mantener legibles iconos y texto.

## Cómo está organizada la pantalla

La página se divide en dos áreas:

- una **barra lateral izquierda** con las categorías
- un **panel principal** a la derecha con las opciones de la sección seleccionada

Las categorías disponibles son:

- `General`
- `Barra superior`
- `Lugares`
- `Combate`
- `Medios`
- `Tema`
- `Base de datos`
- `Diagnóstico`
- `Soporte`
- `Licencias`

Esta estructura separa bien las preferencias de uso diario de las más técnicas, como las copias de seguridad y el diagnóstico.

## General

La sección `General` reúne las preferencias base de la aplicación.

### Perfil DM

Aquí puedes personalizar tu perfil con:

- `Nombre de usuario`
- `Género`

El nombre se reutiliza también en otras partes de la app, por ejemplo en el mensaje de bienvenida de la `Home`.

### Idioma de la interfaz

Puedes decidir si:

- seguir el idioma del sistema
- forzar un idioma concreto de la aplicación

### Mantener la pantalla encendida

En **Ajustes > General**, activa **Mantener la pantalla encendida** para evitar que la pantalla se apague automáticamente mientras DnDino está en primer plano. Resulta útil durante una sesión cuando lees notas o presentas contenido sin utilizar constantemente el ratón o el teclado.

La opción está **desactivada de forma predeterminada**. También funciona con batería, pero aumenta el consumo de energía. La selección se recuerda entre aperturas: al cambiar a otra aplicación se libera la solicitud; al volver a DnDino se restablece si la opción sigue activada. Puedes desactivarla en cualquier momento desde el mismo control.

No requiere permisos especiales y no modifica los ajustes de seguridad de macOS. No impide el bloqueo manual, el reposo solicitado por el usuario, el cierre de la tapa ni las protecciones del sistema. No garantiza impedir salvapantallas o bloqueos impuestos por políticas independientes.

Si macOS no puede activar la función, aparece un aviso: desactiva y vuelve a activar la opción para intentarlo de nuevo. El restablecimiento completo de los ajustes la desactiva.

### Confirmaciones globales

La opción `Pedir confirmación antes de eliminar` añade una confirmación antes de acciones destructivas, como eliminaciones o retiradas.

### Metadatos

Dentro de `General` también encontrarás:

- `Mostrar metadatos en la aplicación`

Esta opción decide si los paneles de metadatos deben mostrarse en las pantallas que los soportan.

### Disposición de paneles en el dashboard de aventura

Esta parte es importante si usas con frecuencia el `Dashboard de aventura`.

Puedes:

- arrastrar paneles
- reordenarlos dentro de la columna izquierda o derecha
- moverlos de una columna a otra

### Tema activo

Dentro de `General` también se muestra el **tema actualmente seleccionado** como resumen rápido. El cambio real de tema se hace en la sección `Tema`.

### Guías introductorias

Gestiona las guías en [Restablecer app y guías](#app-and-guide-reset): reabrir la introducción y reiniciar guías contextuales son comandos separados que no borran datos.

## Barra superior

La sección `Barra superior` define el comportamiento de las herramientas rápidas presentes en la parte superior de la aplicación. Para la descripción completa de cada botón, consulta la página `Barra superior`.

### Aspecto de la barra superior

Puedes elegir si la barra superior se muestra:

- solo con iconos
- o con iconos y nombre debajo

### Dado predeterminado

Aquí puedes elegir el **tipo de dado predeterminado** del lanzador de dados dentro de `Herramientas rápidas`.

### Apertura rápida de personajes

Cada resultado tiene dos botones circulares a la derecha: **Ver** abre la ficha compacta y **Editar** el editor. La fila ya no abre la ficha por sí sola y no existe una preferencia global para elegir entre ambas acciones. [Topbar](topbar.md).

### Apertura rápida de reglas

Este ajuste controla la apertura rápida de `Reglas`.

Desde aquí puedes decidir si ese acceso debe abrir:

- el editor completo
- o una ventana más compacta y orientada a la consulta

### Controles de la ventana de jugadores en la barra superior

La opción `Mostrar controles de la ventana de jugadores en la barra superior` muestra controles rápidos para abrir o cerrar manualmente la `Ventana de Jugadores`.

## Lugares

La sección `Lugares` contiene las preferencias globales utilizadas como comportamiento predeterminado en el panel de lugares.

### Rol de presencia predeterminado

Cuando añades una presencia a un lugar, DnDino puede proponer un rol inicial por defecto.

### Mostrar mapas de los lugares padre por defecto

Si activas esta opción, en la pantalla `Lugares` los mapas heredados de los lugares padre se muestran ya visibles.

### Recordar el último lugar visitado

Si está activo, al volver a la pantalla `Lugares` la aplicación intenta restaurar el último lugar seleccionado para esa aventura.

### Cerrar automáticamente el lugar anterior

Este ajuste se aplica durante una **sesión en vivo activa**.

Cuando un lugar se marca como `En visita`, el lugar que antes estaba `En visita` se marca automáticamente como `Visitado`.

## Combate

Las preferencias de presentación y visibilidad definen los **valores iniciales de los nuevos combates**. Para cambiar un combate, usa [la gestión de segunda pantalla y la visibilidad](combat.md#player-screen-options), también con acciones por grupo. No se sobrescriben las elecciones guardadas en otros combates.

La activación de la pantalla de jugadores y la apertura de ventanas siguen siendo globales. Los combates anteriores sin terminar guardan sus valores iniciales una sola vez, al abrirlos por primera vez.

### Activar pantalla de combate para los jugadores

Estos controles solo aparecen si **Activar pantalla de combate para los jugadores** está activado en **Ajustes > Combate**. Desactivarlo los oculta en la preparación y durante el combate, conservando las elecciones guardadas. No es necesario tener un segundo monitor conectado ni la ventana de jugadores ya abierta.

### Abrir la ventana de jugadores si está cerrada

Si está activo, DnDino abre automáticamente la `Ventana de Jugadores` al empezar el combate. Si está desactivado, la presentación solo se actualiza si la ventana ya está abierta.

### Abrir la ventana de jugadores incluso con un solo monitor

Esta opción aparece solo si la apertura automática está activa. Sirve para usar la `Ventana de Jugadores` aunque no tengas una segunda pantalla.

## Presentación del combate

Estas opciones definen los valores iniciales de presentación de los nuevos combates; puedes cambiarlos en cada combate sin modificar Ajustes:

- `Mostrar intro del combate a los jugadores`
- `Mostrar resumen final a los jugadores`
- `Mostrar asalto en la pantalla de jugadores`
- `Mostrar duración del encuentro en la pantalla de jugadores`
- `Mostrar siguiente turno en la pantalla de jugadores`

La duración del encuentro se muestra como un temporizador legible; si el combate está en pausa, el conteo se detiene.

## Información de héroes

Estas opciones definen la visibilidad inicial de los participantes de tipo héroe en los nuevos combates. Puedes decidir si mostrar:

- PG actuales, máximos y temporales
- condiciones activas

## Información de PNJ

Estas opciones definen la visibilidad inicial de los PNJ en los nuevos combates, también cuando su rol es Aliado. Puedes decidir por separado si mostrar:

- PG actuales, máximos y temporales
- condiciones activas
- el nombre real del PNJ

Si los nombres de PNJ están ocultos, la `Ventana de Jugadores` usa el nombre genérico `PNJ`.

## Información de monstruos

Estas opciones definen la visibilidad inicial de los monstruos en los nuevos combates. Sus PG y condiciones siguen estos ajustes incluso si son aliados; los nombres de monstruos no enemigos permanecen visibles inicialmente. Puedes decidir por separado si mostrar:

- PG actuales, máximos y temporales
- condiciones activas
- el nombre real de los enemigos

Si los nombres de monstruos/enemigos están ocultos, la `Ventana de Jugadores` usa el nombre genérico `Enemigo`.

## Medios

La sección `Medios` reúne las preferencias para la gestión de imágenes y de la ventana de presentación.

### Imágenes para jugadores a pantalla completa

Si está activa, las imágenes mostradas a los jugadores se abren en modo pantalla completa.

### Imágenes del DM en el monitor principal

Esta opción hace que la ventana del DM se abra por defecto en la primera pantalla disponible.

### Recordar tamaño de la ventana del DM

Si está activo, al volver a abrir una nueva imagen para el DM la ventana mantiene:

- el último tamaño
- la última posición

## Mantenimiento de medios

La sección `Mantenimiento de medios` cubre el lado más técnico de la gestión de imágenes.

Desde aquí puedes lanzar `Limpiar medios no utilizados`, que comprueba los archivos de imagen guardados por la aplicación y elimina aquellos que ya no están vinculados a ninguna entidad.

## Tema

La sección `Tema` permite elegir la **paleta global** de la aplicación.

Cada tema muestra una pequeña vista previa visual con sus colores principales, para que puedas entender enseguida cómo cambiará la interfaz.

## Base de datos

La sección `Base de datos` es una de las más importantes para la seguridad de los datos.

Aquí encontrarás:

- la ruta de la carpeta de datos
- la ruta de la base SQLite
- la ruta de la carpeta de copias
- información sobre los snapshots más recientes

### Copia de seguridad automática

Puedes elegir:

- la frecuencia de la copia automática
- el número máximo de snapshots automáticos que se conservarán

### Snapshots en la nube

DnDino también gestiona el comportamiento de los snapshots en la nube.

Desde aquí puedes decidir cómo deben comportarse los guardados en la nube y ver el estado actual a través del texto de resumen mostrado en pantalla.

### Acciones principales

En el panel `Base de datos` encontrarás los principales botones de mantenimiento:

- `Abrir carpeta de datos`
- `Abrir carpeta de copias`
- `Crear snapshot...`
- `Restaurar snapshot...`
- `Restaurar desde iCloud`

### Reinicio de la aplicación

La función `Restablecer datos de la aplicación` elimina:

- la base de datos de la aplicación
- los medios de la aplicación

pero conserva las copias ya creadas.

### Últimos snapshots

En la parte inferior de la sección `Base de datos`, DnDino muestra también la lista de los últimos snapshots encontrados.

Para cada uno se muestran:

- nombre del archivo
- fecha
- tamaño

## Diagnóstico

La sección `Diagnóstico` sirve para controlar el estado técnico de la base de datos SQLite utilizada por la aplicación.

Aquí puedes:

- actualizar los datos de diagnóstico
- ver la ruta de la base de datos
- comprobar si el archivo existe
- verificar su tamaño y fecha de modificación
- ver la versión de SQLite

### Tablas

El diagnóstico también muestra la lista de tablas encontradas en la base de datos junto con el número de registros presentes en cada una.

## Soporte

La sección `Soporte` reúne los canales rápidos para contactar con quien desarrolla la aplicación.

Aquí encontrarás:

- el correo de soporte
- el botón `Solicitar soporte`
- el botón `Enviar una sugerencia`
- el botón `Copiar correo`

## Licencias

La sección `Licencias` reúne las referencias legales y de atribución utilizadas por la aplicación.

Actualmente incluye en particular la parte relativa al **System Reference Document 5.2** de Dungeons & Dragons, con referencias:

- al documento SRD
- a la licencia `CC-BY-4.0`

!!! tip
    Si estás configurando DnDino por primera vez, las secciones más útiles para revisar de inmediato son `General`, `Barra superior`, `Combate` y `Base de datos`. Suelen ser las que más influyen en el uso diario y en la seguridad de los datos.
## Novedades de la versión 1.4

La sección `Base de datos` ahora es `Base de datos y medios`.

En las versiones de lanzamiento, DnDino ya no muestra rutas técnicas internas. En su lugar, la sección se centra en información útil: tamaño de la base de datos, número de imágenes guardadas, tamaño total de imágenes, instantáneas, exportación de copias de seguridad y exportación de medios.

Las instantáneas y los medios de la app pueden exportarse a una ubicación elegida por el usuario mediante el panel estándar de guardar de macOS. Los medios siguen copiados dentro de la sandbox de la app para que DnDino no pierda referencias si los archivos originales se mueven o eliminan.

La sección Diagnóstico queda reservada para builds de depuración y no se muestra en la versión de lanzamiento.

<!-- guide-coverage: MOD-042 MOD-043 MOD-049 MOD-051 MOD-060 MOD-061 MOD-062 MOD-070 MOD-071 MOD-073 MOD-077 MOD-078 MOD-079 MOD-080 MOD-086 MOD-088 MOD-145 MOD-146 MOD-147 MOD-148 MOD-163 MOD-164 MOD-168 MOD-170 -->

## Temas, fondos y opacidad

**Sistema** aparece primero y sigue macOS. Los demás temas se agrupan en **Paletas de colores**, **Especiales** y **Estaciones**. Especiales incluye **Infierno** y **Magia**; las cuatro estaciones usan paisajes fantásticos ilustrados con aventureros. Hero ofrece los mismos temas e imágenes.

Puedes desactivar el fondo decorativo o importar un **fondo personalizado**. Solo se guarda una imagen; la nueva reemplaza la anterior. Cambiar de tema desactiva el fondo personal, pero lo conserva.

El control de opacidad actualiza al instante los paneles compatibles, incluidos títulos y búsqueda de lugares, cabecera de aventura, tarjetas de héroes y sesiones. Conservan un tono más oscuro o transparencia atenuada para facilitar la lectura; textos, imágenes y controles no se vuelven transparentes. Otros paneles siguen opacos. **Predeterminado** restaura las opacidades originales y la posición correcta del control, no un 50 % común.

Cambiar de tema recrea la pantalla principal y vuelve a **Ajustes → Tema**. Las ventanas secundarias abiertas y sus borradores sin guardar permanecen intactos; la barra inferior sigue el nuevo tema. Los botones principales y la selección lateral usan los colores del tema con texto adaptado al contraste. **Sistema** conserva los controles nativos de macOS.

Consulta [Conexión con Hero](hero-sync.md) para autorizaciones, historial, inicio live automático opcional y diferencias entre desconectar, quitar asociación y olvidar.

## Notificaciones y sonido {#notification-settings}

En **Ajustes → Dispositivos Hero**, oculta el historial inferior sin desactivar los avisos. Otro interruptor, activo por defecto, controla el sonido de **nuevos mensajes y solicitudes de vinculación**. Cambios Live, conexiones/desconexiones y avisos de combate son silenciosos. Consulta [Notificaciones](topbar.md#notification-history).

## Restablecer app y guías {#app-and-guide-reset}

Estas operaciones tienen efectos distintos. Lee la explicación antes de confirmar.

- **Abrir guía inicial** reabre la introducción sin borrar datos ni reiniciar guías contextuales. La nueva introducción 2.0.0 aparece también si completaste la anterior.
- **Mostrar de nuevo las guías contextuales** reinicia las guías de cada pantalla, no la introducción. Se desplazan a áreas fuera de vista y abren las secciones necesarias.
- **Restablecer datos**, también en Base de datos y Multimedia, borra archivo y medios, conservando perfil, preferencias, guías y copias locales/iCloud.
- **Eliminar copias locales** borra copias manuales y automáticas gestionadas por DnDino, no los datos actuales ni los archivos exportados.
- **Eliminar copia iCloud** borra solo la instantánea de la app, si está disponible. Una copia futura puede recrearla si siguen activadas.
- **Restablecimiento completo**, separado al final con doble confirmación, elimina datos, medios, copias gestionadas, fondo personal, credenciales Hero, perfil, preferencias y guías, y cierra la app. Los archivos exportados quedan intactos.

Cierra la sesión live y ventanas secundarias antes de actuar sobre el archivo. Sin iCloud, debes elegir explícitamente un restablecimiento local; si falla el borrado cloud solicitado, no se borran los datos locales. Son acciones irreversibles: exporta antes lo que quieras conservar.
