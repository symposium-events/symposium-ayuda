---
title: "Clave de validación de pagos"
weight: 4
lastmod: 2019-09-10T12:57:14Z
dokuwiki: clave_de_validacion_de_pagos
---
Esta clave sirve como una medida de seguridad adicional y puede ser configurada y modificada por un Administrador desde el Panel de Administración.

![](/media/admin/clave_pagos.png?w=250&align=center)

El sistema permite añadir una contraseña para limitar la potestad de los Administradores económicos a la hora de rechazar pagos que figuran como confirmados. Como el rechazo de pagos que figuran como confirmados puede provocar descuadres en las cuentas, es posible limitar esta posibilidad a un grupo de administradores económicos reducido para minimizar la posibilidad de errores.

![](/media/admin/clave_pagoss.png?w=800&align=center)

El formulario permite configurar y modificar la contraseña. La contraseña no se ocultará visualmente, para evitar tener que modificarla en caso de extravío y tener que comunicársela a todos los administradores económicos nuevamente.

En caso de eliminar la contraseña, se eliminará el requisito de la misma y cualquier Administrador económico podrá rechazar un pago que figure como confirmado.

## Cómo y cuándo funciona

Cuando el Administrador económico quiera rechazar un pago, Symposium le preguntará la clave en un campo denominado Contraseña contable. Si la clave es correcta, podrá rechazar finalmente el pago.

![](/media/panel_admin/verificacion_contrasena.png?w=400&align=center)
