---
title: "Nuevo sistema de plantillas de evento"
weight: 90
lastmod: 2020-02-24T08:33:38Z
dokuwiki: plantillas_responsivas
---
Symposium ofrece un conjunto de plantillas de evento muy flexibles y que proporcionan gran margen de personalización. Son plantillas *responsive* y se adaptan perfectamente a todo tipo de formatos de pantalla, tanto para ordenadores con pantalla grande como dispositivos móviles.

## Principales ventajas

- Las plantillas *responsive *  se adaptan a las resoluciones de los distintos dispositivos: ordenadores, tabletas y smartphones
- Se puede configurar su apariencia en tiempo real, viendo los cambios estéticos en vivo
- Puede crearse una versión específica de una plantilla por evento, permitiendo mayor personalización

## ¿Cómo usar las nuevas plantillas?

### Activación

Las nuevas plantillas *responsive* se pueden **activar** desde el mismo lugar que las anteriores, sección **Diseño > Plantillas,** dentro del menú de edición del evento. Fíjate que tenga el sufijo **-responsive** en el nombre y el **icono multiplataforma**.

![](/media/plantillas_responsivas/icono-responsivo_1.png?align=center)

### Personalización

Una vez seleccionada la plantilla *responsive*, para poder modificar los colores deberemos hacer clic en el botón Ver evento, en la parte alta de la página de edición. En la página del evento que se nos acaba de abrir nos encontraremos en la parte superior izquieda un icono con forma de pincel.

![](/media/plantillas_responsivas/icono-edicion.png?align=center)

Al hacer clic se desplegará un editor de colores. Para **modificar un color**, tan solo tienes que hacer clic sobre la casilla coloreada y se abrirá un editor con un espectro de colores completo. Una vez selecciones tu color arrastrando la cruz hasta el color deseado de la gama y elijas el nivel de brillo del mismo, la plantilla se actualizará para mostrar el resultado de tu selección.

Para dejar de editar los colores haz clic de nuevo sobre el icono del pincel. Si quieres restaurar los colores por defecto, haz clic sobre el icono de restaurar (dos flechas circulares).

![](/media/plantillas_responsivas/personalizacion.png?align=center)

### Imagen de cabecera

Además ahora es posible utilizar imágenes de cabecera sin límite de tamaño. En la sección Diseño > Personalizar podremos subir una imagen y será posible indicar que no queremos recortarla.

![](/media/plantillas_responsivas/cabeceras.png?align=center)

De este modo podemos elegir si queremos utilizar una imagen de cabecera a modo de **logo** o si queremos utilizarla de tamaño grande a modo de **póster**.

![](/media/plantillas_responsivas/distintas-cabeceras.png?align=center)

## ¿Cómo crear una plantilla?

Para crear una plantilla debes descargar una ya existente. Te recomendamos que descargues la plantilla *classic-responsive*  para modificarla acorde con tus requisitos.

Verás que dentro del paquete .zip que descargas existe la siguiente estructura de ficheros:

```
plantilla.zip
    /js
      - script.js
    /less
      - styles.less
    /partials
      - ficheros.ptl
    /templates
      - ficheros.tpl
```

### Javascript

El fichero `/js/script.js`  te permitirá ejecutar tu propio código Javascript.

Para detectar la navegación entre secciones y lanzar código específico para cada una, puedes escuchar el evento `render.handlebars`  de la siguiente forma:

```
     $('body').on('render.handlebars', function (e, template) {
          // tu código
     });
```

La variable `template`  puede tomar los siguientes valores: `abstract, accepted_abstracts, attendees, dates, detail, donations, files, main, news, programme, section, speakers, sponsors, tickets, upload, videos`.

### CSS / less

El fichero `/less/styles.less`  te permitirá modificar los estilos de la plantilla. Podrás utilizar toda la potencia de la tecnología `less`: variables, mixins, etc.

Recuerda que nuestro fichero `main.less`  incluye los estilos necesarios para incorporar Bootstrap como base, entre otros. Puedes consultar todos los componentes y estilos disponibles en la web de [Bootstrap](http://getbootstrap.com/).

### Ficheros Handlebars

Los ficheros .tpl y .ptl son los `templates` y `partials` que utiliza *Handlebars* para renderizar el contenido de la página.

Los ficheros .tpl son las plantillas que se cargan al entrar en cada sección. Puedes modificar su contenido, pero debes respetar los nombres de estos ficheros ya que de lo contrario harás que las distintas secciones del evento dejen de funcionar.

Los ficheros .ptl son los parciales o partials, trozos de código que se pueden renderizar dentro de la página según sea necesario.

#### Estructura

El fichero principal `main.tpl` es el fichero por el que se accede a la página. Es el que contiene la distribución principal de los elementos.

Este es su contenido en la plantilla `classic-responsive`:

```
{{> overlay }}
{{> navbar this }}
<div id="content-wrapper">
    {{> header this }}
    {{> menu this }}
    <div id="content" class="container">
        {{> detail this }}
    </div>
</div>
{{> footer this }}
```

La línea 1 carga el parcial `overlay`. Un parcial se carga con la sintaxis

```
partial append nombre-del-parcial
```

Datos callback permite añadir el contenido de un partial al final del contenido de un elemento del DOM. Datos contiene los objetos necesarios para la correcta carga del parcial. Tras la carga, se ejecuta la función recibida en el método callback.
