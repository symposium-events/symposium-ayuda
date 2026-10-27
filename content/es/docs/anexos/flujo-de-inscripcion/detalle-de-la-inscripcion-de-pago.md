---
title: "Diagrama de flujo"
weight: 4
lastmod: 2019-07-05T11:33:53Z
dokuwiki: detalle_de_la_inscripcion_de_pago
---
![](/media/detalle_de_la_inscripcion_de_pago/usuario_inscripcion_pago.png?align=center)

## Descripción del proceso interno

A medida que el usuario va cumplimentando su inscripción la plataforma va construyendo un objeto que almacena toda la información. Una vez el usuario llega al paso final y confirma la inscripción ese objeto se guarda en base de datos.

Tanto si la inscripción es gratuita como de pago se crea un recibo. Un recibo engloba asistentes, inscripciones y productos relacionadas. Si alguno de los elementos tiene un coste, el recibo se relaciona con un estado de pago.

En las inscripciones con coste, el recibo se almacena tan pronto como el usuario decide que va a pagar. En ese instante, todo se guarda en base de datos y se marca como pendiente de pago. De esta forma, se evita la pérdida de información en caso de que ocurra algún error en la plataforma de pagos de terceros. Cuando se confirma la transacción se actualiza el estado del pago pertinente y se refleja en la plataforma.
