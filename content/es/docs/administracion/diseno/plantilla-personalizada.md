---
title: "Plantilla personalizada"
weight: 2
lastmod: 2023-04-21T12:28:29Z
dokuwiki: plantilla_personalizada
---
Las plantillas definen la parte visual de la web del evento. Dependiendo de la plantilla que se utilice para el evento, dispondrá de una maquetación distinta, localización de los botones, colores, tamaño y tipografía de las fuentes, etc.

Symposium ofrece varias plantillas por defecto, ya diseñadas y listas para su activación. a pesar de ello, estas plantillas son perfectamente personalizables. Desde esta sección, puedes descargar un kit para crear tus propias plantillas personalizadas. Dentro del archivo, encontrarás un documento con toda la información que puedas necesitar para crear tu plantilla.

Para personalizar estas plantillas haz clic en la opción *Plantilla personalizada* que encontrarás en el apartado *Diseño*.

![](/media/admin/personalizar_plantillas.png?w=250&align=center)

## Bajar plantilla de sistema

En este panel podrás encontrar todas las plantillas disponibles de la plataforma. Escoge la plantilla que quieras modificar a tu gusto y descárgala. Algunas plantillas tienen variantes según el color base.

![](/media/admin/plantillas_admin.png?w=500&align=center)

**Plantillas responsive (uso recomendado)**

El paquete comprimido que has descargado contiene una estructura de carpetas y un fichero README.txt con instrucciones y especificación de dónde está cada cosa.

**Plantillas classic (uso no recomendado)**

El paquete comprimido que has descargado contiene un fichero *tpl* con la estructura de la plantilla, dos ficheros de texto con instrucciones, uno en español y otro en inglés, y directorios para localizar ficheros JavaScript y CSS personalizados.

![](/media/admin/captura_de_pantalla_2013-03-21_a_la_s_11.35.48.png?align=center)

## Modificar plantilla de sistema para convertirla en plantilla personalizada (sólo Plantillas Responsive)

### Directorio assets

Es el directorio que te recomendamos para incluír las imagenes que veas necesarias. Si necesitas hacer referencia a una imagen dentro de un partial o un template hazlo de forma relativa:

```
<font inherit/Courier New,Courier,monospace;;inherit;;inherit><img src="{{template_path}}assets/ficheros.png" /></font>
```

**Directorio js**

Dentro de este directorio debes incluir tus ficheros Javascript. El fichero script.js se incluye automáticamente (es **importante** que no le cambies el nombre). El método que te recomendamos para ejecutar código en el evento "document ready" es el que figura en este archivo.

Si necesitas ejecutar código después de que se cargue un fichero partial o template, debes escuchar al evento "render.handlebars" que se lanza sobre body. Ejemplo:

```
<font inherit/Courier New,Courier,monospace;;inherit;;inherit>$('body').on('render.handlebars', function (e, template) {
// template contiene el nombre del bloque cargado, sea ptl o tpl
});</font>
```

Si necesitas cargar otros ficheros Javascript te proveemos de un método que los carga de forma asíncrona. Este método carga en línea los ficheros que le indiques:

```
<font inherit/Courier New,Courier,monospace;;inherit;;inherit>$.loadScriptSeries(['lista/de/ficheros.js', 'otro/fichero.js'], function(){
// callback a ejecutar cuando se haya cargado el último fichero
});</font>
```

### Directorio less

Dentro del directorio LESS encontrarás la hoja de estilos .less que da forma a este tema. En la primera línea verás que se importa el fichero "main.less". Este fichero incluye los estilos Bootstrap y otros estilos de componentes de la plantilla como el calendario.

El siguiente bloque define las variables. Puedes añadir todas las variables que necesites pero si eliminas alguna es posible que el selector de colores deje de funcionar adecuadamente.

Recuerda leer http://lesscss.org detenidamente para obtener más información y poder sacar el máximo rendimiento al pre-procesado de hojas de estilo.

### Directorios partials y templates

Los ficheros .tpl y .ptl son los templates y partials que utiliza Handlebars para renderizar el contenido de la página.

Los ficheros .tpl son las plantillas que se cargan al entrar en cada sección.  Puedes modificar su contenido, pero debes respetar los nombres de estos ficheros ya que de lo contrario harás que las distintas secciones del evento dejen de funcionar.

Al entrar en la página del evento por primera vez se carga el fichero main.tpl que renderiza el esqueleto principal de la página y después carga el contenido de la sección correspondiente.

Los ficheros .ptl son los parciales o partials, trozos de código que se pueden renderizar dentro de la página según sea necesario. Puedes modificarlos y crear tantos nuevos como veas necesario. Te recomendamos que eches un vistazo a su estructura para hacerte una idea de como utilizarlos.

Ejemplo:

```
1.- {{> overlay }}
 2.- {{> navbar this }}
 3.- <div id="content-wrapper">
 4.-     {{> header this }}
 5.-     {{> menu this }}
 6.-     <div id="content" class="container">
 7.-         {{> detail this }}
 8.-     </div>
 9.- </div>
10.- {{> footer this }}
```

