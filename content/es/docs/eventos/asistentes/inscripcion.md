---
title: "Inscripciones"
weight: 1
lastmod: 2025-03-05T09:45:47Z
dokuwiki: inscripcion
---
Symposium permite gestionar la forma en la que los usuarios pueden inscribirse en un Evento, el plazo para ello así como cuántos asistentes se aceptan. El diseño de las Inscripciones se hace en el menú **Asistentes > Inscripciones**.

![](/media/panel_organizador/inscripciones.png?w=250&align=center)

Existen cuatro tipos de registro:

- **Sin registro**: declara el Evento de libre asistencia y sin control por parte de la organización;
- **Registro en otra página web**: elige esta opción si el registro en el Evento se hace en alguna otra página web que no gestionas con Symposium;
- **Gratuito**: permite que haya un control de asistencia sin necesidad de gestión económica;
- **De pago**: es el tipo de inscripción más complejo y que implica que los asistentes tendrán que pagar una entrada al Evento. A partir de esta selección, Symposium te proporcionará numerosas herramientas para el control económico y de los asistentes. Desde este menú podrás administrar todo lo relacionado con la inscripción a tu Evento y en caso de que proceda, la venta de inscripciones al mismo. El menú está dividido en distintos bloques en los que gestionar cada uno de los aspectos de este apartado.

Tienes una explicación del flujo de Inscripción de Symposium en [este artículo](/docs/anexos/flujo-de-inscripcion/el-flujo-de-inscripcion-al-detalle).

## Tipo de registro

En este bloque puedes seleccionar el tipo de registro que quieres para tu Evento. Una vez seleccionado, guarda los cambios pulsando el botón "*Guardar*".

![](/media/inscripcion/tipoderegistro202302.png?w=837&align=center)

**ATENCIÓN  : Si cambias el tipo de registro en un Evento ya creado, todos los datos de los inscritos se borrarán.**

Las Inscripciones son las entradas para el Evento. Puedes crear varios tipos de Inscripción, según necesites y pueden tener precio o ser gratuitas.

Una vez elegido el tipo de registro, localiza más abajo la caja "Inscripciones". Debes crear al menos una Inscripción. Puedes crearlas según necesites y con las características que estimes. Por ejemplo, básicas, VIP, para adultos, para niños… Cada una de ellas tendrá un nombre, un precio y una divisa si el tipo de inscripción que escogiste antes es de pago, un número de entradas disponibles para ese tipo y si estará visible para los visitantes o no.

Puedes crear entradas que no aparezcan publicadas, es decir que los visitantes de la web no puedan adquirir porque no salen en la página, sino que las gestionarás personalmente a modo de invitaciones.

### Validación

