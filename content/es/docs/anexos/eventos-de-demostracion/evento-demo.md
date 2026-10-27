---
title: "Crear, testear y eliminar Evento"
weight: 1
lastmod: 2019-07-05T11:36:23Z
dokuwiki: evento_demo
---
Es habitual querer dar de alta Eventos con el propósito de probar la plataforma. Una vez que estás preparado para empezar a añadir Eventos reales, probablemente quieras deshacerte de los de prueba, para que no aparezcan en ningún listado ni en las búsquedas.

En este artículo te explicamos cómo usar un Evento a modo de demostración sin dejar un rastro visible para los usuarios posteriormente.

## Crear el Evento

Si tienes permiso para crear Eventos, el botón aparecerá tanto en tu *Panel Organizador* como en tu *Panel Asistente*.

![](/media/evento_demo/add_event.png?align=center)

Nada más crearlo, el Evento se configura en modo *borrador*. Esto quiere decir que aún no será visible públicamente en los listados y búsquedas de la plataforma.

### Permitir asistentes al Evento

Desde el menú de edición del Evento se pueden configurar múltiples opciones. Una de las opciones más comunes es iniciar una gestión de asistentes. Puedes encontrar estas herramientas de gestión en el menú **Asistentes** > **Inscripciones**, que encuentras en la columna de la izquierda.

Para que los usuarios se puedan inscribir en el Evento debes crear un tipo de registro que lo permita. Hay cuatro tipos de registro en la lista desplegable:

- **Sin registro**: declara el Evento de libre asistencia y sin control por parte de la organización;
- **Registro en otra página web**: elige esta opción si el registro en el Evento se hace en alguna otra página web que no gestionas con Symposium;
- **Gratuito**: permite que haya un control de asistencia sin necesidad de gestión económica;
- **De pago**: es el tipo de inscripción más complejo y que implica que los asistentes tendrán que pagar una entrada al Evento. A partir de esta selección, Symposium te proporcionará numerosas herramientas para el control económico y de los asistentes.

![](/media/evento_demo/registration_method.png?align=center)

**ATENCIÓN: Si cambias el tipo de registro en un Evento ya creado, todos los datos de los inscritos se borrarán.**

Las Inscripciones son las entradas para el Evento. Puedes crear varios tipos de Inscripción, según necesites y pueden tener precio o ser gratuitas.

Una vez elegido el tipo de registro, localiza más abajo la caja **Inscripciones**. Debes crear al menos una Inscripción. Puedes crearlas según necesites y con las características que estimes. Por ejemplo, básicas, VIP, para adultos, para niños… Cada una de ellas tendrá un nombre, un precio y una divisa si el tipo de inscripción que escogiste antes es de pago, un número de entradas disponibles para ese tipo y si estará visible para los visitantes o no. Puedes crear entradas que no estén publicadas, es decir que los visitantes de la web no puedan adquirir, sino que las gestionarás personalmente a modo de invitaciones.

![](/media/evento_demo/add_registration.png?align=center)

### Se requieren métodos de pago

Si observas que no puedes escoger un **Método de pago**, debes comprobar si ya los hay disponibles en tu plataforma. Crearlos es una tarea del Administrador del sitio web. Si tienes asignado ese rol, podrás acceder a ese panel, que describimos a continuación. Si no, por favor consulta con el Administrador.

Asumiendo que tienes permisos de administración, navega al **Panel de Administración**  en el pie de página. Una vez aquí, configura las opciones Métodos de pago y Receptores de pagos, acorde a las necesidades de tu plataforma.

![](/media/evento_demo/admin_panel_payments.png?align=center)

Ahora dirígete al **Panel de gestión económica**, cuyo enlace encontrarás a pie de página también. Selecciona la opción Asignar receptor de pago.

![](/media/evento_demo/accounting_panel.png?align=center)

Busca tu Evento y añade los receptores de pago que necesites.

![](/media/evento_demo/assign_payment_receiver.png?align=center)

Vuelve al menú de edición del Evento, desde el **Panel Organizador**  y configura tantos apartados como necesites. Puedes añadir Productos relacionados con las inscripciones o un formulario para que rellenen los asistentes durante el proceso de inscripción entre muchas otras opciones.

Una vez satisfecho con la configuración del Evento, no olvides publicarlo para que sea visible al público y los usuarios se puedan inscribir.

![](/media/evento_demo/publish_event.png?align=center)

Ten en cuenta que pueden pasar hasta 30 minutos desde que publicas tu Evento hasta que aparece en los listados y búsquedas. Esto se debe a que la plataforma usa un motor de indexado para agilizar el procesamiento de miles de Eventos y usuarios.

## Testear el Evento

Ahora puedes navegar a la página principal de tu Evento, e inscribirte, adquiriendo así un rol de *asistente*  a la vez que el que ya posees de *organizador*. Esto puede ser un poco confuso, así que si dispones de otra cuenta de correo es recomendable usarla para probar el Evento como inscrito, a fin de ser lo más fiel posible a la realidad.

![](/media/evento_demo/register_attendee.png?align=center)

Cuando hayas inscrito a un usuario, puedes ir al menú **Asistentes > Listado**  y podrás ver los datos de la inscripción de este nuevo asistente.

![](/media/evento_demo/attendees_list.png?align=center)

Si ahora navegas al **Panel de gestión económica**  y localizas el Evento en el menú Gestionar pagos de un Evento, podrás ver, aceptar y rechazar los pagos relacionados con el Evento.

![](/media/evento_demo/manage_payments.png?align=center)

## Eliminar el Evento

Cuando ya no necesites hacer más pruebas, puedes borrar el Evento. Puedes hacerlo en **Panel organizador**. Si intentas eliminar un Evento que ya tiene asistentes que han pagado una entrada, verás una aviso que explica que por ese motivo no puedes hacerlo.

![](/media/evento_demo/cannot_delete_event_new.png?align=center)

Esto ocurre porque el Evento tiene pagos válidos y es un mecanismo de seguridad indispensable para mantener la coherencia de los datos en un aspecto tan sensible como los pagos.

Para poder eliminar un Evento que tiene pagos validados, primero tendrás que cancelar todos ellos en el **Panel de gestión económica**, en la sección Gestionar pagos de un Evento. Busca tu Evento, expande el listado de pagos, y rechaza el pago en todas las pruebas que hayas hecho.

![](/media/evento_demo/cancel_payment.png?align=center)

Una vez se hayan anulado los pagos, sí podrás borrar el Evento.
