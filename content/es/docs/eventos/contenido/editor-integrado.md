---
title: "Editor integrado"
weight: 90
lastmod: 2023-03-20T10:06:32Z
dokuwiki: editor_integrado
---
En la gestión de contenidos de los websites de evento en SYMPOSIUM es frecuente encontrar un editor, desde el formulario de creación de nuevo evento hasta las distintas secciones que permiten contenido libre.

Hay dos modos de usar el editor: el modo estándar, que permite usar botones para aplicar estilos al texto e insertar elementos de imagen o vídeo, similar al uso de un procesador de textos como Word; y el modo Fuente HTML, que permite escribir o pegar el código HTML de la página que se quiere mostrar. El primer modo es el estándar y se puede alternar entre ellos con el botón Fuente HTML.

La mayoría de usuarios de la plataforma, cuando crean y gestionan eventos, preferirá usar el modo estándar.

![](/media/creando_un_evento_nuevo/ckeditor202303.png?w=805&align=center)

Es posible escribir directamente en el editor y aplicar estilos habituales para el texto, como el color de la fuente y el color del fondo, poner el texto en negrita, cursiva y subrayado. Hay botones para formatear texto como listas numeradas o sin orden fijo y para alinear párrafos.

Además de lo anterior, hay botones específicos para crear contenidos de páginas web, tales como insertar enlaces en el texto, añadir imágenes, tablas, símbolos, vídeos, o contenidos que están en otros websites. Se describen a continuación.

## Botones de formato rápido y botón para eliminar formato

Como en un procesador de textos, el editor proporciona varios botones para aplicar estilo rápido y sencillo a los textos seleccionados. Se trata de los botones para texto en negrita, cursiva, subrayado simple, tachado, y texto en subíndice o superíndice.

![](/media/creando_un_evento_nuevo/ckeditor202303basicformat.png?w=805&align=center)

Hay un botón específico para limpiar el formato del texto seleccionado. Puede resultar muy útil para escenarios en que se ha copiado y pegado contenido desde un procesador de textos como Word, o desde otras páginas web. Estos textos suelen llevar código de estilo propio que, a veces, descuadra la página que se está creando. Se hace difícil de arreglar sin acceder al modo de edición HTML.

![](/media/creando_un_evento_nuevo/ckeditor202303cleanformat.png?w=805&align=center)

## Insertar imagen

Abre un cuadro de diálogo con los campos necesarios para incluir una imagen en el contenido. Es importante tener en cuenta que la imagen debe ser un fichero subido al servidor del evento, o bien que esté en otro servidor público de Internet. Si se copia y se pega desde un documento de Word, la imagen no se mostrará luego en la web del evento porque el servidor de SYMPOSIUM no podrá acceder a ella.

![](/media/creando_un_evento_nuevo/insertar_imagen_1.png?w=732&align=center)

Si la imagen que se quiere mostrar está en el ordenador de quien edita, tendrá que subirla al servidor de SYMPOSIUM. Para eso, debe usarse el botón Ver servidor. Mostrará una lista de ficheros que ya estén subidos, si los hay, y la posibilidad de subir otros. Bastará con hacer clic en el fichero que se quiere mostrar, siempre que sea una imagen y se rellenará el campo URL. Conviene incluir un Texto Alternativo para mejorar la accesibilidad de la web y completar, opcionalmente, los demás campos.

## Insertar tabla

Es parecido al anterior. Consiste en indicar cuántas filas y columnas tendrá, además de otros atributos estándar que el lenguaje HTML establece para definir las tablas. Estos atributos se pueden cambiar después. Es posible hacer clic con el botón secundario del ratón sobre la tabla en el propio editor para obtener un menú de opciones para modificarla.

![](/media/creando_un_evento_nuevo/insertar_tabla.png?w=738&align=center)

## Insertar un contenido que está en otra web

Hay dos botones para insertar contenidos de otras webs. En HTML, estos elementos se denominan iframes y, estrictamente, es una forma de incrustar en una página web otra página que puede estar en cualquier otro website de Internet. Es frecuente usar esto para insertar elementos multimedia de otros proveedores, como vídeos de Youtube, o presentaciones online como Genialy.

![](/media/creando_un_evento_nuevo/insertar_iframe.png?w=768&align=center)

Uno de los botones permite editar los atributos del iframe, con todo detalle. El otro botón sólo requiere introducir la URL del contenido que se quiere enlazar y genera automáticamente los atributos del iframe. Si bien es posible usar estas herramientas para insertar vídeos de Youtube, hay una específica para esto que lo hace igual y, además, genera contenido responsive, de modo que el navegador sabrá redimensionar el vídeo para que encaje bien en pantallas de distintas dimensiones.

![](/media/creando_un_evento_nuevo/insertar_video_responsive.png?w=737&align=center)

Este botón muestra un panel que sólo pide la URL del vídeo y definir sus proporciones. Los vídeos más modernos suelen tener proporción 16/9. Los más antiguos, como los viejos televisores de tubo, tienen proporción 4/3.

### Insertar vídeos responsive desde Youtube

Es importante saber desde dónde se debe obtener el enlace del vídeo que se quiere insertar. Si se quiere un vídeo responsive, no servirá copiar y pegar la dirección web del vídeo. En su lugar, hay que obtenerla en Youtube siguiendo estos pasos:

1. Clic en Compartir
1. Seleccionar de entre todas las opciones "Insertar"
1. Del bloque de código que aparece, seleccionar y copiar la dirección entrecomillada del campo src
1. Pegar esa URL en el campo.

| |
|---|
| ![](/media/creando_un_evento_nuevo/insertar_video_responsive_01_compartir.png?w=774&align=center) |

| |
|---|
| ![](/media/creando_un_evento_nuevo/insertar_video_responsive_02_insertar.png?w=529&align=center) |

| |
|---|
| ![](/media/creando_un_evento_nuevo/insertar_video_responsive_03_copiar.png?w=1025&align=center) |