La validación permite al organizador [validar manualmente a los asistentes](/docs/eventos/asistentes/listado#la-informacion-disponible-en-el-listado-de-asistentes). A continuación se indica en una tabla el comportamiento que se obtiene al combinar los distintos tipos de inscripción y validación.

| Tipo de registro | Con Validación | Definición | ¿Cuando se confirma una asistencia? |
|---|---|---|---|
| Sin registro |  | No se gestionan inscripciones | No aplicable |
| Registro en otra página web |  | Se indica un enlace externo desde donde se gestionarán las inscripciones | No aplicable |
| Gratuito | No | Gestión de Inscripciones gratuitas sin necesidad de validación | La Inscripción estará confirmada automáticamente |
| Gratuito | Sí | Gestión de Inscripciones gratuitas que deben ser validadas manualmente | El organizador confirma manualmente a cada asistente. Hasta entonces toda inscripción figura como "pendiente" |
| De Pago | No | Gestión de Inscripciones gratuitas o de pago sin necesidad de validación | Las Inscripciones gratuitas se confirmarán automáticamente. Las Inscripciones de pago se confirmarán automáticamente a la recepción del pago, pero si no llega figurarán como "pendiente" |
| De Pago | Sí | Gestión de Inscripciones gratuitas o de pago que deben ser validadas manualmente | Toda Inscripción figura como "pendiente" hasta que el Organizador las confirme manualmente, incluyendo las de pago que se hayan abonado. |

Un Inscrito debe estar Confirmado para figurar como Asistente de pleno derecho. Un Inscrito rechazado no cuenta para el aforo o cualquier otra estadística.

![](/media/inscripcion/inscripcion_estado_1_.png?align=center)

### Privacidad

Una asistencia a un Evento puede ser pública o privada. Pública significa que es visible en el listado de asistentes de cara a cualquier visitante de la plataforma, mientras que privada mantiene la inscripción oculta a cualquier persona ajena a la organización del Evento.

El organizador puede seleccionar que tipo de privacidad quiere para las asistencias. Puede permitir que sea cada asistente el que decida si su asistencia es pública o privada, o si, por el contrario, prefiere que todas las asistencias sean privadas por defecto.

### Unidades Administrativas

Si seleccionas el Tipo de Registro como "De Pago" y en tu plataforma se han configurado [Unidades Administrativas](/docs/gestion-economica/configuracion/accounting-units), podrás solicitar a una de las unidades que te asigne un receptor de pagos. Hazlo solo en los casos en los que sepas que Unidad Administrativa te corresponde, y en caso de no saberlo consulta con los Administradores de la plataforma.

### Limitar inscripciones múltiples

Este ajuste se aplica solamente en el evento que estés editando. Es posible que tu plataforma te permita seleccionar si quieres limitar o si quieres permitir las inscripciones múltiples. Sin embargo, en algunas circunstancias, los Adminsitradores de la plataforma pueden haber solicitado a SYMPOSIUM que se limiten en todos los casos. Si es así, este selector no aparecerá.

Si seleccionas Limitar la inscripción múltiple, un usuario que visite la web de tu evento sólo podrá hacer una inscripción y no se le facilitará inscribir a varias personas en un mismo proceso. Este ajuste guarda relación directa con un atributo que pueden tener los [tickets](/docs/eventos/asistentes/inscripcion#inscripciones1) (los tipos de inscirpción que diseñes en tu evento).

De serie, en SYMPOSIUM existe una lógica que permite que una misma persona haga las inscripción de varias en un mismo evento. Puedes limitar esa posibilidad si quieres mayor control sobre el número de inscripciones que adquiere una misma persona en una sesión de trabajo. No obstante, debes tener en cuenta que esa misma persona puede completar una inscripción y, de inmediato o más adelante, hacer otra para un tercero.

## Ley Orgánica de Protección de Datos - Tratamiendo de datos personales

Si tu Evento tiene configurado registro de usuarios, será necesario que selecciones una de las [plantillas para la Ley de Protección de Datos](/docs/administracion/cobertura-legal/politica-de-privacidad), creada previamente por el Administrador de la plataforma.

![](/media/panel_organizador/plantillas_lopd.png?w=750&align=center)

## Capacidad del Evento

En este bloque puedes determinar si el Evento tiene capacidad ilimitada o si por el contrario hay un número de inscripciones disponibles antes de completar el aforo.

![](/media/panel_organizador/aforo.png?w=750&align=center)

Escribe el número de plazas disponibles para el Evento o deja el campo de texto en blanco si quieres que tenga capacidad ilimitada. También puedes decidir si la capacidad del Evento se muestra en su página principal o si por el contrario permanece oculta, utilizando el check "Mostrar capacidad". Finalmente, haz clic en Guardar.

Puedes cambiar el aforo en cualquier momento, aunque hay restricciones.

- El nuevo aforo nunca puede ser inferior al número de inscritos, cuando ya los haya.
- El nuevo aforo nunca puede ser inferior a la suma de inscritos validados más inscritos pendientes de validar, cuando la validación manual esté activa.
- El nuevo aforo nunca puede ser inferior a la suma de inscritos validados más los pendientes más las inscripciones con pago confirmado, aunque estas correspondan a inscripciones canceladas. Para que estas últimas dejen de contar, se deben rechazar primero esos pagos.

## Plazo de inscripción

En este bloque puedes establecer el periodo durante el cual se realizará la Inscripción o venta de Inscripciones del Evento, seleccionando fechas de inicio y de cierre.

![](/media/panel_organizador/plazo_de_inscripcion.png?w=750&align=center)

Como se indica en el recuadro de aviso, debes tener en cuenta que las fechas y horas que indiques deben ser las locales del lugar de celebración. Symposium da soporte a distintos husos horarios.

## Inscripciones {#inscripciones1}

Aquí podrás gestionar todo lo relacionado con las entradas para el Evento. Al principio se mostrará un cuadro de aviso con las formas de pago que están disponibles para el Evento. Estos medios de pago aceptados se configuran en el panel de Administración y no dependen específicamente de un Evento. si necesitas que se acepte otro medio de pago, por favor contacta con el Administrador del sitio web.

![](/media/inscripcion/entradas20230228.png?w=837&align=center)Puedes configurar varios tipos de inscripciones, cada una con unas características distintas que se ajusten a tus necesidades como organizador del Evento.

Para cada tipo de inscripción puedes configurar las siguientes características:

- Nombre de la inscripción.
- Gratuita o de pago, y en su caso, el precio de la inscripción.
- Capacidad ilimitada, o número límite de inscripciones disponibles.
- Visibilidad del número de inscripciones disponibles, de forma que el público pueda verlo o no.
- Máximo de unidades que un usuario puede reservar o adquirir.
- Fecha y hora de inicio y finalización del periodo de venta de la inscripción.
- Una descripción sobre qué ofrece el tipo de inscripción, qué servicios incluye o cualquier otra información útil para el usuario.

De esta forma, puedes gestionar completamente la suscripción a tu Evento. Por ejemplo, es posible dar de alta una inscripción con precio reducido hasta 15 días antes del Evento, y una segunda con el precio normal desde esa fecha hasta el inicio del Evento. También puede ser que el precio de las inscripciones varíe según los servicios que ofrezcan. Todo esto es perfectamente configurable utilizando las herramientas que se ofrecen en la plataforma.

El selector Max tiene como valor por defecto 10 y consiste en limitar cuántas unidades de un mismo tipo de inscripción puede adquirir un usuario al hacer inscripción múltiple. Así, puedes tener más control sobre la asistencia al evento. El valor máximo es, también, de 10 unidades por cuestiones técnicas. Es importante tener en cuenta que este ajuste depende de la configuración de la plataforma y la del propio evento:

- si los Administradores de plataforma solicitaron a SYMPOSIUM limitar las inscripciones múltiples, este selector no aparecerá;
- si has configurado tu evento para Limitar la inscripción múltiple, este selector tampoco aparecerá.

Una vez has terminado de configurar el tipo de entrada, haz clic en “Guardar” para guardar los cambios. Para repetir el proceso y añadir más tipos de entrada, haz clic en el botón "*Añadir*".

## Casos especiales

Recuerda que el Evento puede tener configuradas unas fechas de plazo de inscripción. En ese caso, estas fechas predominan sobre las fechas de disponibilidad de las inscripciones. Si el plazo de inscripción se cierra mientras que las inscripciones están abiertas, no estarán disponibles.

Así mismo, si decides ampliar el plazo de inscripción a tu Evento, recuerda ampliar el plazo de disponibilidad de las inscripciones.

Para poder recibir pagos en la plataforma, el administrador del sitio debe haber habilitado y asignado a tu Evento algún Receptor de Pago. Si creas inscripciones de pago sin que esta asignación haya tenido lugar, estas no serán visibles para el público.

Si intentas eliminar un tipo de inscripción y la plataforma te indica que no es posible porque tiene un formulario de inscripción compartido con otro ticket, será porque uno o varios campos personalizados del [formulario de inscripción](/docs/eventos/asistentes/formulario-de-inscripcion) de ese ticket han sido copiados en otro que ya tiene ventas:

![](/media/archivos_asistentes/eliminar_inscripcion.png?w=800&align=center)

Por tanto, la plataforma impide su eliminación para evitar la pérdida de la información obtenida por el formulario de inscripción.

Como alternativa, sugerimos que lo marques como no visible desmarcando el check de ¿Visible? Así, no se mostrará en el proceso de inscripción.

## Donaciones

Los Eventos permiten la recaudación mediante Donaciones. Estas funcionan como Inscripciones que no afectan al aforo del Evento. Se pueden crear tantos tipos de Donaciones como se precise y los Donantes aparecerán en los [listados de Asistentes](/docs/eventos/asistentes/listado) que un Organizador puede obtener en los menús de control de asistencia.

![](/media/panel_organizador/donacion.png?w=750&align=center)

Como se muestra en la imagen, no es necesario fijar un precio o cantidad, ya que el usuario es libre de realizar el aporte que considere. Además es posible utilizar sistemas similares a los de las inscripciones como limitar las fechas de disponibilidad. Además, en los Eventos multi idioma se replicarán las Donaciones y sus fechas, si se establecen, pero será necesario traducir y adaptar los textos en cada versión de la web por separado.

![inscripdonacionesfront.jpg](/media/inscripcion/inscripdonacionesfront.jpg?w=180&align=center)

En la web del Evento, junto al botón Inscripción aparecerá el que permite donar y al hacer clic en él, aparecerá un formulario igual al de Inscripción. Es posible personalizar ese formulario de Donación con nuevos campos definidos por el Organizador, de la misma forma que se pueden personalizar los de Inscripción con la utilidad del menú **[Asistentes > Formularios de inscripción](/docs/eventos/asistentes/formulario-de-inscripcion)**  .

![inscripdonacionesfront_02.jpg](/media/inscripcion/inscripdonacionesfront_02.jpg?w=885&align=center)

## Recordatorio de evento próximo

En la parte inferior, puedes encontrar un bloque como el siguiente:

![](/media/archivos_asistentes/recordatorio.png?w=700&align=center)Por defecto, los eventos no están marcados para enviar recordatorios.

Si activas el check, el evento pasará a la lista para enviar email recordatorio a los asistentes confirmados para informarles de la proximidad del inicio del evento.

El proceso se lanza todos los días a las 0:00 UTC y tendrá en cuenta los eventos cuyo inicio se encuentre entre las 24 y 48 horas previas a la hora de ejecución.
