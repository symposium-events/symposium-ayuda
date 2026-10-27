---
title: "Preguntas frecuentes"
weight: 85
lastmod: 2013-05-21T08:41:59Z
dokuwiki: faq
---
[¿Cómo puedo borrar un evento?](/docs/faq#borrando-un-evento)

[¿Cómo puede un administrador borrar un evento, incluso si tiene inscritos?](/docs/faq#borrando-un-evento-como-administrador-de-la-plataforma)

[Mi evento muestra el botón de inscripción pero no se le puede hacer clic ¿qué ocurre?](/docs/faq#la-inscripcion-al-evento)

[No veo donde puedo inscribirme en mi evento ¿cómo lo hago?](/docs/faq#la-inscripcion-al-evento)

[Si tengo un evento de entrada gratuita con cena (la cena cuesta 10€) ¿cómo puedo hacer que Symposium gestione la inscripción a mi evento?](/docs/faq#la-inscripcion-con-cena)

[Si tengo un evento de entrada gratuita con cena (la cena se paga allí al restaurante) ¿cómo puedo hacer que Symposium gestione la inscripción a mi evento?](/docs/faq#el-formulario-de-inscripcion)

[Tengo dos salas con dos sesiones en paralelo, una con 40 personas de aforo en una y 25 en otra. ¿cómo puedo gestionar la inscripción para completar las dos salas?](/docs/faq#aforos-por-inscripcion)

[¿Qué sucede si durante la inscripción ocurre un error y no se puede completar un pago?](/docs/faq#gestion-de-errores-en-los-pagos)

## Borrando un evento

Para borrar un evento debemos dirigirnos a nuestro Panel de Organizador. Pulsando en la barra superior sobre nuestro nombre de usuario navegaremos a la sección de usuario y desde allí podremos acceder al Panel de Organizador seleccionando la pestaña correspondiente.

Una vez dentro veremos un listado de nuestros eventos, separados por próximos a celebrarse o los ya ocurridos. Junto al título del evento encontraremos los botones VER, EDITAR y BORRAR.

Cuando borremos un evento que tiene asistentes estos recibirán una comunicación por correo electrónico indicándoles que el evento se ha cancelado.

NOTA: Un evento que ha recibido algún pago no puede ser borrado. Por motivos de seguridad, los datos relativos a pagos se mantienen en la herramienta durante un tiempo para cubrir reclamaciones y otras incidencias.

## Borrando un evento como Administrador de la plataforma

En ocasiones puede ser necesario eliminar un evento incluso cuando tiene inscritos y ha recibido pagos, como por ejemplo, cuando se realizan pruebas y demostraciones. A continuación vamos a explicar como un Administrador de la plataforma puede deshacer cualquier tipo de operación unilateralmente. NOTA: Está totalmente desaconsejado modificar un evento real ya que creará inconsistencia de datos y será imposible dar soporte en caso de reclamaciones y otras incidencias.

### Precondición

Para poder borrar un evento o pasarlo de nuevo a modo borrador deben cumplirse las siguientes condiciones:

- El evento NO debe tener ningún inscrito
- El evento NO debe encontrarse actualmente en plazo de inscripción

### Como eliminar las inscripciones a un evento

En caso de que las inscripciones a un evento deban ser eliminadas, el Administrador deberá [suplantar a los inscritos](/docs/administracion/usuarios/entrar-como-otro-usuario) uno por uno, y cancelar sus inscripciones.

Para poder suplantar a un usuario, necesitamos conocer el correo electrónico con el que se ha registrado en la plataforma. Es importante que sea el correo electrónico del inscrito y no debemos confundirlo con el correo de contacto de su inscripción. Para ver las direcciones de correo de los usuarios inscritos a nuestro evento, acudiremos al [listado de asistentes](/docs/eventos/asistentes/listado). Allí podremos pulsar sobre "Imprimir / Exportar a EXCEL" para obtener toda la información relativa a los mismos, incluido sus correos electrónicos.

![](/media/faq/correo_asistente.png?align=center)

A continuación, [suplantaremos uno por uno](/docs/administracion/usuarios/entrar-como-otro-usuario) a los asistentes utilizando la opción "Nombre o email de usuario" y el dato que hemos obtenido del listado. Una vez suplantado, nos dirigiremos a su [listado de asistencias](/docs/panel-de-usuario/eventos-a-los-que-asisto) para CANCELAR la asistencia al evento que queremos borrar. Si el asistente ha realizado un pago, se le pedirá confirmación para cancelar su inscripción. Deberemos aceptar la confirmación para poder borrar completamente la asistencia.

Una vez hayamos cancelado la asistencia de todos los asistentes, procederemos con el siguiente paso.

### Cerrando la inscripción al evento

Para que la inscripción al evento no se encuentre en vigor, debemos modificar las fechas de inscripción del mismo. Eso lo haremos desde la sección [Fechas de interés](/docs/eventos/herramientas/fechas-de-interes). Fijaremos la fecha de cierre de inscripciones a un día en el pasado y pulsaremos en Guardar.

Ahora nuestro evento tiene la inscripción cerrada y podemos proceder a eliminarlo o volver a colocarlo como borrador.

### Volver a modo Borrador

Un evento en modo borrador es invisible para los usuarios, por lo que permite ocultar efectivamente cualquier contenido de pruebas. Para devolver el evento al estado Borrador, una vez seguidos los pasos anteriores, nos encontraremos con el botón "¿Volver a borrador?" en la zona superior derecha de la pantalla.

![](/media/faq/volver_a_borrador.png?w=420&align=center)

### Eliminando el evento

Si preferimos eliminar el evento por completo, podremos hacerlo desde nuestro [listado de eventos](/docs/eventos/panel-de-organizador/organizador-de-eventos). Cabe recordar que SOLO podremos eliminar un evento si no ha recibido ningún pago. Si nuestro evento ha recibido alguno, deberemos limitarnos a devolverlo al [modo borrador](/docs/faq#volver-a-modo-borrador).

## La inscripción al evento

En la página de un evento tendremos disponible, generalmente en la cabecera, un botón con el texto "Inscribirse" que nos permitirá iniciar el proceso de inscripción. Normalmente tiene un tamaño mayor al resto de elementos y se encuentra en la parte superior de la página del evento, próximo al título y la imagen de cabecera, aunque es posible que una plantilla lo muestre en otro lugar.

Este botón se muestra solamente si se cumplen una serie de condiciones:

- Nos encontramos dentro del plazo de inscripciones
- Existe al menos una inscripción cuyo propio plazo de inscripciones también está en curso
- En caso de que nuestro evento sea de pago, nuestro evento debe tener un receptor de pagos asignado

Por lo tanto, para comprobar si nuestros datos son correctos, deberemos comprobar en orden que:

- En la sección Fechas de Interés, dentro de la sección Herramientas, tenemos dadas de alta las fechas de Apertura y cierre de inscripciones adecuados.
- A continuación, desde Inscripción, en la sección Asistentes, comprobaremos que en Tipo de Inscripción hemos seleccionado una opción distinta a "Sin registro".
- En la misma sección, más abajo, encontramos el bloque Inscripciones. Deberemos comprobar que la inscripción que creemos debe estar disponible tiene las fechas adecuadas. Lo haremos pulsando sobre el icono con forma de lápiz que se muestra a la derecha de la misma.

Si a pesar de que los datos son correctos no puede ver el botón "Inscribirse", compruebe que no está utilizando una plantilla personalizada que contenga algún error. En la sección Diseño, entre en la herramienta Plantillas y seleccione alguna de las plantillas de sistema (Modern, Classic, Elegant o Compact) a ver si esto soluciona el problema.

## La inscripción con cena

Supongamos que organizamos un evento cuya inscripción es gratuita. Al finalizar el evento, los asistentes podrán asistir a una cena cuyo precio será de 10 euros. ¿Como puede Symposium ayudarme a organizarlo?

En la opción Inscripción del menú, dentro de la sección Asistentes, encontraremos todo lo necesario para organizar un caso como este, utilizando también la opción Productos.

Primero configuraremos la inscripción al evento. Desde la opción Inscripción, seleccionaremos como Tipo de Inscripción el modo Gratuita. A continuación, podremos definir otros parámetros si los vemos necesarios, como el aforo. Finalmente confirmaremos que en Inscripciones se ha creado una entrada gratuita y que estará disponible en el plazo que nosotros vemos adecuado.

Ahora, en la opción del menú Productos, dentro de la sección Asistentes daremos de alta un nuevo producto que denominaremos "Cena de clausura", por ejemplo. Podremos introducir una breve descripción, una imagen y el precio: 10 euros. Por último, podemos configurar como queremos que nuestros asistentes adquieran la "cena":

- "Uds. en stock" nos permite definir un máximo de aforo, en este caso. Por ejemplo, si nuestra reserva es para 20 personas, pondríamos esa cantidad como stock.
- "Disponible hasta" será útil si queremos cerrar la venta de cenas en un determinado momento. Por ejemplo, si queremos confirmar la reserva del restaurante 3 días antes. De este modo, aunque no se hayan vendido todas las unidades disponibles el producto ya no estará a la venta.
- "Máximo por inscripción" determinará cuantas cenas puede comprar un solo asistente. Si queremos, por ejemplo, que cada asistente pueda traer un acompañante, marcaremos un 2 como máximo. De este modo, cuando una persona se inscriba al evento podrá comprar 2 plazas en la cena, y si inscribiese a 2 personas, podría comprar 4, etc.

Todos estos parámetros son opcionales y pueden dejarse vacíos para que no surtan efecto.

De este modo, tras seleccionar una entrada, los asistentes verán que pueden adquirir una plaza en la cena y la pagarán con su inscripción. Además, desde la sección Productos podremos exportar un fichero Excel con un listado de los inscritos que han comprado la cena para ayudarnos en la organización.

### La inscripción con cena sin utilizar la sección Productos

Supongamos que organizamos un evento cuya inscripción es gratuita. Al finalizar el evento, los asistentes podrán asistir a una cena cuyo precio será de 10 euros. ¿Como puede Symposium ayudarme a organizarlo?

En la opción Inscripción del menú, dentro de la sección Asistentes, encontraremos todo lo necesario para organizar un caso como este, utilizando las opciones Aforo e Inscripciones.

Primero configuraremos la inscripción al evento. Desde la opción Inscripción, seleccionaremos como Tipo de Inscripción el modo De Pago. A continuación, seleccionaremos el aforo del evento, si lo tiene. En nuestro ejemplo, el aforo del evento es ilimitado, aunque solo disponemos de 20 plazas para la cena. Veamos como podemos solventarlo:

- El primer paso, será dejar el aforo del evento como ilimitado.
- A continuación, crearemos una entrada gratuita a nuestro evento y definiremos sus parámetros como convenga.
- Seguidamente crearemos una entrada de pago, con un precio de 10 euros e indicaremos claramente que incluye la cena.
- Como queremos que solo se vendan un máximo de 20 plazas, definiremos como tal la cantidad bajo el mensaje "¿Cuántas?".
- Además, para poder confirmar la reserva con 3 días de antelación, estableceremos el plazo de disponibilidad adecuadamente para que esta entrada no esté disponible pasado el día correspondiente.

Listo. Ahora nuestros asistentes podrán seleccionar simplemente acudir a nuestro evento o adquirir también la cena desde Symposium seleccionando el segundo tipo de entrada. Para nuestra comodidad, desde la opción Listado en la misma sección Asistentes, podremos exportar a Excel el listado de que asistentes han comprado una entrada u otra.

## El formulario de inscripción

Supongamos que organizamos un evento cuya inscripción es gratuita. Al finalizar el evento, los asistentes podrán asistir a una cena que se pagará en el propio restaurante. ¿Como puede Symposium ayudarme a organizarlo?

Para solventar este caso, utilizaremos las Inscripciones y los Formularios de inscripción disponibles en la sección Asistentes.

Primero configuraremos la inscripción al evento. Desde la opción Inscripción, seleccionaremos como Tipo de Inscripción el modo Gratuita. En la parte inferior, en el bloque Inscripciones configuraremos los parámetros que consideremos adecuados para nuestra inscripción. En este ejemplo dejaremos el nombre "Inscripción gratuita" para referirnos a la misma.

A continuación, en la opción Formulario de Inscripción del menú, crearemos una nueva pregunta para nuestra inscripción. Los pasos a seguir serán los siguientes:

- Seleccionamos en el desplegable nuestra inscripción "Inscripción gratuita"
- En el tipo de campo seleccionamos pregunta Si/No.
- En el texto de la pregunta indicamos "¿Asistirá a la cena?"
- Y seleccionamos la casilla "¿Es obligatorio?" que fuerza al usuario a contestar para poder continuar con su inscripción.

Listo. Cuando el usuario se inscriba, mientras introduce sus datos personales, se le preguntará si asistirá a la cena y obligatoriamente deberá responder para poder finalizar su inscripción.

Del mismo modo, podemos añadir una pregunta de tipo texto corto para preguntar cuantos comensales acudirán con el o cualquier otro dato que necesitamos, como si preferirá carne o pescado, por ejemplo.

Desde la opción Listado de la sección Asistentes podremos exportar un fichero Excel con todas las respuestas de nuestros inscritos, para poder gestionar la organización de la cena adecuadamente.

## Aforos por inscripción

Supongamos que organizamos un evento que dispone de dos salas, con distinta capacidad, que queremos completar. En nuestro ejemplo, la Sala A tendrá una capacidad de 45 personas, mientras que la Sala B tendrá una capacidad de 20 personas.

Desde la sección Asistentes, en la opción de menú Inscripción podremos dar de alta dos inscripciones que satisfagan esta casuística. Tras configurar adecuadamente el Tipo de Inscripción nos desplazaremos al bloque Inscripción para iniciar el proceso:

- En primer lugar daremos de alta la "Inscripción para la Sala A" que configuraremos siguiendo nuestras necesidades. En nuestro ejemplo, fijaremos la Cantidad disponible a 45 unidades.
- A continuación daremos de alta la "Inscripción para la Sala B" con sus parámetros correspondientes. Siguiendo el caso del ejemplo, fijaremos la Cantidad disponible a 20 unidades.

Con estos sencillos pasos, el registro en nuestro evento estará limitado a esas dos opciones que a su vez solo estarán disponibles mientras no se cumplan los cupos definidos. Además, desde la sección Asistentes podremos exportar un fichero Excel que nos detallará los datos de nuestros inscritos, con la inscripción seleccionada entre otros datos.

### ¿Y si en el caso anterior además de los límites por sala quisiera limitar el aforo global a solo 45 personas?

Supongamos que en el ejemplo anterior queremos limitar el total de asistentes a 45. Es decir, queremos permitir que sea posible que la Sala A se llene y no haya ningún inscrito en la B. O que si la sala B se llena, solo 25 personas puedan inscribirse en la sala A.

Para lograr este efecto utilizaremos la herramienta Capacidad del evento, disponible en la opción de menú Inscripción dentro de la sección Asistentes.

Una vez dentro de la opción Inscripción, encontraremos el bloque Capacidad del evento en segunda posición. Este bloque nos permite definir el aforo general del evento, a modo de límite total para las capacidades de las distintas inscripciones que hayamos dado de alta.

Simplemente, indicando la cantidad (45 según nuestro ejemplo) conseguiremos limitar el total de asistentes a nuestro evento, aunque el total de las plazas disponibles en cada inscripción sea mayor.

## Gestión de errores en los pagos

Durante el proceso de inscripción la plataforma va almacenando los datos relativos al mismo. Una vez se alcanza el paso final de revisión y hace clic en el botón de Pago o Confirmación se confirman los datos y se guardan como pendientes. A partir de este instante, todos los datos relativos a la inscripción y el pago a recibir se han almacenado correctamente en el sistema.

En el caso de que ocurriese un error inesperado y nunca se recibiese dicho pago, entrarían en funcionamiento varios mecanismos para solventar la situación.

En primer lugar, si el usuario sigue conectado a la web, al intentar volver a inscribirse se detectaría que acaba de realizar una inscripción que no se ha completado. En este momento, se le ofrecería mediante un diálogo la posibilidad de retomar dicha inscripción, cancelarla o iniciar una nueva normalmente, solventando la incidencia in situ.

![](/media/faq/error_overlay.png?align=center)

Además, el sistema ejecutará periódicamente una búsqueda de pagos pendientes. Al localizar uno, enviará al correo indicado como responsable del pago un correo electrónico recordando el estado de la inscripción y el pago pendiente. Ese correo contendrá dos enlaces a la plataforma que permitirán completar o cancelar la inscripción respectivamente. Este envío se realizará a las 5, a las 24 y a las 48 horas de haber iniciado la inscripción.

![](/media/faq/pending_email.png?align=center)

En caso de que el responsable de la inscripción no realice la confirmación o cancelación pertinentes, el sistema cancelará la inscripción automáticamente a las 72 horas.

Cuando se cancele una inscripción de pago, ya sea el usuario manualmente o el sistema automáticamente, no se eliminará ningún dato. En el sistema figurarán las inscripciones de los asistentes tal y como se realizaron pero marcadas como canceladas. Igualmente, el pago, en caso de haberlo, será marcado como cancelado y se indicará si se cancelado manualmente por el usuario o automáticamente por el sistema.

De este modo, quedará constancia de todo el proceso para atender a posibles reclamaciones o incidencias.
