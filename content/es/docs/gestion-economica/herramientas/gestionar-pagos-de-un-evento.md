---
title: "Gestionar pagos de un evento"
weight: 2
lastmod: 2020-04-08T16:42:02Z
dokuwiki: gestionar_pagos_de_un_evento
---
La herramienta de gestión de pagos de un evento permite controlar todos los pagos recibidos en un evento determinado. Solo un Administrador económico o Administrador de la plataforma pueden tener acceso a este menú desde el Panel de Gestión económica.

![](/media/admin/pagos_de_un_evento.png?w=250&align=center)

Para gestionar un pago, en primer lugar localiza por el ID o por título el evento que quieres consultar, y a continuación haz click en el botón "Buscar".![](/media/admin/pagos_de_un_evento_2.png?w=750&align=center)

Obtendrás un listado completo de todos los pagos recibidos en el evento, indicando los siguientes datos en una primera vista:

- **Comprador:**  Email del comprador e indicación del número de inscripciones asociadas. El proceso de inscripción permite realizar inscripciones múltiples que se abonan en un solo pago en el mismo proceso.
- **Estado**. Los iconos de estado indican si está pendiente, aceptado, cancelado (el Administrador económico puede cancelar un pago) o rechazado (para el caso de pagos electrónicos rechazados de forma automática por el banco.
- **Fecha**. Fecha de inscripción.
- **Número de recibo**. Número único de identificación de recibo. El asistente dispone de dicho número y le sirve para indicarlo ante posibles incidencias.
- **Cantidad**. Importe total de la inscripción que puede variar en función de si se han realizado una o varias inscripciones en el proceso
- **Observaciones**  del asistente. Los inscritos al evento pueden dejar anotaciones al momento de solicitar factura. Esas anotaciones se convierten en llamadas de atención para el Gestor económico con forma de un triángulo amarillo a la derecha de cada pago. Estas observaciones están inicialmente Pendientes de atención. Por cada una, el Gestor económico la puede marcar como Ya atendida, o bien volver a dejarla como Pendiente de atención.

Para obtener más detalles sobre el pago y realizar acciones, haz click en el icono para desplegar la información de la operación.

## Reenviar recibo

Es posible volver a enviar el recibo del pago al correo del comprador. Alternativamente, puedes indicar otro correo al que reenviar el recibo.

## Reenviar factura

Si el comprador ha solicitado factura, puedes reenviarla a su correo electrónico o bien, indicar otro para que la reciba.

## Descargar factura

Como Administrador económico, puedes descargar las facturas de los pagos recibidos.

## Añadir observaciones a la factura

El Gestor económico puede añadir texto adicional a la factura en forma de campo Observaciones. Este contenido se imprimirá en la parte inferior del documento.

## Verificar o rechazar el pago

En el caso de transferencias bancarias, el Administrador económico revisaría los listados bancarios de ingresos, en el concepto de dichos listados debe encontrar el código de transacción (ya que así se indica que se haga en el proceso de inscripción) y debe compararlo con el que aparece en el detalle de la inscripción.

Una vez se ha verificado un pago es posible cancelarlo (por error, devolución, etc). En ese caso el sistema permite indicar la razón. El sistema puede configurarse para solicitar una contraseña en estos casos (rechazo de un pago que está confirmado) para intentar minimizar el riesgo de errores contables

![202004_gestionar_pagos.jpg](/media/gestionar_pagos_de_un_evento/202004_gestionar_pagos.jpg?w=836&align=center)

### Exportar a fichero Excel

![](/media/admin/pagos_excel.png?w=750&align=center)

Es posible exportar los pagos de un determinado evento a fichero Excel utilizando el botón disponible a la derecha del título del evento.
