---
title: "Formulario de inscripción"
weight: 4
lastmod: 2024-02-27T21:49:49Z
dokuwiki: formulario_de_inscripcion
---
Por defecto, los datos mínimos que se requieren para poder realizar una inscripción son el nombre, apellidos y correo electrónico del asistente. Estos datos son necesarios y comunes a todos los eventos que tienen configurado registro de asistentes. Adicionalmente, puedes requerir otros datos o textos de ayuda para notificar algo los asistentes. Symposium ofrece la posibilidad de crear formularios de inscripción personalizados con diferentes tipos de preguntas. Esto puedes hacerlo desde la sección **Asistentes > Formularios de inscripción**.

![](/media/panel_organizador/formulario_de_inscripcion.png?w=250&align=center)

## El panel Formularios de inscripción

La página Formularios de inscripción se organiza en dos áreas diferenciadas. En la parte superior se muestran controles para añadir nuevos campos a una determinada inscripción. En la parte inferior se muestran tablas con los campos que se han diseñado para mostrar en las distintas Inscripciones, siempre que ya se haya configurado alguno.

![](/media/panel_organizador/ejemplo_formulario_inscripcion.png?w=750&align=center)

## Creación de un campo para el formulario de inscripción

Los formularios de inscripción son una serie de preguntas personalizadas por el organizador del evento y que el asistente tiene que cumplimentar en el proceso en que realiza la inscripción al evento.

Los tipos de preguntas disponibles son:

- **Pregunta con texto corto:**  recomendada cuando se espera una respuesta breve.
- **Pregunta con texto largo:**  recomendada cuando se espera una respuesta extensa.
- **Pregunta de Sí o No**
- **Texto de ayuda:**  se muestra un texto de aviso, en formato de texto de ayuda para informar al usuario sobre algo.
- **Pregunta de fecha:**este control se presenta en forma de calendario a fin de que el usuario seleccione una fecha.
- **Selección de una opción:**  el asistente debe elegir una opción entre las disponibles.
- **Selección múltiple:**  el asistente debe elegir una o más opciones entre las disponibles.
- **Fichero adjunto:**  este control habilita un botón para enviar al Evento un fichero.
- **Selección de un país:**  es una lista alfabética de países.

Supongamos un Evento en el que, para datos estadísticos, se desea conocer la edad de los Asistentes. Para ello, se personaliza un formulario de inscripción.

Primero, se debe elegir a qué tipo de Inscripción se asociará el campo, a elegir del listado Inscripción. Cabe pensar que la pregunta se hará a todos los inscritos sin importar qué entrada vayan a comprar. Symposium facilita esto creando un campo asociado a un tipo de Inscripción que luego se puede copiar para las demás, de modo que no hace falta repetir el proceso una y otra vez.

Después, se elige el tipo de campo de la lista que se expone en el apartado anterior a este párrafo. En función de lo que se quiera preguntar, a la derecha aparecerán unas opciones u otras. En el caso de un campo de tipo Fecha tan sólo hay que indicar un texto amable para la pregunta. Cuando se ofrecen opciones, habrá que escribirlas a mano una a una.

![](/media/panel_organizador/crear_preguntas.png?w=750&align=center)

A continuación se debe elegir si se activan o no tres opciones, independientes unas de otras.

- **¿Es obligatorio?**: hace posible marcar el campo como obligatorio, para lo cual hay que marcar un check y el Inscrito sólo podrá confirmar la compra de su entrada después de haber respondido a la pregunta del campo.
- **¿Ocultar esta pregunta al asistente?**: se trata de una opción que oculta el campo al usuario que quiere comprar una entrada, pero que posteriormente sí tendrá que rellenar el Organizador. Se ha diseñado para almacenar cierto tipo de información necesaria para el Evento, pero que no se pregunta a los Asistentes. Por ejemplo, si tiene título de Doctor o si es un invitado especial del Rectorado de la universidad.
- **¿Mostrar esta pregunta en el listado de asistentes?**: permite decidir si la respuesta sale o no en el [listado de asistentes](/docs/eventos/asistentes/listado) que se puede obtener para el control del Evento.

En el ejemplo de la fecha de nacimiento, se ha decidido que el campo sea obligatorio, pero no se ocultará a los asistentes, puesto que son ellos quienes deben rellenarlo y se marcará la opción de mostrarlo en los listados porque es útil para el Organizador.

En los Eventos multi idioma, los formularios se replican para cada versión de la web del Evento, pero es necesario traducir y adaptar los textos en cada una de las versiones.

## Duplicar una pregunta para otras Inscripciones

Es posible que una misma pregunta se quiera incluir en todas o algunas inscripciones. Symposium permite crear el campo una sola vez asociado a un tipo de entrada y después copiarlo para las demás, de modo que se evita tener que crear el campo una y otra vez tantas veces como entradas haya.

![](/media/panel_organizador/clonar_preguntas.png?w=450&align=center)

Para duplicar un campo de formulario, se localiza en las tablas de la mitad inferior de este panel y se hace clic en el botón Copiar. Se mostrará un cuadro en el que se pueden marcar qué tipos de entrada y de donación deben mostrar ese campo.

## Ordenar campos del formulario

Cuando se crean varios campos personalizados para un tipo de entrada, es importante el orden en que aparecerán en pantalla al usuario. Esto se controla en el propio panel Formularios de inscripción, en las tablas de la parte inferior. Si bien el orden inicial se determina en función del orden de creación de campos, se puede modificar usando la técnica de arrastrar y soltar del ratón.

La animación que se muestra más abajo expone cómo se cambia el orden de los campos de un formulario de inscripción.

![](/media/formulario_de_inscripcion/dragdrop_form.gif?align=center)

## Traducción de las preguntas del formulario a otros idiomas

Symposium es una plataforma [multi idioma](/docs/eventos/herramientas/activar-modo-multi-idioma) que permite traducir los contenidos hasta en cinco idiomas diferentes. Las preguntas del formulario personalizado pueden traducirse, una vez creadas, seleccionando el idioma en el que quieras editar el evento.

Hay que tener en cuenta que, aunque esté traducido, el formulario debe ser el mismo y presentar las mismas opciones para todos los idiomas, de modo que en las preguntas del tipo selección de una / varias opciones, deben tener el mismo número de respuestas para que sea posible trazar una continuidad. En el caso de que se elimine o añada una nueva respuesta solo para uno de los idiomas, esta modificación afectará al resto de versiones.
