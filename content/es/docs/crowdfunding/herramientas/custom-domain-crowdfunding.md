---
title: "Dominio personalizado"
weight: 13
lastmod: 2020-08-21T08:55:07Z
dokuwiki: custom_domain_crowdfunding
---
Por omisión, todos los proyectos dentro de Sympoisum tienen una página con dirección tipo: http://institución.symposium.events , donde institución es el nombre genérico de la institución que ha contratado Symposium. Es posible que la institución disponga de un dominio propio y quieras utilizar una dirección web específica para el proyecto. Con esto mejoras la personalización.

En el menú **Herramientas > Dominio personalizado** existe la posibilidad de indicar la dirección que tienes para el proyecto y que debes haber comprado antes.

![](/media/crowdfunding/menu_custom_domain.png?w=290&align=center)

Escribe en el cuadro de texto la dirección que has contratado precedida de las tres uves dobles (www.domain.tpl) y haz clic en Guardar. Para que funcione, debes configurar la Zona DNS del dominio que contrataste de este modo:

| | | |
|---|---|---|
| **domain.tpl** | **A** | **63.32.241.141** |
| **www.domain.tpl** | **CNAME** | **domain.tpl** |

Sustituye *domain.tpl* por el dominio que hayas contratado.
