---
title: "Listado de asistentes"
weight: 6
lastmod: 2026-07-31T08:48:25Z
dokuwiki: listado
---
Un Organizador necesitará hacer gestión de los asistentes a un Evento, especialmente cuando la asistencia requiera de validación. Cuando es así, es posible aceptar o rechazar inscripciones de forma individual o afectando a un grupo seleccionado de ellas. También es posible revocar estas decisiones en un sentido o en el opuesto. Incluso es posible rechazar inscripciones que tengan carácter de validación automática y revocar esa decisión después, si es preciso.

Además de las habituales tareas de gestión de asistentes, con esta utilidad es posible obtener un listado de los asistentes, tanto los que están confirmados como los que han sido rechazados, así como los que han cancelado su inscripción de forma voluntaria en su panel privado.

![](/media/listado/listado_asistentes.png?w=250&align=center)

## El panel del Listado de asistentes

Hay tres secciones en este panel:

- **Filtros**para localizar asistentes concretos o grupos de asistentes
- **Asistencias activas**  con indicación de estado (confirmado, rechazada o pendiente)
- **Asistencias canceladas**  por parte de los inscritos desde su panel privado

## Filtrando la lista de asistentes

Aquí puedes consultar la lista de asistentes al Evento y la puedes ordenar por nombre o fecha de inscripción, o bien aplicar filtros con los campos de búsqueda para tener a la vista sólo un conjunto de ellos. Es útil sobre todo si la lista se hace muy larga. Además, si el Evento es de pago, también se podrá aplicar un filtro por el estado de este (confirmada, pendiente o cancelada).

![](/media/panel_organizador/listado_de_asistentes_filtros.png?w=750&align=center)

En la cabecera de esta caja de filtros existen los botones para hacer exportación del listado, tanto en formato imprimible como en hoja de cálculo.

## La información disponible en el listado de asistentes

Según cómo se hayan diseñado las Inscripciones, el listado tendrá un aspecto u otro. La principal diferencia la establecen las Inscripciones "Con Validación" ya que esa acción de validar la realiza el Organizador en este mismo panel.

![](/media/listado/listado_de_pago.png?align=center)

En un **Evento de pago sin validación**, la inscripción tiene el mismo estado que el pago porque al llegar este, se confirma al asistente automáticamente. No se requiere intervención manual del Organizador.

![](/media/listado/listado_free.png?align=center)

En un **Evento gratuito con validación**  no existe control de estado del pago, pero sí se requiere una confirmación manual de la asistencia en este panel. Así, junto al estado de la inscripción se muestran dos botones que permiten **aceptar**  y **rechazar**  al solicitante. Nótese que es posible rechazar a un asistente al que se había aceptado previamente y viceversa.

![](/media/listado/listado_validacion.png?align=center)

Por último, puede existir un Evento con Inscripciones que requieran validación y sean de pago. Aquí, independientemente del estado del pago se puede aceptar o rechazar la inscripción. Esta configuración puede ser útil cuando se quiere comprobar las credenciales de los asistentes antes de admitirlos en el Evento, de modo que cumplan ciertos requisitos.

![](/media/listado/listado_datos_extra.png?align=center)

Haciendo clic en el icono con el símbolo +, se despliega la información adicional de una Inscripción. Se muestra la fecha en la que se hizo y la visibilidad de la misma. En los detalles se muestran el correo de contacto del usuario que ha comprado la inscripción, el identificador de la transacción y el estado del pago.

Si el asistente confirmó compras de [Productos](/docs/eventos/asistentes/productos-relacionados) en el proceso de Inscripción, aparecerán también relacionados en esta tabla.

Finalmente se muestran las respuestas del asistente en el [Formulario de inscripción](/docs/eventos/asistentes/formulario-de-inscripcion), si se hubiesen personalizado campos e incluso existe la opción de modificar esas respuestas desde este panel.

## Modificar nombre de asistentes

Desde el listado de asistentes, el Organizador puede modificar el nombre y los apellidos de cualquiera de ellos.

Para realizar este cambio, basta con hacer clic en el icono del lápiz (**Modificar nombre**), situado junto al asistente que se desea editar:![](/media/listado/modificar1.png?w=700&align=center)A continuación, se abrirá una ventana en la que será posible actualizar los campos Nombre y Apellidos. Una vez realizados los cambios, hay que hacer clic en **Guardar** para confirmar la modificación:

![](/media/listado/modificar2.png?w=700&align=center)

## Exportando la información

Haz clic en el botón "Imprimir/Exportar a Excel" para imprimir el listado de asistentes, o para exportarlo en formato de Excel para compartirlo o guardar una copia.

Al utilizar esta opción se abrirá una nueva pestaña del navegador en la que se pueden indicar qué campos se quieren incluir en la exportación. Tras seleccionar cómo quieres compartirlo, haz clic en "Exportar a Excel" o "Imprimir" para realizar la acción deseada.

![](/media/listado/listado.png?w=903&align=center)

## Significado de los iconos

En el listado de asistentes aparecen distintos iconos dependiendo de la configuración del registro de asistentes y del estado de la inscripción.

**Sin iconos:**cuando el evento es gratuito, el listado de asistentes no muestra iconos, ya que el estado de la inscripción no depende de ningún pago.

![](/media/admin/no_aplicable.png?w=16)**No aplicable:**este icono indica que no hay ningún pago asociado al asistente porque, a pesar de que el evento sea de pago, la inscripción está configurada como gratuita.

![](/media/panel_organizador/pendiente.png?w=16)**Pendiente:**representa que el pago de la inscripción del usuario no se ha efectuado, por lo que permanece en estado pendiente.

![](/media/panel_organizador/accept.png?w=16)**Aceptado**: indica que el pago de la inscripción ha sido efectuado por parte del usuario y validado.

![](/media/panel_organizador/cancel.png?w=16)**Cancelado**: cancelación de la inscripción por parte del propio usuario.

![](/media/panel_organizador/rechazado.gif?w=16)**Rechazado**: indica que el organizador ha rechazado la asistencia del usuario al evento.
