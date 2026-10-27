---
title: "Servidor de correo electrónico"
weight: 4
lastmod: 2024-11-22T09:56:14Z
dokuwiki: email_server
---
- [Servidor de correo nativo de SYMPOSIUM](/docs/administracion/configuracion/email-server#servidor-de-correo-nativo-de-symposium)
- [Servidor de correo propio](/docs/administracion/configuracion/email-server#configuracion-de-un-servidor-propio)
- [Servicio de Google](/docs/administracion/configuracion/email-server#configurar-una-cuenta-de-google)

## Servidor de correo nativo de SYMPOSIUM

En este caso, la plataforma envía correos usando como FROM: una cuenta y dominio de SYMPOSIUM, normalmente mailing@symposium.events. Usamos Amazon SES para enviarlo y usa el SPF y DKIM del dominio symposium.events. Los mensajes salen con el la cuenta de contacto de la plataforma en el reply-to. No es necesario, en este caso de uso, que se realice ninguna configuración adicional.

## Configuración de un servidor propio

A criterio del Administrador, es posible configurar la plataforma para que envíe los mensajes a través del servidor de correo propio de la institución. En este caso, la plataforma se conecta al servicio SMTP que se especifique. Se usa como FROM: la cuenta de correo que la institución especifica y los mensajes llegan a destino enviados por el partner desde su infraestructura.

En este caso, la institución tiene también el control para activar el SPF y DKIM de su servicio de SMTP propio que no depende de SYMPOSIUM y es muy conveniente porque evitará que los mensajes salientes sean marcados como spam. Para ello, el equipo de tecnología debe añadir un include al registro SPF:

include:_spf.symposium.events

**Nota:**  Antes de abordar la configuración del servidor de correo electrónico, consulta con tu equipo técnico. Los datos necesarios para hacerlo son de una alta especificidad técnica y es posible que necesites la asistencia del responsable del área correspondiente.

Si decides dejar de usar el servidor nativo de SYMPOSIUM para usar el de tu institución, deberás entonces activar el check "¿Usar configuración personalizada?".

### 1. Configura tu servidor (información para el equipo de Sistemas)

- Añade un regla a tu firewall que permita llegar al puerto 25 de tu servidor (o al que corresponda) a la IP 63.32.121.65

### 2. Configura la plataforma (como administrador de tu plataforma de eventos)

Tendrán que configurarse los campos que se requieren en el formulario:

- **Host:**  que será la ip o el dominio del servidor que realizará el envío.
- **Seguridad:**  permite seleccionar entre estándar, SSL o TLS.
- **Puerto:**  que fijará el puerto de la conexión, generalmente 25 y 465 según la seguridad seleccionada sea estándar o SSL respectivamente.
- **¿Requiere autenticación?:**  en caso afirmativo, tendrás que marcar la casilla e introducir usuario y contraseña.

![](/media/email_server/email_server.png?w=745&align=center)

Una vez guardados los cambios, Symposium enviará todas las comunicaciones de correo electrónico a través de ese canal.

## Configurar una cuenta de Google

Si tu proveedor de correo es Google a través de sus servicios empresariales, consulta esta guía para configurar la cuenta que ejercerá de relé de correo.

[https://support.google.com/a/answer/176600?hl=es](https://support.google.com/a/answer/176600?hl=es)
