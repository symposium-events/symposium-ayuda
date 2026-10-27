---
title: "Unidades Administrativas"
weight: 90
lastmod: 2013-04-26T07:03:37Z
dokuwiki: accounting_units
---
En SYMPOSIUM by Emagister se denominan Unidades Administrativas a los grupos en los que se engloban receptores de pago y administradores económicos, para permitir una gestión económica departamental. Definir una unidad administrativa permite restringir el ámbito de operación de determinados receptores de pago y/o administradores económicos a un subconjunto de eventos.

Además los organizadores de eventos podrán solicitar ser administrados por una determinada unidad, poniéndose en contacto con la misma para solicitar la asignación de un receptor de pagos.

## Como empezar a utilizar las Unidades Administrativas

Para empezar a utilizar esta funcionalidad debemos crear una Unidad Administrativa. Para ello, nos dirigiremos a la sección Administradores económicos dentro del Panel de Administración.

Al dar de alta un nuevo Administrador económico podremos asignarlo a una Unidad Administrativa existente o crear una nueva. Si seleccionamos "Nueva unidad administrativa" se nos pedirán dos datos: el nombre de la unidad y un correo electrónico de contacto. Si seleccionamos "Administrador económico global" le asignaremos permisos globales y no verá su ámbito restringido (será como no utilizar las Unidades Administrativas).

![](/media/accounting_units/add_group.png?w=744&align=center)

El nombre de la unidad será visible para administradores y organizadores de eventos y debe ser descriptivo. El correo electrónico se usará para comunicar al grupo que hay eventos pertenecientes a esa unidad pendientes de la asignación de un receptor de pago.

![](/media/accounting_units/new_group.png?w=742&align=center)

En esta imagen podemos ver el resultado de crear un nuevo administrador y asignarlo a una nueva Unidad Administrativa. Ahora, disponemos de dos grupos en el listado: los Administradores Globales (que no están restringidos) y la nueva unidad denominada a modo de ejemplo "Mi Unidad Administrativa".

Podemos ver también una serie de botones que nos permiten acciones sobre los elementos. Los botones más grandes, Editar y Borrar permiten modificar o eliminar la Unidad Administrativa. Podemos cambiar su nombre y su correo de contacto en cualquier momento. Los botones más pequeños se utilizan para modificar a los administradores económicos. Editar permite cambiar de Unidad Administrativa a ese usuario (ya sea a una existente o a una nueva) y Desactivar le quita los privilegios de Administración Económica.

También podemos ver que hay un administrador económico que no puede ser modificado, lo que se indica con un icono de un candado. Esto ocurre cuando activamos la casilla "¿Incluir administradores del sitio?" e indica que ese usuario es un Administrador de la plataforma y por tanto no se le puede restringir ni modificar.

**NOTA:** Para que exista una unidad administrativa es indispensable que tenga un administrador económico asignado. Por eso, para crear una unidad administrativa, hay que hacerlo dando de alta un nuevo administrador económico o "destinando" a ella a uno ya existente. Si se vacía una unidad administrativa, esta será eliminada.

A partir de este momento, ese administrador económico verá su ámbito reducido a su Unidad Administrativa. Solo podrá asignar los receptores de pago que estén asignados a su unidad.

## Limitando el uso de determinados receptores de pago

Una vez creada una Unidad Administrativa, ya podemos dar de alta o modificar los receptores de pago para que solo pertenezcan a dicha unidad. Esto significa que los administradores contables de dicha unidad dejarán de tener disponibles todos los receptores del sistema y pasarán a tener solo los que se han asignado explícitamente.

En el formulario de alta y edición de receptores de pago tendremos disponible un desplegable que nos permitirá indicar a que Unidad Administrativa se restringe este receptor.

![](/media/accounting_units/add_group_to_receiver.png?w=741&align=center)

Una vez guardados los cambios, este receptor quedará vinculado a la Unidad Administrativa.

**NOTA:** Los administradores económicos globales, en caso de haberlos, podrán asignar los receptores indistintamente, sin verse afectados por ninguna limitación.

## El organizador de eventos. Solicitando un receptor de pago.

Cuando utilizamos un sistema basado en Unidades Administrativas, añadimos una nueva funcionalidad de cara al organizador de eventos. Al configurar la inscripción a su evento, podrá solicitar a una de las unidades administrativas que le asigne un receptor de pago.

![](/media/accounting_units/send_request_receiver.png?w=738&align=center)

Esta acción enviará un correo electrónico a la dirección de contacto de la Unidad Administrativa, y además, mostrará al evento como pendiente de asignación en el Panel de Contabilidad de la unidad correspondiente.

Este sistema agiliza la comunicación entre organizadores y gestores a la hora de iniciar procesos de pago en eventos.

**NOTA:** Un organizador podrá solicitar un receptor de pago a una unidad administrativa aunque ya haya realizado una solicitud (útil para evitar errores en solicitudes, etc). La solicitud previa se cancelará y se iniciará una nueva. Esto será posible **solo** mientras no se haya recibido ningún pago en el evento. En el momento en que se hayan comenzado a recibir pagos, el cambio de unidad administrativa no será realizable.

![](/media/accounting_units/request_receiver.png?w=739&align=center)
