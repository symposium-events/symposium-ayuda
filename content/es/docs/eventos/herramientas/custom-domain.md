---
title: "Dominio personalizado"
weight: 9
lastmod: 2020-01-22T13:43:38Z
dokuwiki: custom_domain
---
Por omisión, todos los Eventos dentro de Sympoisum tienen una página con dirección tipo: `http://institución.symposium.events` , donde institución es el nombre genérico de la institución que ha contratado Symposium. Es posible que la institución disponga de un dominio propio y quieras utilizar una dirección web específica para el Evento. Con esto mejoras la personalización.

En el menú **Herramientas > Dominio personalizado** existe la posibilidad de indicar la dirección que tienes para el Evento y que debes haber registrado antes.

![](/media/panel_organizador/dominio.png?w=250&align=center)

Escribe en el cuadro de texto la dirección del Evento y haz clic en Guardar. Para que funcione, debes tener configurar la Zona DNS de tu gestor de dominio de este modo:

| | | |
|---|---|---|
| **domain.tpl** | **A** | **63.32.241.141** |
| **www.domain.tpl** | **CNAME** | **domain.tpl** |

Sustituye *domain.tpl* por el dominio que hayas contratado.
