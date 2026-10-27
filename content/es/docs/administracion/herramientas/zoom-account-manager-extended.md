---
title: "Gestión de cuentas Zoom"
weight: 93
lastmod: 2022-02-24T09:27:02Z
dokuwiki: zoom_account_manager_extended
---
En este artículo te explicamos cómo funciona la integración de cuentas propias de Zoom y detallamos todas las funcionalidades específicas de este módulo.

El módulo de cuentas propias Zoom permite a la institución usar su propia cuenta de Zoom integrada en la plataforma de gestión y en el flujo de los eventos. Puedes ofrecer salas de webinar con gestión automatizada de las reservas y también disponer de salas con control manual.

- Los organizadores de eventos recibirán credenciales únicas para ocupar las salas.
- Los asistentes inscritos a los eventos recibirán enlace para participar.
- Al terminar cada webinar, la plataforma generará automáticamente el informe de asistencia.

Consulta los Pasos para vincular una cuenta propia de Zoom en Symposium [aquí](/docs/administracion/herramientas/zoom-account-manager)

## La visión del organizador del evento

### Solicitud de sala para webinar

Los organizadores de eventos de tu plataforma pueden solicitar salas de webinar desde el menú Contenido → Programa / Videoconferencias. El proceso es muy sencillo y consiste en que indiquen:

- Título del webinar
- Fecha y hora en que debe comenzar
- Duración en minutos
- Si quieren permitir el acceso a los participantes manual o automáticamente

### Confirmación de la sala

Una vez que un organizador solicita una sala, Symposium consultará las que hay activas en la plataforma para asignación automática. No se tendrán en cuenta las salas que estén activas con gestión manual.

**Se calcula el tiempo total de reserva de la sala, que consiste en la suma de:**

- Tiempo de preparación (antes de la hora de inicio del webinar)
- Duración de la sala
- Tiempo de cortesía (después de la hora de fin del webinar)
- Tiempo de postprocesado que necesita la plataforma de eventos

**Se recorre secuencialmente la lista de salas activas y con asignación automática para localizar cuál tiene disponible todo el intervalo de tiempo que se necesita bloquear**.

- Si se encuentra una sala libre en el horario que se necesita, se le asigna
- Si no se encuentra una sala disponible en el horario solicitado:
      - se guarda la solicitud y se informa al organizador
      - se muestra sugerencia de contactar con los administradores de la plataforma para que le proporcionen una sala

### Inicio de la sesión de webinar

Llegada la fecha en que se celebra un webinar, Symposium realiza varios procesos:

- Con la antelación que se haya configurado en la plataforma, genera unas credenciales de uso de la sala asignada, que son válidas sólo para ese webinar, consistentes en:
      - Dirección web para abrir la aplicación Zoom
      - Nombre de usuario, que es el email asociado a la sala
      - Contraseña, que genera la plataforma
- Envía por email al solicitante de la sala las credenciales y también las pone a su disposición en el menú Contenido → Programa / Videoconferencias, donde realizó la solicitud.
- Envía por email a los asistentes inscritos al evento una dirección web para acceder a la sala. También la hace disponible para ellos en su panel privado de usuarios de la plataforma, si hacen login con su cuenta personal.

### Finalización del webinar

Diez minutos antes de la hora de finalización del webinar, se envía al organizador un email de aviso para que pueda cerrar la sesión a tiempo.<br> Si el anfitrión del webinar no cierra la sala desde la aplicación Zoom a la hora prevista, se le proporciona un tiempo de cortesía, el cual los administradores pueden establecer para toda la plataforma en el bloque Configuración.

Pasado el plazo de cortesía, Symposium finaliza automáticamente el webinar sin más aviso, cierra la sala y comienza el proceso de generación del informe de asistentes, que estará disponible para los organizadores en el menú **Contenido → Programa / Videoconferencias.**  También quedará disponible para los administradores en su menú **Webinars > Informes de webinars**.

## Cómo funciona la Vinculación de tu cuenta Zoom