La línea 1 carga el parcial overlay. Un parcial se carga con la sintaxis "{{> nombre }}". En las líneas 2, 4, 5, 7 y 10 se cargan más partials. El segundo parámetro es el contexto de datos. Si utilizamos this enviamos el contexto de la plantilla actual al parcial que estamos cargando.

Puedes explorar los ficheros .tpl y .ptl para ver las distintas opciones disponibles.

Como ves en las líneas 3, 6, 8 y 9, se puede combinar código HTML y Handlebars alternativamente.

El bloque div con identificador "content" es el que utiliza el motor para renderizar el contenido de cada sección. Si decides modificar el fichero main.tpl debes incluír este identificador para que el motor pueda renderizar las secciones correctamente.

## Modificar plantilla de sistema para convertirla en plantilla personalizada (sólo Plantillas Classic)

Se recomienda no utilizar símbolos ni caracteres acentuados en los nombres de fichero.

### Directorio ASSETS

En este directorio deberán incluirse todas las imágenes que quieran enlazarse desde la plantilla.

### Directorio CSS

En este directorio deberán incluirse todos los estilos que quieran enlazarse desde la plantilla. Los estilos se aplican mediante ficheros de estilos en cascada.

Si el fichero *css* hace referencia a una imagen incluida en el directorio *assets*, la ruta deberá ser relativa. Por ejemplo, si en el fichero *styles.css* quisieras poner como fondo la imagen disponible en *assets/background.png* tendrías que usar:

```
body {
  background-image: url("../assets/background.png");
}
```

En este directorio puede existir cualquier número de ficheros *css*, que deberán ser correctamente referenciados desde la plantilla (ver fichero *tpl*).

### Directorio JS

En este directorio deberán incluirse todos los scripts que quieran enlazarse desde la plantilla. Los scripts se aplican mediante ficheros *Javascript*.

Si algún script hace referencia a una imagen incluida en el directorio *assets*, la ruta deberá ser relativa.

En este directorio puede existir cualquier número de ficheros *Javascript*, que deberán ser correctamente referenciados desde la plantilla (ver fichero *tpl*).

### Fichero TPL

El fichero *tpl* contiene la información a renderizar por el sistema. La plantilla está escrita en lenguaje HTML y lleva etiquetas especiales delimitadas por dobles llaves que corresponden a los distintos bloques definidos.

```
{{ ETIQUETA }}
```

Al realizar una plantilla se pueden renderizar los bloques que se deseen, en cualquier orden. Además es posible englobarlos en cualquier contenido HTML para facilitar el estilo.

#### Embeber estilos y scripts

Al principio del fichero, dentro de la correspondiente etiqueta HTML *&lt;head>* deberán incluirse los estilos y scripts definidos por el usuario. Para hacerlo correctamente, de nuevo, las rutas deberán ser relativas.

Por ejemplo, para incluir los ficheros presentes:

- assets\
- css\
      - styles.css
- js\
      - script.js
- fichero.tpl

tendrías que hacerlo de la siguiente manera:

```
<head>
    {{ IE COMPATIBILITY }}
    {{ METAS AND TITLE }}
    {{ OTHER LINKS }}
    <!-- reset -->
    <link rel="stylesheet" type="text/css" href="css/styles.css" />
    {{ SCRIPTS }}
    <script type="text/javascript" src="js/script.js"></script>
</head>
```

Además, es posible consultar si un bloque está disponible con sentencias **IF**. De este modo, es posible saber si estás en una determinada sección, o si un bloque está presente para renderizar un contenido de una forma u otra. Por ejemplo:

```
<!-- !IF SUBHEADER IMAGE -->
    <div id="event-header-text">
    {{ SUBHEADER TITLE }}
    <div class="enrolment_wrapper">
        {{ ENROLMENT BUTTON }}
    </div>
    {{ SUBHEADER IMAGE }}
    </div>
<!-- END IF SUBHEADER IMAGE -->
```

Puedes ver en detalle los bloques disponibles en cada sección en el anexo más abajo.

## Subir plantilla personalizada

Una vez terminada la plantilla, tienes que crear un fichero comprimido que contenga los siguientes ficheros y carpetas:

- el fichero *tpl*
- las carpetas *assets*, *css*  y *js*

Es importante que todos estos elementos no estén contenidos dentro de ninguna carpeta extra, sino directamente en la raíz del fichero comprimido.

![](/media/admin/subir_plantilla_personalizada.png?align=center)

En la sección *Nueva plantilla*  completa todos los datos:

- El nombre que darás a tu plantilla.
- El número máximo de elementos a mostrar en el menú (el resto de elementos del menú se mostrarán en la opción de menú *“Más…”*).
- Una captura de pantalla que sirva para previsualizar tu plantilla.
- El fichero comprimido.

Y ya puedes hacer clic en *Guardar*. A partir de ahora tendrás disponible para cualquier evento tu [plantilla](/docs/eventos/diseno/plantillas) personalizada. Si tu plantilla no aparece en la sección de plantillas de la edición del evento, asegúrate de que esté seleccionada como [plantilla disponible](/docs/administracion/diseno/plantillas-disponibles).

## Anexo

[Documento](/docs/administracion/diseno/plantilla-personalizada-anexo) de bloques disponibles en las plantillas.
