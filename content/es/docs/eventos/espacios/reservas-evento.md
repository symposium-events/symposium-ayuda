---
title: "Reservas"
weight: 1
lastmod: 2026-06-12T09:49:55Z
dokuwiki: reservas_evento
---
El menú **Reservas** permite a los organizadores solicitar espacios y recursos para sus eventos y consultar las reservas que tengan en marcha.

![](/media/menureservas_1.png?w=300&align=center)

### Crear una reserva

Es necesario completar la siguiente información:

![](/media/crearunareserva.png?w=500&align=center)

- **Selecciona un ítem del programa**: es opcional. Este campo sólo aparecerá si existe contenido en la sección Programa del evento. Si la hay, al seleccionarla se copian sus datos a la reserva.
- **Contenido y tema**: se puede escribir manualmente. En caso de que se haya seleccionado una actividad del Programa, se rellena automáticamente.
- **Fecha y hora de inicio**: permite edición manual. Al igual que Contenido y tema, si se ha seleccionado una actividad del Programa se rellena automáticamente.
- **Fecha y hora de fin**: permite edición manual y, como la de inicio, puede copiarse automáticamente desde una actividad del Programa.
- **Ubicación**: selector de sede o edificio donde se celebrará la actividad.
- **Espacios**: sala o espacio disponible dentro de la ubicación seleccionada. Es importante saber que mostrará únicamente los espacios que estén disponibles para las fechas y horarios indicados.

La reserva podrá incluir los recursos asociados al espacio, como sillas, material técnico o equipamiento adicional, siempre sujetos a disponibilidad. Es una mecánica similar a la de un carro de compra. Por ejemplo:

![](/media/recursos.png?w=500&align=center)

Una vez completada la información, pulsa el botón Reservar para enviar la solicitud. No es posible reservar espacios o recursos que ya estén bloqueados por otras solicitudes en el mismo tramo horario.

### Estados de las reservas

Las reservas pueden encontrarse en los siguientes estados:

- **Pendiente**: la solicitud está pendiente de validación y tiene una reserva de los recursos. Por tanto, tiene prioridad sobre cualquier nueva solicitud que pueda entrar.
- **Aceptada**: la reserva ha sido aprobada por los administradores.
- **Rechazada**: la solicitud no ha sido aprobada por los administradores y los espacios y recursos se liberan de inmediato para nuevas solicitudes.

Desde esta pantalla es posible filtrar las reservas según su estado y consultar rápidamente la información de cada solicitud.

Resulta necesario tener en cuenta que los cambios de estado son gestionados exclusivamente por los usuarios con rol de administradores de plataforma desde el menú **Reservas**.

## Modificar o eliminar reservas

Desde el listado de reservas también es posible gestionar **solicitudes pendientes y aceptadas**:

- **Modificar**  una reserva para actualizar el campo **Contenido y tema**  o los **Recursos asociados**. Si es necesario cambiar las fechas u horarios de la reserva, será necesario eliminar la solicitud y crear una nueva.

Cuando se modifica una reserva ya aceptada, el sistema genera automáticamente una nueva solicitud en estado pendiente vinculada a la reserva original:

![](/media/modificaroeliminarreservas.png?w=500&align=center)

Una vez que los administradores aprueben la modificación, la reserva original desaparecerá y se sustituirá por la nueva versión.

- **Eliminar**  una reserva para cancelar la solicitud.

Es posible crear tantas reservas como sean necesarias, siempre que exista disponibilidad de espacios y recursos.
