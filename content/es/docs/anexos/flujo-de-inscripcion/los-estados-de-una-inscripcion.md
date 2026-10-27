---
title: "Diagrama de flujo"
weight: 5
lastmod: 2019-07-05T11:34:12Z
dokuwiki: los_estados_de_una_inscripcion
---
![](/media/los_estados_de_una_inscripcion/inscripcion_estado.png?w=650)

## Caso base

Generalmente una inscripción va a situarse en estado *Pendiente* al ser creada. Después será *Confirmada* o *Rechazada* por la validación manual o la validación automática realizada por el pago.

Hay dos casos especiales que cambian este funcionamiento. Si la inscripción es gratuita y no tiene validación, por ejemplo, la inscripción pasa automáticamente a *Confirmada*. Si la inscripción es de pago y tiene validación manual, la asistencia tendrá el estado que se indique manualmente, ignorando el estado del pago.

Cabe destacar que existe una configuración adicional, y es que la inscripción puede estar *Cancelada*. Una inscripción cancelada no se tiene en cuenta para ningún cálculo, simplemente se almacena por motivos de registro. El estado cancelado no es un estado en si, si no un marcado a una inscripción. Por tanto, una inscripción puede estar pendiente y cancelada o confirmada y cancelada. Esto se produce porque el estado Cancelada lo otorga el asistente, mientras que los otros estados los otorga el organizador o la plataforma.

## Tipos de inscrito a un evento

Los inscritos **confirmados** son aquellos que han seguido una de las siguientes opciones:

- se han inscrito en un evento gratuito sin validación
- se han inscrito en un evento gratuito con validación y han sido aceptados por el organizador
- se han inscrito en un evento de pago sin validación y han realizado un pago por transferencia que ha sido aceptado por el contable
- se han inscrito en un evento de pago con validación y han sido aceptados por el organizador

Los inscritos **pendientes**  son aquellos que han seguido una de las siguientes opciones:

- se han inscrito en un evento gratuito con validación y aún no han sido validados por el organizador
- se han inscrito en un evento de pago sin validación y han realizado un pago por transferencia que aún no ha sido validado por el contable
- se han inscrito en un evento de pago con validación y aún no han sido validados por el organizador

Los inscritos **rechazados**  son aquellos que han seguido una de las siguientes opciones:

- se han inscrito en un evento gratuito con validación y su inscripción ha sido denegada por el organizador
- se han inscrito en un evento de pago sin validación y han realizado un pago por transferencia que ha sido denegado por el contable
- se han inscrito en un evento de pago con validación y su inscripción ha sido denegada por el organizador

Los inscritos **cancelados**  son aquellos que han seguido una de las siguientes opciones:

- han decido cancelar su asistencia, opción disponible desde su panel de asistente
- se han inscrito en un evento de pago con o sin validación y han realizado un pago con validación automática que ha sido denegado
