---
title: "Documentación recibida"
weight: 4
lastmod: 2024-02-27T21:47:14Z
dokuwiki: comunicaciones_recibidas
---
En Symposium existe un control detallado de la documentación científica de un Evento. Una parte fundamental de esta funcionalidad es la gestión de los documentos que los usuarios que quieren participar envían a los organizadores. Como es sabido, Symposium se adapta a los estándares académicos y para un Evento es posible admitir Abstracts y Comunicaciones. Los primeros son resúmenes de los segundos, que consisten en los trabajos científicos que se quieren presentar en el Evento.

La gestión de la documentación recibida se hace en el menú **Doc Científica** > **Documentación recibida**..

![](/media/panel_organizador/decoumentacion_recibida.png?w=250&align=center)

Si bien la evaluación de estos contenidos la pueden hacer los miembros de la organización, que está compuesta por el Organizador el Evento y los miembros del [Comité Organizador](/docs/eventos/herramientas/comites#comite-organizador), es frecuente que se encargue a un grupo seleccionado de usuarios de la plataforma, que integrarán el [Comité Científico](/docs/eventos/herramientas/comites#comite-cientifico).

Los usuarios remiten documentos al Evento -sean Abstract, sean Comunicaciones- y deben asociarlos a una [Temática](/docs/eventos/doc-cientifica/recepcion-comunicaciones#tematicas). Estas tienen designado un Responsable, quien recibirá un email de aviso por cada documento que se reciba. Si no hay un Responsable designado, será el propio Organizador quien reciba todos esos mensajes de aviso.

Es posible consultar un listado completo de los correos electrónicos que genera Symposium en [Comunicaciones por correo electrónico](/docs/introduccion/comunicaciones-por-correo-electronico).

## Activar la Revisión anónima

Al principio de esta sección hay un check que puede ser interesante activar, a criterio de los Organizadores, para activar la opción de anonimato de los documentos. Si se activa, los Revisores nunca podrán ver quién es el autor de los documentos que tienen que evaluar. Esta funcionalidad resulta valiosa en Eventos de carácter científico.

![](/media/panel_organizador/anonimo.png?w=750&align=center)

## Botones para exportar el contenido

A continuación, esta página se organiza en dos pestañas, una mostrará la colección de Abstracts que se hayan recibido en orden de Temáticas, la otra mostrará en el mismo orden las Comunicaciones.

En la parte superior de cada pestaña hay dos botones:

- **Exportar a Excel**: permite obtener un documento con el contenido completo de los documentos en formato entendible por varios tipos de aplicaciones, como hojas de cálculo o navegadores web, y todos los demás campos que los autores hayan tenido que rellenar para enviarlos. Para obtener esta información será necesario aceptar expresamente una cláusula de protección de datos.
- **Descargar Zip**: permite obtener un fichero de archivo de tipo Zip con los documentos que haya en una Temática a escoger. Los usuarios que quieran obtener estos documentos estarán limitados por los permisos que los organizadores les hayan proporcionado. Si se quieren obtener documentos de varias Temáticas, se deberá repetir el proceso tantas veces como Temáticas haya.

![recepciondocumentaciondescargarexcel.jpg](/media/doc-cientifica/recepciondocumentaciondescargarexcel.jpg?w=245&align=center)![recepciondocumentaciondescargarzip.jpg](/media/doc-cientifica/recepciondocumentaciondescargarzip.jpg?w=245&align=center)

## Filtro de contenidos

En ocasiones, la documentación científica para un Evento se hace muy numerosa y el listado, muy largo. Es posible organizar ese contenido mediante los elementos de filtrado:

- Estado de validación: muestra sólo los documentos que estén Pendientes, Aceptados o Rechazados
- Ordenar por: Título (se ordenaría alfabéticamente), Identificador (número de orden de cada documento, Fecha
- Temática: a elegir entre las disponibles
- Ascendente o Descendente (para cuando se elija ordenar alfabéticamente)

![](/media/panel_organizador/filtro_contenidos.png?w=750&align=center)

Además de los campos de filtrado de la lista, hay un cuadro para escribir términos concretos a buscar entre la documentación y su correspondiente botón Buscar.

## Listado de documentos

### Abstracts

El listado de Abstracts se organiza por Temáticas o Categorías. En primera instancia, se muestra un listado resumido y por cada Abstract se muestra:

- **ID**: un número de orden
- **Título**
- **Autor**, cuando no esté activa la [Revisión anónima](/docs/eventos/doc-cientifica/comunicaciones-recibidas#activar-la-revision-anonima)
- **Puntuación y número de valoraciones recibidas**, siempre que ya haya recibido alguna y en función de si hay más de un Revisor asignado al Abstract
- **Contactar**: para enviar un email al autor
- **Botón +**: despliega el contenido visible del Abstract que a su vez muestra:
      - ***Fecha** *
      - ***Tipo de documento** *
      - ***Formulario +***  . que despliega los campos personalizados que se indicaron en el Formulario de subida
      - ***Contenido***  del Abstract
      - ***Valoración***  , por Rango (lista desplegable) o por [Valoración por Rúbrica](/docs/eventos/doc-cientifica/valoracion-rubrica) (botón que abre un panel con los criterios y niveles diseñados previamente)
      - ***Asignar la valoración a Revisores***  , cuando esté activa la Revisión individual en la Temática; si ya ha sido valorado por todos los asignados, muestra la puntuación que ha obtenido el trabajo
      - ***Estado***  : para determinar si el documento se aprueba, se rechaza o se mantiene en espera
      - ***Comentarios***  : para añadir comentarios públicos y moderar los que existan, si están activados para la Temática
      - ***Eliminar envío***  : para borrar por completo el Abstract
      - ***Cambiar categoría***  : para asignar el Abstract a otra Temática, si fuese pertinente
      - ***Editar envío***  : para mostrar el formulario de envío del Abstract en la web del Evento con la posibilidad de modificarlo

### Comunicaciones

Muy parecido al panel de Abstracts, inicialmente se organiza por Temáticas o Categorías. Se muestra un listado abreviado de Comunicaciones con:

- **ID**: un número de orden
- **Título**
- **Autor**, cuando no esté activa la [Revisión anónima](/docs/eventos/doc-cientifica/comunicaciones-recibidas#activar-la-revision-anonima)
- **Puntuación y número de valoraciones recibidas**, siempre que ya haya recibido alguna y en función de si hay más de un Revisor asignado a la Comunicación
- **Botón +**: despliega el contenido visible del Abstract que a su vez muestra:
      - ***Fecha** *
      - ***Tipo de documento** *
      - ***Formulario +***  . que despliega los campos personalizados que se indicaron en el Formulario de subida
      - ***Descargar***  para obtener el fichero con la Comunicación
      - ***Valoración***  , por Rango (lista desplegable) o por [Valoración por Rúbrica](/docs/eventos/doc-cientifica/valoracion-rubrica) (botón que abre un panel con los criterios y niveles diseñados previamente)
      - ***Asignar la valoración a Revisores***  , cuando esté activa la Revisión individual en la Temática; si ya ha sido valorado por todos los asignados, muestra la puntuación que ha obtenido el trabajo
      - ***Estado***  : para determinar si el documento se aprueba, se rechaza o se mantiene en espera
      - ***Comentarios***  : para añadir comentarios públicos y moderar los que existan, si están activados para la Temática
      - ***Añadir actividad***  : permite convertir una Comunicación en una entrada del Programa del Evento sin tener que pasar por el menú Contenido > Programa.
      - ***Eliminar envío***  : para borrar por completo la Comunicación
      - ***Cambiar categoría***  : para asignar la Comunicación a otra Temática, si fuese pertinente
      - ***Descargar Abstract***  : ofrece en descarga el Abstract de esa Comunicación
      - ***Editar envío***  : para mostrar el formulario de envío de la Comunicación en la web del Evento con la posibilidad de modificarla

## Algunas funciones comunes para Abstracts y para Comunicaciones

- **Cambiar Estado del documento**  (siempre se cambia manualmente)**:**
      - ***Aceptado***  : el documento quedará aprobado como contenido oficial del Evento. Para un Abstract significa poder, además, enviar la correspondiente Comunicación
      - ***Rechazado***  : lo contrario de lo anterior, el documento no formará parte del Evento. Para un Abstract supone la imposibilidad de enviar su correspondiente Comunicación.
      - ***Pendiente***  : queda a la espera de revisión posterior
- **Puntuar**: relacionado con las dos primeras, pero no de forma automática. Un Revisor puede evaluar un documento según se haya configurado, mediante [Rango](/docs/eventos/doc-cientifica/recepcion-comunicaciones#valoracion-por-rango) o por [Rúbrica](/docs/eventos/doc-cientifica/recepcion-comunicaciones#valoracion-por-rubrica).
- **Descargar**el documento
- **Ver y publicar comentarios**, cuando esté configurado para su Temática que se acepten [Comentarios públicos](/docs/eventos/doc-cientifica/recepcion-comunicaciones#tematicas)
- **Asignar Revisores**, cuando se haya configurado para su Temática la [Revisión individual](/docs/eventos/doc-cientifica/recepcion-comunicaciones#tematicas)

![](/media/doc-cientifica/listadoabstracts.png?w=640&align=center)

- **Asignar la valoración a un Revisor:**para asignar individualmente la evaluación de un documento a un Revisor, primero debe estar activada la opción de Revisión individual en la [Temática](/docs/eventos/doc-cientifica/recepcion-comunicaciones#tematicas) a la que corresponda el documento y debe haber como mínimo dos Revisores para esa Temática entre los cuales escoger. Además, debe existir un [Método de valoración](/docs/eventos/doc-cientifica/recepcion-comunicaciones#configuracion-de-valoraciones) definido allí mismo.

![absval.jpg](/media/doc-cientifica/individual_reviewers.png?w=625&align=center)

Si un trabajo ya tiene Revisores individuales asignados, se mostrará una lista de ellos. El Organizador del evento podrá, además, ver la puntuación que ha dado cada uno de ellos. Los demás Revisores no pueden ver lo que puntúan los demás. Las valoraciones individuales también se detallan en el fichero de exportación y, de nuevo, sólo están visibles para los Organizadores.

Para asignar un Revisor o varios, marca sus correspondientes casillas de check y haz clic en Añadir revisores. Si más adelante quieres añadir otros Revisores, en el listado sólo aparecerán los que tengan la temática de ese documento y aún no sean Revisores de este en concreto.

Para retirar Revisores asignados a un documento, simplemente haz clic en el botón Borrar. Sólo puedes quitarlos de la asignación a ese documento cuando no hayan emitido aún una valoración. Si han evaluado, el botón Borrar ya no estará disponible.

- **Moderar comentarios**: sólo los miembros del Comité científico tienen la posibilidad de moderar los comentarios de las comunicaciones, siempre que estos se hayan activado en las correspondientes Temáticas. Se puede añadir un Comentario o Mostrar los que ya existan. Estos comentarios públicos se muestran y se gestionan directamente en el front del Evento, nunca en el Backoffice.

![](/media/panel_organizador/comentarios_doc.png?w=150&align=center)

La funcionalidad de registrar anotaciones en forma de comentarios está disponible en dos modalidades, entre las que se elige al marcar o dejar desmarcada la opción "Este comentario es una nota interna". Por defecto, los comentarios son Notas internas y los autores científicos no recibirán ningún aviso sobre ello.

![](/media/doc-cientifica/sci_comentarios.png?w=320&align=center)Al hacer clic sobre el botón Comentar, se despliega el editor para nuevos comentarios. El editor permite algunas reglas de estilo, negritas, cursivas, listas ordenadas y enlaces a otras páginas.

Por defecto, los comentarios son una nota interna.

Si se desactiva el check "Este comentario es una nota interna", entonces se enviará un email al autor con el comentario, el cual, además, quedará grabado.

El botón Mostrar despliega la lista de los comentarios asociados al trabajo que se ha recibido. Todos los comentarios sobre un trabajo están visibles para los organizadores del evento, los miembros de comités con acceso a la documentación, incluido el Comité científico y los Revisores que pueden leer cada documento.

- **Eliminar envío**: esta acción no es reversible. Una vez eliminado un documento no se puede recuperar.

## Acción específica de las Comunicaciones: añadir al Programa

En un Evento puede ser interesante que una Comunicación recibida pase a formar parte del Programa. Es habitual en Eventos científicos y ahorra trabajo en la gestión. Cuando se acepta una Comunicación, se puede hacer clic en el boton Añadir actividad. Aparecerán unos controles que permiten agregar sobre la marcha una actividad al Programa del Evento sin tener que visitar expresamente el menú Contenido > Programa.

![](/media/panel_organizador/anadir_al_programa.png?w=750&align=center)Además, la aplicación Symposium escribirá el título de la actividad directamente copiado del título de la Comunicación, aunque se podrá modificar. Se deben indicar fechas de inicio y fin y una descripción. En Eventos multi idioma sólo se guardarán las fechas para los demás idiomas. El título y la descripción deberán modificarse manualmente en el Programa de cada Evento en la correspondiente versión de cada lengua.
