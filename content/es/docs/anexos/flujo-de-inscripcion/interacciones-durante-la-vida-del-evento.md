---
title: "Creación del evento"
weight: 3
lastmod: 2019-07-05T11:33:28Z
dokuwiki: interacciones_durante_la_vida_del_evento
---
![](/media/interacciones_durante_la_vida_del_evento/interaccion_inscripcion.png?align=center)

El organizador crea el evento cumplimentando todos los datos que considere necesarios. Si el evento tiene alguna inscripción de pago, un administrador económico asignará un receptor de pago al evento.

## Publicación del evento

Cuando el organizador considera que el evento está listo lo publica. Al perder el estatus de *borrador*, el evento ya puede recibir visitas de otros usuarios y aparece en los motores de búsqueda.

## Durante el proceso de inscripción

Cuando un usuario decide inscribirse se inicia un proceso que vinculará a uno o varios usuarios, con una o varias inscripciones de un evento. Está asociación se guarda en un objeto que se denominará recibo y que tendrá un identificador único. Si el recibo es de pago, le corresponde un estado de pago que se creará como *Pendiente*. La inscripción o inscripciones de los asistentes se crearán también como *Pendientes*.

Todos estos datos se crean y almacenan en el momento en que el usuario decide confirmar la operación y (opcionalmente) se dispone a realizar el pago. Se procede de este modo para evitar errores derivados de delegar en terceras partes la gestión de los pagos. Cuando el usuario abandona la plataforma para realizar el pago, los datos ya han sido almacenados y procesados evitando cualquier pérdida de información.

Del mismo modo, al confirmar la operación se envían una serie de comunicaciones por correo electrónico:

- El comprador recibe un resguardo con los datos de su reserva
- Los asistentes reciben los detalles de sus cuentas de usuario, en caso de ser nuevos usuarios. También se les informa de la reserva de sus inscripciones
- Si el evento tiene un mensaje de bienvenida predefinido, este se les envía a los asistentes

## Pago validado

Al validar un pago el administrador económico se actualiza el estado del mismo. La asistencia pasa a estar confirmada si la validación es automática. Al producirse estas actualizaciones se envían tres comunicaciones por correo electrónico:

- Se informa al comprador de que su pago ha sido completado con éxito
- Se informa al asistente de que se ha confirmado su asistencia
- Si el evento es con validación, se informa al organizador de que hay nuevos asistentes pendientes de ser validados

## Pago rechazado

Cuando el administrador económico decide rechazar un pago, este se actualiza inmediatamente. El comprador de las inscripciones recibirá una comunicación por correo electrónico que contendrá la información necesaria para hacer las reclamaciones pertinentes en caso de que haya ocurrido un error.

Si la validación es automática, también se rechazará la asistencia.

## Cancelación de asistencia

Si el usuario decide unilateralmente cancelar su asistencia, se enviará una comunicación al organizador del evento para notificarle. La cancelación de la asistencia tendrá efecto inmediato aunque no se procesará ningún tipo de devolución, quedando esas tareas en mano de los administradores económicos.
