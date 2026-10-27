---
title: "Formulario de subida de Documentación científica"
weight: 3
lastmod: 2021-11-26T10:13:14Z
dokuwiki: formulario_subida
---
El proceso de envío de Documentación científica por parte de los usuarios se hace desde un formulario en la web del Evento, según se trate de Abstracts o de Comunicaciones. Este formulario está definido por el sistema de Symposium con unos componentes predeterminados, pero es posible añadir más controles o eliminar algunos de los que aparecen por defecto. La definición de un Formulario de subida de documentación se hace desde el menú **Doc Científica** > **Formulario de subida**.

![](/media/panel_organizador/formulario_cientifica.png?w=250&align=center)

Al entrar en esa página, se ofrecen una serie de controles para añadir funcionalidad al Formulario de subida y más abajo una lista de los campos que ya hay en él.

## Campos actuales

Inicialmente, se presenta un cuadro con el título Autores y una relación de los campos que se mostrarán en todos los formularios de subida. Hay dos que son siempre obligatorios, más otros tres que en principio salen, pero se pueden ocultar:

- **Nombre completo del autor**: obligatorio;
- **Correo de contacto del autor**: obligatorio;
- **Nombre público del autor**: opcional, activado por defecto;
- **Identificador ORCID**: opcional, activado por defecto;
- **Filiación del autor**: opcional, activado por defecto.

La información que los aspirantes escriban allí será visible para los Revisores. Si se necesita que esté oculta para una Evaluación anónima, hay que activar una opción que aparece en otro menú, **Doc Científica**  > **Documentación recibida**.

![](/media/panel_organizador/formulario_cinetifica_2.png?w=750&align=center)

Se pueden ocultar campos simplemente marcando el check correspondiente a ellos en la columna "¿Oculto?". Esos campos por defecto no se pueden modificar. Si se precisa otra funcionalidad, se deben ocultar y crear campos nuevos que hagan lo que se necesite.

## Crear Nuevo campo

### Configuración multi idioma

La creación de un nuevo campo en cualquier de los idiomas afecta siempre a todos los idiomas del Evento porque se hacen tantas copias copias como idiomas haya. Sin embargo, deberás traducir su configuración a cada idioma por separado. Si no lo haces, en todos aparecerá con el texto del idioma en que originalmente lo hayas creado.

Por otra parte, la modificación de un campo en un idioma no afecta en absoluto a los demás. De este modo es posible hacer la traducción y adaptación de cada uno.

### Personalización de un campo

Es posible crear un campo que aparezca en dos o más Categorías, pero no en todas. Para ello, se debe crear una sola vez y vincularlo a una Categoría. Después, localizarlo en la tabla de campos y hacer clic en el botón Copiar. La aplicación preguntará en qué otras Categorías se necesita que aparezca.

Los campos personalizados se pueden modificar o eliminar, para lo cual existen botones específicos.

El proceso de crear nuevos campos para el Formulario de subida consiste en:

1. **Vincularlo una Categoría**: el nuevo campo sólo aparecerá para documentos que se quieran subir a una Categoría o Temática determinada. Si se elige Autores, saldrá siempre en todas las Categorías, si bien la respuesta sólo será visible en eventos que no tengan activa la Revisión anónima.
1. **Elegir el tipo de campo**:
      1. Pregunta con texto corto
      1. Pregunta con texto largo
      1. Pregunta Sí/No
      1. Selección de una opción
      1. Selección múltiple
      1. Fecha
      1. Fichero adjunto
      1. Selección de país: es una lista desplegable con nombres de países en orden alfabético
      1. Texto de ayuda: este último no es un campo a rellenar, sino que permite al Organizador mostrar texto en el Formulario de subida de documentación para ayudar a los usuarios si lo pueden necesitar.
1. **Configurar el tipo de campo elegido**: en función de qué tipo de campo se añade, habrá que poner un texto a modo de título y puede que establecer una serie de opciones entre las que elegir o un botón para subir documentos.

### Opciones adicionales

Al marcar el check ¿Obligatorio? se impide que el visitante de la web envíe documentos sin haber antes cumplimentado ese campo.

La opción ¿Ocultar esta pregunta al autor? hace que no sea el visitante quien deba cumplimentar el campo, sino el propio Organizador sin que el visitante tenga necesariamente que saberlo. Es útil para hacer anotaciones internas del tipo "Es asistente VIP" o algo parecido.

Si se crea un nuevo campo vinculado exclusivamente a una Categoría o Temática, sólo se hará visible cuando el visitante que quiere enviar un documento seleccione dicha Categoría en la web del Evento.
