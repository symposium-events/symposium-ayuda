---
title: "Configuración de Integración"
weight: 7
lastmod: 2023-10-24T10:56:57Z
dokuwiki: configuracion_integracion
---
Desde el panel de **Administración**> **Configuración**> **Configuración de Integración**, es posible configurar:

## Configuración de Integración Personalizada

Sección pensada para evaluaciones futuras de la plataforma. Puedes ponerte en contacto con Soporte para obtener más información.

## Configuración de Webhooks

Permite activar el envío de notificaciones de los eventos en tiempo real y en formato webhook para, posteriormente, hacer llamadas al API de SYMPOSIUM que corresponda.

Para que esta integración funcione, facilitamos un token que hará de secreto compartido entre SYMPOSIUM y las aplicaciones del partner. Es importante recalcar que si se regenera el token existente, el partner deberá reconfigurar sus servicios con el nuevo token.

Se pueden crear suscripciones a los siguientes webhooks:

| Tipo de evento | Descripción |
|---|---|
| registration.created | Notificaciones sobre inscripciones nuevas. |
| registration.cancelled | Notificaciones sobre inscripciones canceladas. |
| registration.additional_purchase | Notificaciones sobre compras adicionales en inscripciones. |
| donation.created | Notificaciones sobre donaciones nuevas. |
| donation.cancelled | Notificaciones sobre donaciones canceladas. |
| registration.updated | Notificaciones sobre modificaciones en inscripciones. |
| payment.confirmed | Notificaciones sobre pagos confirmados. |
| payment.rejected | Notificaciones sobre pagos rechazados. |

Además, es posible configurar los distintos endpoints, de producción y de pruebas, a los que enviar notificaciones que resulten de interés:

![](/media/archivos_asistentes/webhooks1.png?w=500)

Finalmente, el check de **Suscripción al Evento** activa o desactiva la suscripción individual, siempre que esté activa la funcionalidad a nivel global.