El modelo de integración de Symposium para las cuentas de Zoom está centrado en el concepto de salas de webinar disponibles para que los organizadores de eventos las usen. Es análogo al funcionamiento de las salas de reuniones que hay en las oficinas.

<br> Una cuenta maestra de Zoom puede contener múltiples subcuentas. En el modelo de integración con Symposium, esas cuentas son salas y se ponen a disposición de todos los organizadores de la plataforma. Cuando un organizador va a usar una, Symposium le proporciona una contraseña válida sólo para ese webinar. Al terminar, la contraseña caduca y la sala queda libre.

<br> Al hacer clic en el botón Vincular cuenta, Symposium te llevará al portal de Zoom y, tras hacer login en la cuenta maestra, autorizarás a Symposium a gestionarla.

<br> Symposium no puede crear usuarios ni borrarlos dentro de tu cuenta de Zoom. En su lugar, se hace una lista de las cuentas vinculadas que tiene y las convierte en salas. Como administrador, decides cuántas de ellas se hacen disponibles.

Importante: Symposium nunca utiliza el usuario principal de la cuenta, el que ejerce la propiedad, aunque también tenga licencia de Webinar. Consideramos una buena práctica que la cuenta tenga un usuario sin licencia Webinar y que sólo sirva para la gestión.

Una vez vinculada la cuenta en Symposium, verás un listado con las subcuentas de Zoom asociadas. Estas subcuentas se pueden convertir en **Salas de webinar**  disponibles.

![gestionar_enlace_con_cuenta_1.jpg](/media/admin/gestionar_enlace_con_cuenta_1.jpg?w=829&align=center)

Por tanto,<br> **Usuarios de la cuenta de Zoom = Salas disponibles en Symposium**

<br> De inicio, las salas están desactivadas. Para que los anfitriones puedan solicitarlas, activa las que consideres.

### Convivencia con la cuenta de Symposium

El actual servicio de videoconferencia de Symposium consiste en una integración mediante la cual Symposium presta salas de Zoom a los organizadores que las solicitan para celebrar eventos online. Estas salas, propiedad de Symposium, mantienen una configuración estándar para todos los partners y están sujetas a disponibilidad.

<br> En el momento en que vincules una cuenta propia de Zoom en la plataforma, las salas de Symposium dejarán de estar disponibles y pasarás a gestionar el módulo de videoconferencias con tus salas y configuración personalizada.

Los organizadores que a partir de entonces soliciten salas de webinar, pasarán a utilizar las salas que habilites en tu portal con tus condiciones y preferencias.

### ¿Qué ocurre si ya hay webinars reservados con la cuenta de Symposium?

Es posible que antes de vincular tu cuenta en la plataforma haya algunos webinars reservados con el módulo de Symposium. Estos webinars se celebrarán con las salas prestadas por Symposium. A partir de la vinculación de tu cuenta institucional, las nuevas reservas se asignarán a tus salas.

## Salas de webinars activas

Este listado muestra todas las salas activas que están a disposición de los organizadores de webinars.<br> <br> ![](/media/admin/anfitriones_de_webinar.png?w=800&align=center)

### Modo de asignación

Las salas pueden funcionar de dos modos: manual y automático.

- Modo **automático**: la plataforma autoriza el uso de la sala a quien la solicita, si está disponibles en el tramo horario que se pide;
- Modo **manual**: la sala sólo puede autorizarla un administrador de plataforma. También es posible asignarla a un webinar que ya tuviese asignada otra sala.

Por defecto, las salas activas están configuradas en modo **manual**. Activa el modo automático para las salas que quieras que estén disponibles sin necesidad de que un administrador intervenga.

También es posible cambiar el modo de asignación a **Manual**de una sala que estuviese en **Automático**, siempre que no tengan ninguna reserva de webinar.

### Videoconferencias

Consulta los webinars asignados a cada una de las salas.<br> ![](/media/admin/anfitriones_de_webinar_videoconferencias.png?w=800&align=center)

En el listado aparecen todos los webinars asignados a cada sala con indicación de:

