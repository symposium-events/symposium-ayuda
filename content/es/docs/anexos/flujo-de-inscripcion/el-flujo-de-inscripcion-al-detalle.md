---
title: "El proceso de inscripción"
weight: 1
lastmod: 2019-07-05T11:32:15Z
dokuwiki: el_flujo_de_inscripcion_al_detalle
---
## Diagrama del flujo de inscripción

![](/media/el_flujo_de_inscripcion_al_detalle/inscripcion_usuario.png?w=650&align=center)

## Introducción: los actores involucrados

En en el proceso de inscripción en un evento de SYMPOSIUM by Emagister encontramos diversos actores que participan en la forma en la que se procesa y procede en la inscripción. A continuación desglosamos estos conceptos a modo introductorio.

#### Organizador

El usuario que ha creado el evento, o un usuario al que se le ha cedido la potestad de afectar a la configuración de la inscripción del mismo mediante los diversos mecanismos disponibles en Symposium.

#### Asistente

El usuario que se ha inscrito en nuestro evento.

#### Administrador económico

Es un usuario administrador del sistema con la potestad para asignar un *Receptor de pago* a un evento, así como de validar y rechazar pagos.

#### Inscripción

Una inscripción (o entrada) es una entidad que engloba una serie de propiedades y que al asignarse a un usuario le convierte en *Asistente*. La inscripción está definida por un nombre, una descripción, un precio, una cantidad de unidades disponibles y un plazo de disponibilidad.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_6.png?align=center)

Una *Inscripción* estará disponible siempre que:

- Nos encontremos dentro del Plazo de inscripción
- Tengamos unidades disponibles y el Aforo no esté cubierto
- Tengamos asignado un receptor de pago si la inscripción es de pago
- La inscripción esté marcada como ‘visible’

La inscripción a un evento puede realizarse por medio de distintos tipos de inscripción (o entradas). Por ejemplo: un evento puede tener una inscripción con descuento para estudiantes y otra inscripción estándar.

#### Plazo de inscripción

Es un rango de fechas en el que estará habilitada la inscripción al evento. Fuera de este rango, la inscripción al evento no será posible. El *Plazo de inscripción*  prevalece sobre el plazo de disponibilidad de un tipo inscripción (entrada), es decir, si el *Plazo de inscripción*  se cierra, la *Inscripción*  no estará disponible aunque así lo indique su plazo de disponibilidad.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_7.png?align=center)

#### Validación

Es un [mecanismo](/docs/eventos/asistentes/inscripcion#validacion) mediante el cual el *Organizador*  tiene la potestad de decidir si acepta o no a un asistente ignorando cualquier otro dato. Este mecanismo es opcional.

#### Estado del pago

Indica si un pago realizado para completar una inscripción se ha realizado con éxito, está pendiente o por el contrario, se ha cancelado o rechazado. En el caso de una inscripción gratuita este estado se ignorará.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_8.png?w=718&align=center)

#### Receptor de pago

Es un mecanismo interno capaz de recibir un pago mediante alguna de las plataformas disponibles. Un evento deberá tener asignado un receptor de pago para que las inscripciones de pago estén disponibles.

Es posible asignar un receptor de pago ‘por defecto’ para que se asigne a todas las inscripciones de pago.

#### Unidad administrativa

Es un sistema opcional de agrupación de diversos actores para fragmentar la actividad económica de la plataforma. Una Unidad administrativa engloba receptores de pago, administradores económicos y eventos.

## Configurando la inscripción a un evento

Cuando [creamos un evento](/docs/eventos/creando-y-editando-un-evento/creando-un-evento-nuevo), éste figura inicialmente como *Sin registro*. Es posible entonces configurar dos tipos de inscripción que se gestionarán desde SYMPOSIUM by Emagister: inscripción gratuita e inscripción de pago.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_0.png?w=217&align=center)

Desde el menú de edición del evento, dentro de la sección Asistentes encontraremos [la subsección Inscripción](/docs/eventos/asistentes/inscripcion). En este momento nuestro evento figura como *Sin registro*. Podemos desplegar el menú para seleccionar una de las dos opciones mencionadas anteriormente.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_1.png?w=744&align=center)

La inscripción gratuita contendrá exclusivamente inscripciones sin coste mientras que la inscripción de pago podrá contener de ambos tipos.

