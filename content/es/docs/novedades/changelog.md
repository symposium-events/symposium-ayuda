---
title: "Novedades de la plataforma"
linkTitle: "Historial de versiones"
weight: 1
lastmod: 2016-04-26T14:05:24Z
dokuwiki: changelog
---
=

## Novedades

=

## Versión 2016.03.10

### 10 de marzo de 2016

- Añadida la posibilidad de cerrar un evento
- Actualizada la versión de ReCaptcha para soportar más dispositivos

## Versión 2015.11.15

### 15 de noviembre de 2015

- Añadido soporte para TPVs Santander ELAVON
- Añadida funcionalidad para crear diplomas y acreditaciones
- Añadida una vista compacta para los productos
- Añadida nueva encriptación a los TPVs REDSYS/SERMEPA

## Versión 2015.09.15

### 15 de septiembre de 2015

- Añadido soporte para utilizar el [login SIR de RedIris](https://www.rediris.es/sir/). Es posible probarlo desde el entorno de [Eventos CRUE](http://eventos.crue.org/login.html).
- Actualizada y completada la traducción al portugués de la herramienta.

## Versión 2015.07.15

### 15 de julio de 2015

- Añadida API de consulta de eventos. Para más información contacte con [symposium@emagister.com](mailto:mailto:symposium@emagister.com).

## Versión 2015.06.07

### 07 de junio de 2015

- Añadido soporte para navegación bajo seguridad SSL (navegación HTTPS)

Para poder utilizarla en la plataforma, necesitamos que genere un certificado adecuado para el subdominio de la plataforma de eventos. Para más información contacte con [symposium@emagister.com](mailto:mailto:symposium@emagister.com).

- Añadida la posibilidad de recaudar dinero en los eventos mediante [crowdfunding](/docs/eventos/asistentes/inscripcion#donaciones).

## Versión 2015.05.26

### 26 de mayo de 2015

- Nuevas opciones de idioma disponibles (Herramientas > Activar modo multi idioma) :
      - Modificar el idioma por defecto de un evento
      - Sólo mostrar en el menú de idioma los idiomas que tienen traducción (se utiliza la descripción del evento para determinar si un idioma tiene traducción)
      - Ocultar determinados idiomas en el menú del evento

## Versión 2015.04.21

### 21 de abril de 2015

- Ahora es posible crear una nueva edición de un evento a partir de uno ya existente. [Podéis leer la ayuda aquí.](/docs/eventos/creando-y-editando-un-evento/duplicar-evento)

## Versión 2015.04.15

### 15 de abril de 2015

- Es posible registrar en un evento a un grupo de usuarios utilizando un fichero CSV. [Podéis leer la ayuda aquí.](/docs/eventos/asistentes/batch-registration)

## Versión 2015.03.24

### 24 de marzo de 2015

- Los nuevos usuarios y los inscritos a eventos tienen ahora nombre y apellidos separados en dos campos de la base de datos.
- Es posible registrar a múltiples usuarios con una sola cuenta de correo electrónico. Esta cuenta gestionará esas inscripciones como si fuesen propias o podrá transferirlas a otro usuario.
- Añadido el tipo de evento Otros, que permite indicar un tipo de evento personalizado.
- Añadido soporte para TPVs [CECA](https://comercios.ceca.es).

## Versión 2015.01.27

### 27 de enero de 2015

- Cambio check de seguridad IP en validación de cookies, afectaba a usuarios detrás de un proxy balanceado o con cambio rápido de IP.
- Metatag para forzar la última versión de Internet Explorer, no será compatible con IE 8 y anteriores.

### 15 de enero de 2015

- Cambio enlaces SEO Emagister

## Versión 2014.11.10

### 10 de noviembre de 2014

- Añadido soporte de cifrado TLS para servidores de correo electrónico
- Añadida la posibilidad de marcar algunas respuestas del formulario de inscripción como públicas para que sean visibles en el listado de asistentes. Cuando sea así, el formulario indicará con un mensaje donde corresponda que la respuesta será pública y el asistente podrá ocultar dicha información si lo desea marcando su asistencia como privada.
- Añadido remitente al cuerpo de un correo de contacto con un evento para solucionar problemas ocasionados por la incompatibilidad de algunos servidores y clientes de correo electrónico con el campo reply-to
- Mejorada la respuesta visual del formulario de edición de productos
- Añadido "Curso" como tipo de evento
- Corrección de errores y otras mejoras

## Versión 2014.10.10

### 10 de octubre de 2014

- Aviso al editar el formulario de inscripción en caso de que algún asistente haya respondido ya para evitar la pérdida de información
- Nueva funcionalidad para permitir añadir código HTML directamente a la plantilla del evento, otorgando versatilidad a organizadores de eventos con conocimientos de hojas de estilos y javascript
- En la edición del evento, al buscar asistentes en el listado se puede filtrar por las respuestas dadas en el formulario de inscripción

## Versión 2014.10.06

### 6 de octubre de 2014

- Mejorada la interfaz de usuario en el listado de asistentes para ofrecer una mayor claridad
- Mejorado el editor de texto rico para permitir, además de imágenes, la adición de otros tipos de ficheros como documentos

## Versión 2014.09.23

### 23 de septiembre de 2014

- Añadido soporte para distintos husos horarios, tanto el que corresponde al partner como a cada uno de los eventos según su lugar de celebración
- Mayor detalle en la visualización de las fechas de las transacciones aceptadas desde el panel de gestión económica
- Mejor interacción de usuario durante el proceso de envío de abstracts y papers
- Añadida la posibilidad de enlazar a cualquiera parte de la plataforma en un idioma prefijado
- Mayor robustez del sistema mediante la corrección de pequeñas incidencias

## Versión 2014.07.28

### 28 de julio de 2014

- Mejora de la interacción de usuario al rechazar pagos en el panel de gestión económica
- Cambio automático del estado de las posibles inscripciones si el organizador desactiva la validación
- Agenda: mejora de los estilos e implementación del buscador por texto y mediante calendario
- Notificación opcional al organizador de nueva inscripción, independientemente del tipo de validación
- Añadido multi-idioma a la sección de ficheros del evento
- Mejorado el listado de eventos próximos de la página principal para mostrar durante todo el día los eventos actuales
- Mejora en el panel de gestión económica que permite retener una parte como penalización cuando se rechaza un pago
- Mejora en el proceso de inscripción a un evento que permite, durante los 48 horas siguientes, cambiar la forma de pago a un usuario que eligió pagar mediante transferencia bancaria
- Mejorados los estilos de la versión móvil de la página principal
- Corrección de bugs

## Versión 2014.06.11

### 11 de junio de 2014

- Exportación a Excel en distintos formatos
- Mejora de textos y traducciones
- Menú fijo superior en algunas secciones de la administración, a modo de índice (prueba piloto)
- Al editar un elemento en las distintas secciones de la edición del evento, ahora la pantalla se encuadra en el formulario recién abierto
- Diversas mejoras de estabilidad de la plataforma

## Versión 2014.04.29

### 29 de abril de 2014

- Integración con la Agenda de la universidad Rovira i Virgili:
- Widget mostrando eventos de agenda en la página principal
- [Nueva sección](/docs/administracion/configuracion/rss-faculties) con un listado editable de facultades
- Múltiples hilos RSS, atendiendo a facultad y tipo de evento
- Vistas exclusivas para los eventos de la agenda
- Adaptación de los estilos corporativos de [www.urv.cat](http://www.urv.cat) para la [plataforma de eventos](http://events.urv.cat) de la universidad Rovira i Virgili
- Diversas mejoras en la interacción de usuario
- El editor de texto rico que se usa en distintas secciones del menú de edición del evento ahora puede verse a pantalla completa. Además, la versión básico ahora incluye la opción de pegar texto.
- Se ha mejorado el mensaje de aviso antes de borrar elementos del formulario de inscripción
- El entorno de búsqueda de eventos en el panel de gestión económica es más amigable
- Los campos de edición de fecha que incluyen minutos ahora permiten seleccionar intervalos de 5 minutos
- Se ha añadido un enlace para facilitar la respuesta en varios correos que informan sobre eventos
- Corrección de errores
- Implementación de un tema reponsivo en el entorno de demostración
- Se ha actualizado la página de captación de Emagister
- Adaptación de los estilos corporativos de [campusmarenostrum.es](http://campusmarenostrum.es) para la [plataforma de eventos](http://eventos.campusmarenostrum.es) de Campus Mare Nostrum
- Los gestores económicos ahora pueden pertenecer a tantos grupos como sea necesario **NOTA:**  hemos añadido una [página de documentación](/docs/anexos/eventos-de-demostracion/evento-demo) explicando cómo usar la plataforma para realizar pruebas con eventos.

## Versión 2014.01.29

### 29 de enero de 2014

- Añadida nueva [plantilla de sistema](/docs/eventos/diseno/plantillas) para los eventos: compact extended.
- Añadida [nueva sección](/docs/eventos/contenido/organizadores) que permite mostrar los organizadores de un evento.
- Añadida una columna más al fichero Excel de las estadísticas del panel de gestión económica.
- Visualización de un enlace que ayuda que muestra la sección de la Wiki correspondiente.
- Notificación visual en la configuración del servidor de correo que informa sobre la conectividad del servidor y puerto configurados.

## Versión 2014.01.13

### 13 de enero de 2014

- Añadida nueva opción para importar a Excel las estadísticas del panel de gestión económica.
- Arreglo de bugs del sistema.

## Versión 2013.12.17

### 17 de diciembre de 2013

- Mejor interacción de usuario al editar receptores de pago.
- Añadida opción de búsqueda en la gestión de comunicaciones recibidas.
- Mayor claridad en los listados de asistentes, Excel y vista impresión.
- Mayor flexibilidad en la edición del menú del evento: ahora se pueden crear nuevos submenús y anidar en ellos elementos de menú, arrastrando y soltando.
- Mejor terminología en todo el proceso de gestión de comunicaciones del evento.
- Añadida nueva opción para Universitat Rovira i Virgili con la que pueden mostrar los miembros del equipo organizador de un evento en la página del mismo.

## Versión 2013.11.4

### 4 de noviembre de 2013

- Para los partners que lo soliciten, las notificaciones dirigidas al organizador del evento se envían a todos los miembres del comité organizador del evento.
- Antes de cambiar el tipo de inscripción se solicita confirmación detallando los datos que se perderán.
- Generación dinámica de kits de plantillas de sistema para que nunca queden obsoletos.

## Versión 2013.10.29

### 29 de octubre de 2013

- Se puede personalizar el asunto de los correos que se envían relacionados con un evento.
- Diversos arreglos de bugs del sistema.

## Versión 2013.10.21

### 21 de octubre de 2013

- Añadido enlace de privacidad en el pie para cumplir con la directiva europea sobre el uso de cookies.
- El listado de resúmenes aceptados (abstracts) en la página del evento ahora se muestra paginado.
- Se permite modificar la categoria a la que pertence una comunicación recibida, ya sea un abstract o un paper.
- Añadida opción de exportación a Excel de resúmenes (abstracts) y comunicaciones (papers).
- Diversos arreglos de bugs del sistema.

## Versión 2013.10.3

### 3 de octubre de 2013

- Mejorado el resumen del evento para mostrar más datos de asistencias, entradas y productos.
- Añadido al proceso de inscripción la vinculación de los productos con los asistentes.
- Añadido un sistema para mostrar ayuda por secciones, gestionado por los administradores.
- Añadido el resumen de los eventos en el panel de gestión económica.
- Aplicado orden alfabético en los listados de productos.
- Migración de la plataforma a servidores más potentes.
- Diversos arreglos de bugs del sistema.

## Versión 2013.9.2

### 2 de septiembre de 2013

- Mejorado el tiempo de respuesta general de la plataforma.
- Actualizados todos los mapas para utilizar la versión más reciente de Google Maps.

## Versión 2013.8.5

### 5 de agosto de 2013

- En la generación del fichero Excel de inscritos a un evento ahora se puede filtrar por asistencia cancelada.
- En el listado de eventos de portada ahora aparece el título del evento internacionalizado si éste tiene multi idioma activo.
- En el fichero Excel de gestión de pagos ahora se repiten los valores comunes con el objetivo de falicitar la tarea de hacer filtros y ordenaciones.
- Nuevo [formulario de envío de notificaciones generales](/docs/administracion/herramientas/push-general) por parte de los administradores de la plataforma a todos los usuarios de la aplicación móvil de asistentes.
- La universidad de La Laguna ahora permite acceso a la plataforma mediante CAS, para sus miembros.
- Mejorado el tiempo de respuesta de la página pública del evento.
- Diversos arreglos de bugs del sistema.

## Versión 2013.7.8

### 8 de julio de 2013

- Nuevo sistema de gestión integral de comunicaciones: configurar la [recepción de comunicaciones](/docs/eventos/doc-cientifica/recepcion-comunicaciones) y ver las [comunicaciones recibidas](/docs/eventos/doc-cientifica/comunicaciones-recibidas).
- Nueva distribución de datos en la importación de pagos a Excel.
- Ordenados receptores de pago por unidad administrativa.
- Ordenados alfabéticamente los asistentes en la importación del listado de productos a Excel.
- Añadido mensaje informativo sobre la inscripción múltiple en el proceso de inscripción a evento.
- Mejorado el tiempo de respuesta de la página pública del evento.
- Diversos arreglos de bugs del sistema.

## Versión 2013.6.17

### 17 de junio de 2013

- Ampliada la documentación de la plataforma.
- Nueva página "landing".
- Nueva plantilla para eventos, que muestra el menú en vertical con el estilo Compact.
- Nuevo campo en el formulario de registro que permite seleccionar países, en cualquier idioma de la plataforma.
- Añadida compatibilidad con la última versión de la API de Twitter.
- Añadida posibilidad de traducir respuestas predefinidas en las preguntas de selección individual y múltiple del formulario de registro.
- Diversos arreglos de bugs del sistema.

## Versión 2013.6.3

### 3 de junio de 2013

- Se ha añadido un nuevo permiso disponible para los comités que da acceso a los listados de productos relacionados.
- Mejora estética al mostrar el listado de receptores de pago.
- Ahora es posible filtar el listado de inscritos por el estado del pago.
- El [formulario de inscripción](/docs/eventos/asistentes/formulario-de-inscripcion) a un evento permite ahora adjuntar ficheros.
- Mayor velocidad al listar pagos en el panel de gestión económica.
- El sistema de caché de la plataforma ha sido mejorado.
- Ahora es posible [exportar los pagos de un evento](/docs/gestion-economica/herramientas/gestionar-pagos-de-un-evento) a fichero Excel.
- Diversos arreglos de bugs del sistema.

## Versión 2013.5.20

### 20 de mayo de 2013

- Ahora se permite comprar productos y vincularlos a una inscripción ya existente. Puede hacerse desde el correo electrónico que contiene el recibo o desde el [panel de asistente](/docs/panel-de-usuario/eventos-a-los-que-asisto).
- El [formulario de inscripción](/docs/eventos/asistentes/formulario-de-inscripcion) a un evento permite ahora preguntas con respuestas predefinidas.
- Mejorada la gestión de pagos pendientes. Si se detecta que el usuario actual tiene un pago pendiente se le asiste para averiguar si ha tenido alguna incidencia. En tal caso, puede retomar el pago o cancelarlo. ([ver FAQ](/docs/faq#gestion-de-errores-en-los-pagos))
- Las fechas del programa ahora se ajustan automáticamente al inicio del evento como sugerencia.
- Diversos arreglos de bugs del sistema.

## Versión 2013.5.6

### 6 de mayo de 2013

- El listado de eventos es ahora accesible en el panel de administración.
- Mejoras en la información del listado de eventos, reflejando contabilidad.
- Paginación en el listado de eventos.
- Receptores de pagos agrupados por tipología.
- Mejora en la copia de preguntas del formulario de inscripción pudiendo seleccionar a qué tipo de entrada copiarlo.
- Opción de borrar plantillas de eventos ya subidas.
- Notificaciones por correo cuando un producto a la venta queda fuera de stock.
- Opción de disminuir el stock de un producto ya a la venta a un mínimo de las ventas ya realizadas.
- Mejoras en el proceso de carga e indicadores de progreso mientras se realizan cargas de datos en segundo plano.
- Diversos arreglos de bugs del sistema.

## Versión 2013.4.25

### 25 de abril de 2013

- Nueva funcionalidad que permite configurar [unidades administrativas](/docs/gestion-economica/configuracion/accounting-units) para facilitar la gestión económica
- Nueva funcionalidad que permite añadir [usuarios de soporte](/docs/administracion/usuarios/helpdesk-users), destinados a ofrecer ayuda
- Nueva funcionalidad que muestra un [listado de eventos](/docs/gestion-economica/herramientas/events-list) en el panel de gestión económica
- Nueva funcionalidad que permite configurar un [dominio personalizado](/docs/eventos/herramientas/custom-domain) para tu evento
- Añadido al panel contable un listado de eventos pendientes de que se les asigne un receptor de pagos
- Las inscripciones ya no requieren un plazo de disponibilidad, si no se indica ninguno, se utiliza el plazo de inscripción
- Mejorado el sistema de copiado de preguntas entre inscripciones para incluir las traducciones, obligatoriedad, etc.
- Mejorado el listado de asistentes que ahora incluye también las asistencias canceladas.
- Mejorada la administración de los TPV REDSYS para soportar los distintos tipos de firmado del mensaje.
- Mejorado el comportamiento de los TPV REDSYS en los casos en los que el TPV omite la respuesta por URLOK.

## Versión 2013.4.15

### 15 de abril de 2013

- Mejoras en el proceso de cancelación de un evento. Además de tener una traza contable en los pagos, se muestra un formulario para contactar con la organización del evento.
- El enlace a la página de Facebook que aparece en la pantalla principal, en la caja de redes sociales, se puede configurar desde el panel de administración
- Ahora puedes poner en modo borrador el evento si aún no ha empezado el plazo de inscripción; además antes de publicar el evento se pide confirmación
- Se pueden seleccionar varios asistentes a los que enviar un correo electrónico desde el menú de edición del evento
- Se han corregido varios errores tipográficos
- Se ha actualizado el formulario de publicaciones Editum (sólo Universidad de Murcia)
- Se han añadido más textos de ayuda en la edición del evento
- Nueva funcionalidad que permite configurar el [servidor de envío de correo electrónico](/docs/administracion/configuracion/email-server), y actualizar el correo electrónico de contacto
- Se ha actualizado el texto que aparece al pie de los correos electrónicos
- Ahora puedes modificar más detalles de un receptor de pago en uso
- Ahora puedes elegir si tu receptor de pago está en modo pruebas o listo para ser usado
- Se ha mejorado la visualización del fichero de listado de asistentes, descartando preguntas repetidas en el formulario de inscripción
- Mejoras en la gestión de plantillas personalizadas, ahora se pueden bajar para modificar
- La opción de mostrar en el portal de Eventos de Emagister ahora está disponible para los organizadores, desde Datos básicos de la edición del evento
