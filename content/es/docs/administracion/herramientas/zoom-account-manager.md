---
title: "Gestión de la licencia propia de ZOOM"
weight: 92
lastmod: 2022-02-17T13:48:58Z
dokuwiki: zoom_account_manager
---
## Visión general del módulo de cuentas propias de Zoom

El módulo de cuentas propias Zoom permite a la institución usar su propia cuenta de Zoom integrada en la plataforma de gestión y en el flujo de los eventos. Puedes ofrecer salas de Webinar con gestión automatizada de las reservas y también disponer de salas con control manual.

- Los organizadores de eventos recibirán credenciales únicas para ocupar las salas.
- Los asistentes inscritos a los eventos recibirán enlace para participar.
- Al terminar cada Webinar, la plataforma generará automáticamente el informe de asistencia.

A continuación, exponemos los pasos a seguir para que actives tu propia cuenta de Zoom en tu plataforma. Consulta en detalle el resto de funcionalidades de este módulo en [este artículo](/docs/administracion/herramientas/zoom-account-manager-extended)

## Requisitos previos para vincular una cuenta Zoom

- Licencia Symposium para el Módulo de salas propias de Zoom Webinars.
- En tu cuenta de Zoom debes configurar, al menos, una subcuenta que disponga de licencia de Zoom Webinars.
- Cerrar sesión en el portal de Zoom con el navegador que estás usando, si usaste alguna otra cuenta.

## Paso 1: Instalación de la app Symposium

**IMPORTANTE: antes de realizar este proceso, cierra sesión de tu cuenta Zoom en tu navegador.**

Ya vinculada la cuenta, en la plataforma ya verás un listado con las subcuentas de Zoom asociadas a la cuenta maestra. En adelante, denominaremos **Salas de webinar**  a estas subcuentas.

![](/media/image_1.png?w=799&align=center)

### ¿Qué puede ir mal?

- Si al vincular la cuenta, Zoom no te pide que hagas login, seguramente sea porque ya tenías iniciada la sesión. Si la cuenta en la que estabas trabajando con Zoom es la misma que quieres vincular con Symposium, todo estará bien. Si tenías abierta sesión en otra cuenta distinta, debes revisar todas las integraciones que tengas con esa cuenta en otras aplicaciones y saltar al paso Desinstalar la app Symposium.

## Paso 2: activar las Salas de Webinar en Symposium

El listado muestra todas las salas disponibles en la cuenta maestra de Zoom. Para que la plataforma de eventos pueda hacer gestión de reservas con una sala, es necesario que la actives. Por tanto, puedes activarlas todas o sólo las que consideres.

![gestionar_enlace_con_cuenta.jpg](/media/admin/gestionar_enlace_con_cuenta.jpg?w=600&align=center)

### ¿Qué puede ir mal?

- Si no encuentras ninguna sala en el listado, es posible que tengas que revisar tu cuenta Zoom. Symposium muestra en el listado las subcuentas, que se convertirán en salas disponibles. La cuenta principal nunca se usa por motivos de seguridad. Es necesario que tengas al menos una subcuenta con licencia Zoom Webinars en tu cuenta Zoom.
- Si acabas de dar de alta nuevas subcuentas en el portal de Zoom y no aparecen en este listado, recarga la página. Si aún así siguen sin salir, haz clic en **Vincular cuenta de nuevo**.

## Paso 3: configuración del modo de asignación

Las salas pueden funcionar en dos modos, manual y automático. Indica para cada sala en qué modo quieres que funcione.

- Las salas **automáticas**se autorizarán a los solicitantes de inmediato, siempre que estén libres en el horario que se pida.
- Las salas **manuales**sólo las puede autorizar un administrador de plataforma a un solicitante. Puedes **desactivar**salas, siempre que no tengan algún Webinar asignado.

## Paso 4: Configuración avanzada

Este paso es opcional. Te permite establecer límites a los organizadores que soliciten el uso de salas de Webinar. Si no indicas límites concretos, se aplicarán los límites genéricos de Symposium.

- **Máximo**y**Mínimo número de días de antelación**  para reservar salas de Webinar
- **Duración máxima**  y **Mínima**que tendrán las salas (en minutos)
- **Tiempo de preparación**  para que los organizadores y panelistas hagan pruebas de vídeo y audio antes de que los participantes puedan entrar.
- **Tiempo de cortesía**  que se añade a la duración total del Webinar para ultimar las conclusiones de la sesión.

## Cómo desinstalar la app Symposium

Es posible que en algún momento, quieras desactivar tu cuenta Zoom en tu plataforma. Esto supone que no podrás usar tu cuenta Zoom en los eventos y que las salas que ya estuvieran reservadas no llegarán a iniciarse nunca. Dejarás de tener acceso a los informes de uso y de asistentes de las salas que se celebraron en el pasado.

### Paso 1: Desvincular la cuenta

Entra en el Panel Administración > Webinars > Gestionar cuenta Zoom. En el bloque Gestionar enlace con cuenta Zoom, haz clic en el botón **Desvincular cuenta**.

### Paso 2: Confirma que quieres desvincular la cuenta

Symposium te preguntará dos veces si prestas conformidad para desvincular la cuenta. Recuerda que al hacerlo, Symposium dejará de tener acceso a tu cuenta Zoom y tendrá que borrar todas las salas programadas a futuro, cerrará bruscamente las salas que estuviesen en curso y eliminará la información sobre las salas ya celebradas.

### Paso 3: en el portal de Zoom, desinstala la app

1. Symposium te llevará al portal de Zoom Marketplace. Haz login con tu cuenta y busca en el menú de la izquierda "Installed apps".
1. En el listado de aplicaciones instaladas, localiza Symposium Events. - Haz clic en el botón Uninstall.
1. Confirma la desinstalación. Zoom te preguntará el motivo de hacerlo y, opcionalmente, si quieres dejar los datos en Symposium.
1. Si no marcas el check para dejar los datos en tu plataforma Symposium, se nos avisará para borrarlo todo y lo haremos
1. Si marcas el check para permitir que los datos sigan en tu plataforma Symposium, guardaremos los informes de asistencia.
1. Al regresar a Symposum, comprueba que ya no tienes acceso al listado de salas Zoom.

![](/media/image_3.png?w=600&align=center)

**IMPORTANTE**: Si vuelves a Vincular la misma cuenta de Zoom en el futuro, seguirás sin tener acceso a los datos de Webinars pasados. Esto se debe a que Zoom nos proporciona un identificador de cuenta diferente del que nos dio en la anterior vinculación. Por ello, aun revinculado la misma cuenta, no aparecerán nunca los datos de Webinars pasados.
