---
title: "Personalizar la plantilla del Resumen de evento"
weight: 91
lastmod: 2020-03-09T09:07:11Z
dokuwiki: plantillas_de_resumen_evento
---
La herramienta de difusión de resúmenes de eventos por email se sirve de una plantilla genérica diseñada por Symposium. Los Administradores de plataforma pueden generar plantillas adicionales a partir de la genérica. En este artículo se documenta el fondo conceptual sobre el que se ha construido esta herramienta con objeto de que los diseñadores de plantillas de cada institución dispongan del conocimiento necesario para mantener la compatibilidad con clientes de correo electrónico.

## Tecnologías aplicadas

La herramienta se ha diseñado utilizando tres tecnologías:

- [Handlebars](https://handlebarsjs.com/)
- [Foundation email templates CSS](https://cdnjs.cloudflare.com/ajax/libs/foundation-emails/2.2.1/foundation-emails.min.css)
- Style inliner

## Fundamentos

La plantilla principal está escrita usando Handlebars y el framework Foundation. Handlebars se usa para la lógica de la plantilla y Foundation, para la compatibilidad con navegadores y diferentes dispositivos. Por su parte, el style inliner introduce en los tags de la maquetación los estilos para dar compatibilidad con los distintos clientes de correo electrónico. En este sentido, sin embargo, es posible que algunas aplicaciones, a pesar de todo, no interpreten correctamente el código en función del grado de adhesión a los estándares.

## Apariencia de una plantilla

El contenedor principal tiene este aspecto:

```html4strict
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="icon" href="../../assets/img/icons/foundation-favicon.ico" type="image/x-icon">
    <meta name="viewport" content="width=device-width">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/foundation-emails/2.2.1/foundation-emails.min.css"
        rel="stylesheet">
    <title>{{templateTitle}}</title>
</head>
<body>
    <!-- Docs - https://foundation.zurb.com/emails/docs/css-guide.html -->
    <!-- Wrapper for the body of the email -->
    <table class="body" data-made-with-foundation>
        <tr>
            <!-- The class, align, and <center> tag center the container -->
            <td class="float-center" align="center" valign="top">
                <center>
                    <!-- The content of your email goes here. -->
                    <table class="container">
                        <tr>
                            <td>
                                <!-- Header -->
                                <table class="row padding">
                                    <tr>
                                        <th class="partner-logo">
                                            <a href="{{partnerUrl}}" target="_blank"><img src="{{partnerLogoUrl}}" /></a>
                                        </th>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        {{#if eventImageUrl}}
                    </table>
                </center>
            </td>
        </tr>
    </table>
</body>
```

El elemento header dentro del body es un ejemplo de cómo crear una fila con un enlace a la imagen del evento.

```
{{partnerUrl}}
```

y

```
{{partnerLogoUrl}}
```

son variables que al generar el resumen a partir de la plantilla se sustituirán por los contenidos a los que hacen referencia.

## Variables disponibles, cuándo usarlas y qué representan

| variable | contenido |
|---|---|
| contactEmail | El email de contacto del evento (si no lo hay, se deja en blanco) |
| contactInfo | Verdadero o Falso, según si hay o no información de contacto |
| contactName | Nombre de contacto del evento (si no lo hay, se deja en blanco) |
| contactPhone | Teléfono de contacto del evento (si no lo hay, se deja en blanco) |
| eventDate | Fechas del evento ya formateadas |
| eventDateStartYear | Año de la fecha de inicio del evento en formato YYYY |
| eventDateStartMonth | Mes de la fecha de inicio del evento en formato mm (con ceros iniciales) |
| eventDateStartDay | Día de la fecha de inicio del evento en formato dd (con ceros iniciales) |
| eventDateStartHour | Hora de la fecha de inicio del evento en formato HH (24h con ceros iniciales) |
| eventDateStartMinute | Minuto de la fecha de inicio del evento en formato ii (con ceros iniciales) |
| eventDateEndMonth | Análogo a la fecha de inicio |
| eventDateEndHour | Análogo a la fecha de inicio |
| eventDateEndMinute | Análogo a la fecha de inicio |
| eventTypeName | Tipo del evento |
| eventDateEndDay | Análogo a la fecha de inicio |
| eventDateEndYear | Análogo a la fecha de inicio |
| eventDescription | Descripción completa del evento en HTML que aparece en la home de su website. Debe usarse con precaución porque podría romper el estilo de la plantilla en caso de que contenga estilos en línea o tablas |
| eventIcsUrl | URL del fichero ICS para integración con aplicaciones de calendario personal |
| eventImageUrl | Imagen principal del evento (si no la hay, se deja en blanco) |
| eventInscriptionUrl | URL de la página de inscripción al evento, si está configurado para aceptar asistentes. Si no, queda en blanco |
| eventMapUrl | URL de la ubicación del evento proporcionada por Google Maps |
| eventPlace | Lugar de celebración del evento |
| eventPlaceDetail | Si existe ese contenido, información adicional sobre la ubicación del evento |
| eventShortDescription | Descripción breve del evento, si la hay (este contenido no es traducible en Symposium) |
| eventTitle | Título del evento |
| partnerLogoUrl | URL del logo de la institución que se haya configurado en la plataforma |
| partnerUrl | URL del partner, es decir, la home de la plataforma de eventos |
| templateTitle | Nombre de la plantilla de este resumen |
|  |  |

## Cuestiones adicionales

Dado que Symposium utiliza Handlebars para esta herramienta, es posible crear una plantilla específica que use cualquier proceso lógico que permita Handlebars. Por ejemplo, es posible utilizar sentencias

```
 {{#if}}
```

y llamadas a variables

```
{{variable}}
```

y

```
{{{variable}}}
```

Esta última si contiene HTML que no debe escaparse.