Una vez seleccionemos el tipo de inscripción, se nos solicitará que indiquemos el *[Plazo de inscripción](#plazo-de-inscripcion)* . Este plazo restringirá las fechas en las que estará disponible la inscripción y no debe exceder las fechas del evento.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion.png?w=744&align=center)

Además se nos indicará si queremos activar la *[validación](/docs/eventos/asistentes/inscripcion#validacion)*. Activarla nos da la potestad para aceptar o rechazar a un asistente manualmente, independientemente del estado del pago de su inscripción o cualquier otro factor. Esta herramienta es útil cuando el evento tiene la entrada restringida a un colectivo con determinados requisitos o es susceptible de cualquier otro tipo de inscripción no deseada.

Finalmente, tras guardar los cambios, deberemos crear nuestra primera *Inscripción*.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_2.png?w=744&align=center)

Si hemos creado un evento gratuito, se nos creará automáticamente una inscripción sin coste. Si hemos decidido que nuestro evento será de pago, se nos guiará hacia el formulario de alta de *[Inscripción](#inscripcion)*para que definamos los valores adecuados. Podemos crear tantos tipos de inscripción (entradas) como consideremos necesarios.

Además, podemos indicar el aforo de nuestro evento. De este modo, podemos crear varias entradas de cantidad ilimitada pero limitar el total de ventas a un total determinado.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_3.png?w=745&align=center)

Por último, podemos [añadir un cuestionario](/docs/eventos/asistentes/formulario-de-inscripcion) a cada inscripción que hemos dado de alta. Podemos hacerlo desde la subsección *Formulario de Inscripción*  que encontraremos en la sección *Asistentes*.

## Preguntas frecuentes

### ¿Cuando están disponibles las inscripciones?

Las inscripciones estarán disponibles cuando se cumpla que nos encontramos dentro del plazo de inscripción y además, si la inscripción tiene sus propias fechas de disponibilidad, nos encontremos dentro de las mismas. Además, no deben haberse agotado las unidades disponibles.

Si la inscripción es de pago, solo estará disponible si al evento se le ha sido asignado un receptor de pago.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_9.png?w=700&align=center)

### ¿Cómo puede un organizador solicitar un receptor de pago?

Si se utilizan *[Unidades administrativas](/docs/gestion-economica/configuracion/accounting-units)*, al configurar el evento como de pago, se le mostrará un formulario para que solicite a una de las unidades administrativas disponibles que le asigne un receptor de pago.

De igual manera, incluso si no se utilizan unidades administrativas, los administradores económicos verán en su panel administrativo los [eventos que están a la espera de una asignación](/docs/gestion-economica/configuracion/asignar-receptor-de-pago#eventos-asignados-y-pendientes-de-asignacion).

Por último, está disponible el formulario de contacto con la plataforma para poder solicitar directamente la asignación a los administradores de la plataforma.

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_4.png?w=742&align=center)

### Si no deseo validación manual, ¿cómo se validan los asistentes?

