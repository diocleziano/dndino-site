# Conectar DnDino Hero: guía para el DM

Recibe las fichas de los jugadores en tu aventura y gestiona los valores de juego desde el Mac. La conexión es local, sin servidor externo. Consulta también la [guía para jugadores de Hero](../companion/dndino-sync.md).

!!! info "Disponibilidad"
    Esta página también describe el nuevo cotejo de datos, preparado para la próxima actualización. Requiere versiones de **DnDino y DnDino Hero que lo admitan ambas**. Las anteriores pueden tener otras opciones y un comportamiento inicial distinto.

## Preparación

Abre la aventura correcta. Usad la misma red local, permitid el acceso a la red local y mantened Wi-Fi y Bluetooth activos, con los dispositivos cerca. Cada jugador debe seleccionar el personaje correcto en Hero.

La sincronización en directo requiere **iOS/iPadOS 26 o posterior** en Hero. En sistemas anteriores solo se permite **enviar la ficha manualmente**, incluso fuera del combate. **Conectado no significa sincronizado.**

## Primera conexión

1. En el panel **Sesión en vivo** del tablero de la aventura, inicia la conexión en el área **DnDino Hero**. No necesitas iniciar una sesión de juego.
2. El jugador abre **Ajustes → Conexión DnDino**, busca DnDino y elige tu aventura.
3. Autoriza el dispositivo tras comprobar su nombre y personaje.
4. Importa una ficha nueva o vincula una existente. Revisa la confirmación de sustitución para no sobrescribir la equivocada.
5. Activa **Sincronización automática** para ese dispositivo. **Solo el DM controla la activación**; Hero muestra el estado sin otro interruptor que deba activar el jugador.

La asociación usa identificadores, no solo nombres. Renombrar el personaje no exige crear otra copia.

## Qué datos conservar

**Hero proporciona la estructura de la ficha:** el jugador gestiona niveles, características, descripciones, conjuros y configuración de progresiones.

Con las nuevas versiones, Hero envía una ficha completa al conectar o reconectar, antes de los intercambios en directo. Reactivar la sincronización también requiere alineación. Si los valores coinciden, no aparece comparación.

Si difieren, la ventana compara **PG actuales, máximos y temporales, CA, inspiración heroica, condiciones, recursos restantes y espacios de conjuro utilizados**. Elige conservar el valor DnDino o Hero en cada diferencia. **Hero está preseleccionado**. Las acciones globales toman todos los valores de una de las dos aplicaciones; confirma y espera el resultado.

Ejemplo: conserva los 18 PG de DnDino en lugar de los 24 de Hero, pero elige las condiciones de Hero. Las condiciones se eligen **como conjunto completo**, nunca se fusionan automáticamente.

Los máximos y la configuración de recursos siguen viniendo de Hero. Se avisa de combinaciones incompatibles. Solo ese dispositivo queda en espera; los demás jugadores continúan. Si cambian datos, revisa la comparación actualizada. Reintentar solicita datos nuevos. Cerrar la ventana o interrumpir la conexión desconecta el dispositivo. **Confirmar no activa por sí solo la sincronización en directo.**

## Durante la partida

El directo intercambia los valores compatibles: PG actuales/máximos/temporales, CA, inspiración y condiciones. En combate se tiene en cuenta al participante vinculado.

| Información | Uso |
| --- | --- |
| Progresiones consumibles | Restantes/Total; menos para gastar, más para restaurar |
| Progresiones fijas del nivel actual | Tarjetas consultables, sin controles de consumo |
| Espacios de conjuro | Totales y utilizados, por origen cuando hay varias fuentes |

Los contadores se guardan también en DnDino. Hero confirma los comandos compatibles del DM. Si hay cambios simultáneos, lee el resultado antes de reintentar; no des por aplicado un clic sin confirmar. Los nuevos niveles y configuraciones requieren una **ficha completa**, no solo contadores.

## Descargar, chatear y barra inferior

El botón de descarga a la derecha del chat solicita la ficha ya vinculada sin otro envío manual del jugador. Requiere Hero compatible, conectado y autorizado; no está disponible durante la alineación y no activa el directo.

El área Hero de la barra inferior conserva los dispositivos conectados durante la apertura actual de DnDino, aunque se desconecten. Permite revisar identidad y estado, probar la conexión, abrir el chat, gestionar el directo y desconectar. La prueba no importa datos. El **chat privado requiere el directo activo**; los mensajes no leídos se señalan en la barra.

## Reconexión y problemas frecuentes

Por defecto, el DM debe reactivar el directo en cada nueva conexión. Puede elegir el inicio automático para dispositivos autorizados en los ajustes; la nueva alineación sigue siendo necesaria.

- **No aparece el Mac:** revisa aventura en escucha, red compartida, permisos de Red local y ambas aplicaciones abiertas.
- **Conectado sin actualizar:** comprueba autorización, asociación, iOS/iPadOS 26+, alineación completada e interruptor del DM.
- **Conexión perdida:** mantén Hero en primer plano. Al volver puede reconectarse; también puedes usar Reconectar.
- Desconectar termina la conexión actual sin borrar la ficha importada.
- Eliminar la asociación revoca autorización y asociaciones en esta aventura; olvidar el dispositivo afecta a todas las aventuras. Las fichas importadas se conservan.

Antes de jugar, prueba un pequeño cambio de PG con cada jugador y compruébalo en las dos aplicaciones.
