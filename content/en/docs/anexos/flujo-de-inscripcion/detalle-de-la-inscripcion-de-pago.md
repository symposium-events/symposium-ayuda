---
title: "Flow diagram"
weight: 4
lastmod: 2019-07-05T11:33:53Z
dokuwiki: detalle_de_la_inscripcion_de_pago
---
![](/media/detalle_de_la_inscripcion_de_pago/usuario_inscripcion_pago.png?align=center)

## Description of the internal process

As the user fills in their registration, the platform builds an object that stores all the information. Once the user reaches the final step and confirms the registration, that object is saved to the database.

Whether the registration is free or paid, a receipt is created. A receipt groups together the related attendees, registrations and products. If any of the items has a cost, the receipt is linked to a payment status.

For registrations with a cost, the receipt is stored as soon as the user decides to pay. At that moment everything is saved to the database and marked as pending payment. This prevents information from being lost if an error occurs on the third-party payment platform. When the transaction is confirmed, the status of the relevant payment is updated and reflected on the platform.