Los asistentes se validarán automáticamente cuando se valide el pago, en caso de haberlo. Si el evento es gratuito, se validarán automáticamente al inscribirse. Puedes encontrar una explicación detallada de los distintos casos [aquí](/docs/eventos/asistentes/inscripcion#validacion).

## La inscripción al evento

En la web del evento, generalmente en la parte superior o en la columna derecha, encontraremos el botón de Inscripción al evento. Este botón llevará al usuario al [proceso de inscripción para convertirse en asistente](/docs/uso-de-la-plataforma/inscripcion-a-un-evento).

![](/media/el_flujo_de_inscripcion_al_detalle/configuracion_inscripcion_5.png?align=center)

En primer lugar se muestran las inscripciones disponibles y el usuario puede elegir la cantidad de cada una de ellas que desea reservar. Después se le solicitarán dos datos personales: nombre y apellidos y correo electrónico de contacto. A continuación, si se ha configurado un formulario de inscripción, en usuario deberá cumplimentarlo.

Tras realizar esta acción, el usuario confirmará la inscripción. Al hacerlo, se confirmará el proceso automáticamente en caso de ser gratuita. Si por el contrario era de pago, se le presentará un formulario para que elija el método que más le convenga.

Al pulsar sobre el botón ‘Finalizar’ el sistema guarda todos los datos relativos al proceso y los marca como pendientes. De este modo, es posible saber a qué usuarios y en qué casos se les presentó un problema al realizar la inscripción. Una vez se reciba confirmación del pago, se confirmarán los datos definitivamente.

## Validación del pago de inscripción y de la asistencia

Dentro de SYMPOSIUM by Emagister existen dos tipos de plataformas de pago: las que realizan la verificación automáticamente y las que requieren validación manual.

Las que realizan verificación automática informan por sí mismas a SYMPOSIUM de que el pago se ha recibido, indicando además un identificador de la transacción, el estado del mismo y la fecha en que se ha producido. En el caso de las que requieren validación manual, es SYMPOSIUM quien define el identificador de la transacción y un Administrador económico se encarga de aceptar o rechazar el pago.

| Plataformas de pago con verificación automática | Plataformas de pago con verificación manual |
|---|---|
| SERMEPA/REDSYS y PAYPAL | Transferencia bancaria |

### La relación entre el estado de la asistencia y el estado del pago

La asistencia tiene [3 estados](/docs/anexos/flujo-de-inscripcion/los-estados-de-una-inscripcion) que se asignan por parte del organizador o de la propia plataforma:

- **pendiente**: indica que la asistencia no ha sido confirmada ni rechazada
- **confirmada**: la asistencia ha sido confirmada, el asistente está inscrito en el evento
- **rechazada**: la asistencia ha sido rechazada, el asistente NO está inscrito en el evento

Además, la asistencia puede tener un cuarto estado [asignable por parte del asistente](/docs/panel-de-usuario/eventos-a-los-que-asisto) o de la plataforma:

- **cancelada**: la operación está cancelada a todos los efectos. Se guarda a modo de histórico pero no se contabiliza a nivel estadístico en aforo, etc.

**NOTA**: El estado ‘cancelada’ es independiente de los 3 estados principales. Una asistencia puede estar cancelada y pendiente o cancelada y confirmada. Esto se debe a que son actores distintos los que asignan estos estados, y para mantener la coherencia en la información es necesario combinar ambos valores.

El pago tiene 4 posibles estados:

- **pendiente**: es el estado inicial con el que se crea en la plataforma. Hasta que se recibe confirmación de la plataforma de pagos o manual, el pago figura como pendiente.
- **confirmado**: indica que se tiene constancia de que el pago se ha recibido y es correcto.
- **rechazado**: indica que el pago no se ha recibido, es incorrecto, o ha ocurrido alguna otra incidencia.
- **cancelado**: indica que el usuario o su plataforma de pago ha decidido dar marcha atrás en el proceso e interrumpir la operación.

En el caso de una validación manual no existe relación entre los estados. El organizador decide si confirma al usuario manualmente, independientemente del estado en que se encuentre el pago. No hay vinculación lógica entre ambas entidades dentro de la plataforma.

Si por el contrario la validación es automática (sin validación), la asistencia tendrá el mismo estado que el pago. Además, el rechazo o cancelación de un pago también provoca que se cancele la asistencia.

A continuación, esta tabla indica el estado de la asistencia cuando se recibe una actualización sobre el estado de un pago.

| Estado del pago | Estado de la asistencia |
|---|---|
| Confirmado | Confirmada |
| Rechazado | Rechazada y Cancelada |
| Cancelado | Rechazada y Cancelada |

## Preguntas frecuentes

### Al cancelar un pago, ¿qué datos permanecen en la plataforma?

Todos. Un pago cancelado figura como tal pero no se elimina. Tanto el pago como la asistencia que lo originó permanecen en el sistema como cancelados. No afectan a los cálculos estadísticos pero se sigue teniendo acceso a los mismos para atender a reclamaciones, etc.

### Si se rechaza un pago por error, ¿debe el usuario volver a inscribirse de nuevo al figurar su asistencia como cancelada?

No es necesario, ya que el administrador económico tiene la potestad de [volver a validar ese pago](/docs/gestion-economica/herramientas/gestionar-pagos-de-un-evento), re-confirmando esa asistencia de nuevo. Como no se eliminan los datos, esa asistencia figurará con la misma información que antes de que fuera cancelada.

### ¿El administrador económico tiene alguna restricción a la hora de cancelar o aceptar pagos?

El administrador de la plataforma puede [crear una contraseña de seguridad](/docs/administracion/pagos/clave-de-validacion-de-pagos) que será requerida a la hora de rechazar un pago, a modo de verificación de seguridad. No existe ninguna otra restricción. El Administrador económico puede [aceptar o rechazar un pago](/docs/gestion-economica/herramientas/gestionar-pagos-de-un-evento) tantas veces como sea necesario, quedando constancia de esta actividad para posterior análisis o revisión.

### ¿Se puede "descancelar" una asistencia?

Sí. Si el contable, mediante validación de pago manual (transferencia bancaria), confirma el pago de tu asistencia cancelada, ésta pasa a estar confirmada.

### ¿Qué es una inscripción nominativa?

Es un proceso de inscripción en el que los productos han sido asignados a los asistentes. Hay dos tipos:

- Cuando el proceso de inscripción es individual: todos los productos pertenecen al único asistente registrado.
- Cuando el proceso de inscripción es múltiple: cada producto pertenece al asistente que fue seleccionado durante el registro.

## Reglas de negocio

- Si una inscripción múltiple mezcla entradas gratuitas y de pago, el estado del pago de dicha inscripción afecta también a las entradas gratuitas. Es decir, que si se rechaza el pago de esta inscripción, las entradas gratuitas también serán rechazadas.

- Si una inscripción múltiple tiene asociados tanto productos gratuitos como de pago, el estado del pago de dicha inscripción afecta también a los productos gratuitos. Es decir, que si se rechaza el pago de esta inscripción, los productos gratuitos también serán rechazados.

- El estado de la asistencia no afecta al cómputo de las ventas, sólo el estado del pago afecta a este cómputo. Es decir, que puede haber una inscripción con un asistente cancelado pero cuyo pago es correcto, y por tanto, sumará el dinero correspondiente en las estadísticas, listados y ficheros excel.

- El estado de la asistencia sí afecta al cómputo de las unidades disponibles:
      - Las canceladas no cuentan como entradas adquiridas.
      - Las canceladas que forman parte de procesos de inscripción individuales con productos o múltiples nominativos con productos hacen que sus productos no cuenten como productos adquiridos.

- El cómputo de productos vinculados a inscripciones canceladas excluye los vinculados a inscripciones múltiples anónimas (no nominativas) porque es imposible saber a qué producto afecta cada inscripción.