- Fecha y hora de inicio
- Zona horaria del evento
- Título del webinar
- Id y enlace a la web del evento
- Horario bloqueado de la sala, en el que se tiene en cuenta tanto la duración total de la sesión del webinar como el tiempo previo de preparación y tiempo de cortesía establecido.
- Botón Editar<br>

#### Reasignación manual de Webinar

<br> El botón Editar de la lista de webinars de una sala muestra todos los detalles de la sesión y la posibilidad de moverlo a otra sala distinta de la que tiene.

<br> **IMPORTANTE**: La reasignación de sala significa borrar el Webinar y volver a crearlo en otra sala. Si el Webinar tenía designados panelistas, el organizador deberá invitarles de nuevo. El enlace que recibieron en su momento ya no servirá.

![](/media/admin/unnamed.png?w=718&align=center)

### Desactivar salas

<br> Puedes desactivar una sala y dejará de estar disponible. Al hacerlo, ya no saldrá en el listado “Salas de webinar activas”. Mientras forme parte de la cuenta de Zoom, la encontrarás en el bloque “Gestionar enlace con cuenta de Zoom”, desde donde podrás volver a activarla.

No podrás desactivar las salas que tengan webinars ya programados.<br>

## Calendario de webinars

Muestra todos los webinars de la plataforma en formato calendario:

- Webinars pendientes de asignación
- En curso
- Programados a futuro

Puedes obtener una vista general por mes, semana o día. Cada webinar se muestra como una caja de color. Al hacer clic, se muestra la ventana de Edición del webinar, con sus datos completos y la posibilidad de reasignarlo a otra sala.

![](/media/admin/calendario.png?w=824&align=center)

## Webinars que se van a iniciar

En este bloque aparecerán los webinars que están a punto de comenzar, pero para los que aún no han generado las credenciales de anfitrión. El proceso de generación tarda tan sólo unos segundos, así que es normal que este listado se encuentre vacío. Si por algún motivo el proceso se demora, puedes lanzar la generación de credenciales a mano.

![](/media/admin/iniciando.png?w=838&align=center)

## Peticiones de sala sin asignar

En este listado, encontrarás las solicitudes de webinars que están a la espera de una sala. Puedes atenderlas con dos botones:

- **Asignación automática:**  se le intentará asignar una de las salas que esté en modo automático. Es posible que una petición de webinar esté en el listado porque no haya salas disponibles en ese horario.
- **Asignación manual:**  puedes asignar a la petición de webinar cualquiera de las salas. Si la que intentas asignar no está disponible en el horario solicitado, verás el aviso de que no se ha podido hacer la asignación. Podrás probar a asignar otra sala.

Cuando el tramo horario de una petición de webinar no está disponible en ninguna de las salas de la plataforma, puedes:

- Contactar con el solicitante para que borre la sala y solicite otro horario.
- Ir a tu cuenta maestra de Zoom y contratar un nuevo usuario con licencia Zoom Webinars. Al regresar a Symposium, lo encontrarás en el bloque “Gestionar enlace con cuenta Zoom” y lo podrás activar en la plataforma, bien en modo manual, bien en modo automático. Finalmente, podrás asignar esta nueva sala a la solicitud de webinar.<br>

![](/media/admin/solicitados.png?w=866&align=center)

## Configuración

Establece los valores que se aplicarán a todos los webinars de la plataforma:

- Máximo y mínimo de días de antelación para reservar webinars
- Duración máxima y mínima en minutos que tendrán los webinars
- Tiempo de preparación en el que se generarán las credenciales para los nuevos anfitriones
- Tiempo de cortesía que se añade a la duración total del webinar para ultimar las conclusiones de la sesión.

![duracion_webinar.jpg](/media/admin/duracion_webinar.jpg?w=800&align=center)

El tiempo de duración total de un webinar se compone de:

- El tiempo de preparación de credenciales y envío de correos a participantes
- Periodo de duración de la sala establecido por el solicitante en el formulario de reserva
- Tiempo de cortesía establecido
- Procesado automático que se ocupa de cerrar las salas y generar nuevas credenciales.
