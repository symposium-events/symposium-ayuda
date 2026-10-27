---
title: "Integration configuration"
weight: 7
lastmod: 2023-10-24T10:56:57Z
dokuwiki: configuracion_integracion
---
From the **Administration** > **Configuration** > **Integration configuration** panel, you can configure:

## Custom Integration Configuration

Section intended for future evaluations of the platform. You can contact Support for more information.

## Webhooks Configuration

Lets you enable sending real-time notifications about events in webhook format, so that you can then make the corresponding calls to the SYMPOSIUM API.

For this integration to work, we provide a token that acts as a shared secret between SYMPOSIUM and the partner's applications. Note that if the existing token is regenerated, the partner must reconfigure its services with the new token.

You can create subscriptions to the following webhooks:

| Event type | Description |
|---|---|
| registration.created | Notifications about new registrations. |
| registration.cancelled | Notifications about cancelled registrations. |
| registration.additional_purchase | Notifications about additional purchases in registrations. |
| donation.created | Notifications about new donations. |
| donation.cancelled | Notifications about cancelled donations. |
| registration.updated | Notifications about changes to registrations. |
| payment.confirmed | Notifications about confirmed payments. |
| payment.rejected | Notifications about rejected payments. |

You can also configure the different endpoints, production and testing, to which the notifications of interest are sent:

![](/media/archivos_asistentes/webhooks1.png?w=500)

Finally, the **Subscription to the event** check box enables or disables the individual subscription, provided that the feature is enabled at global level.
