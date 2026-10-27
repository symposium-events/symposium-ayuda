---
title: "Receptores de pago"
weight: 2
lastmod: 2024-04-14T15:33:25Z
dokuwiki: receptores_de_pago
---
Un Receptor de pago es un número de cuenta corriente, una cuenta de Paypal o un terminal de TPV al que van destinados los pagos que se realizan en un evento.

Puedes activar Receptores de pago en el Panel de Administración > Pagos > Receptores de pago:

![](/media/admin/recep.png?w=250&align=center)

Una vez que se ha activado un Método de pago, es necesario definir al menos una cuenta disponible que recoja los pagos para este Método. Para ello debes crear un Receptor de pagos. Es posible crear varios Receptores de pagos vinculados a cada Medio de pago, no hay una limitación en Symposium para ello. Será necesario que, una vez tengas activo el Método de pago, asignes el Receptor de pagos al evento para que pueda recibir los ingresos a esta cuenta. De lo contrario, el evento no podrá activar inscripciones de pago ni la venta de productos, al prescindir de un Receptor.

## Dar de alta un Receptor de pago

En este menú, obtendrás un listado de los distintos Receptores de pago que ya han sido creados en tu instancia. Puedes editarlos o bien, crear uno nuevo clicando en el botón "Añadir receptor de pago".

A la hora de crear un nuevo Receptor, deberás completar una serie de campos a partir de los datos que proporcione la entidad bancaria. Dependiendo del Método de pago al que va destinado el Receptor tendrán que configurarse condiciones diferentes.

Hay campos que son comunes en la creación de una nueva cuenta de pagos como son el correo de contacto para incidencias relacionadas con los pagos, un nombre descriptivo para mostrar internamente a los administradores contables, un nombre que se mostrará de forma pública al listas las opciones de pago disponibles al hacer una inscripción y el aviso que se debe mostrar cuando se ha seleccionado este método de pago.

Para todos los Receptores de pago hay una opción para establecer si se quiere que el terminal de pago esté disponible y asignado a todos los eventos por defecto, evitando así tener que realizar el proceso de asignación de forma manual.

![](/media/admin/receptor.png?w=750&align=center)

- Si se marca, el Receptor de pagos estará activado para todos los Eventos de la plataforma, sin necesidad de que los Organizadores lo soliciten.
- Si no se marca, los Organizadores deberán solicitar la activación del Receptor de pagos. La Asignación corresponde a un miembro del grupo de Gestores económicos.

Además, en caso de que se haya dado de alta al menos una [Unidad](/docs/gestion-economica/configuracion/accounting-units)[Administrativa](/docs/gestion-economica/configuracion/accounting-units) se podrá asignar el receptor a una de ellas. En caso de no querer utilizar esta funcionalidad, bastará con asignarlo a "Ninguna".

## Añadir una cuenta Paypal

En el campo *Cuenta*  será necesario indicar el correo de la cuenta Paypal que hayas contratado. Este Receptor permite la validación automática de pagos por parte de Symposium en el momento de ser efectuado.

![](/media/admin/paypal.png?w=799&align=center)

## Añadir una cuenta para transferencias bancarias

Los terminales de transferencias actúan de una forma diferente a los anteriores, pues requiere validación manual del pago por parte del Administrador económico de la plataforma.

Al configurar un terminal de este tipo tendrás que indicar el número de cuenta al que irán destinados los pagos, la entidad bancaria, el nombre del beneficiario. Además, se debe configurar el formato del concepto que los asistentes deben indicar al hacer la transferencia. Esto es lo que permitirá después identificar a qué inscripciones corresponde cada cobro recibido en la cuenta bancaria.

![](/media/admin/transferencia.png?w=819&align=center)

## Añadir un TPV de SERVIRED/REDSYS, CECA, ELAVON o CREDOMATIC

Para dar de alta un TPV virtual, es necesario contratarlo a la entidad bancaria, que se encargará de facilitar los datos de configuración del mismo para que pueda recibir pagos. Las principales entidades están adscritas a una de estás cuatro modalidades, REDSYS, CECA, ELAVON y CREDOMATIC. Una vez hayas formalizado la contratación, tendrás acceso a los datos de configuración necesarios.

En el formulario en Symposium, deberás elegir el tipo de TPV y a continuación cumplimentar los datos necesarios que te proveerá la plataforma del TPV.

| Campo del formulario en Symposium | Propiedad en Redsys | Propiedad en Ceca | Propiedad en Elavon | Propiedad en Credomatic |
|---|---|---|---|---|
| Cuenta | Identificador de comercio | MerchantID | ClientID | *no aplicable* |
| Identificador | *no aplicable* | *no aplicable* | *no aplicable* | Processor_id |
| Código de caja | *no aplicable* | AcquirerBIN | *no aplicable* | *no aplicable* |
| Terminal | Número de terminal (generalmente 001) | Número de terminal (generalmente 00000001) | Número o nombre de cuenta (opcional) | *no aplicable* |
| Divisa | Divisa del terminal (generalmente Euros) | Divisa del terminal (generalmente Euros) | Divisa del terminal (generalmente Euros) | Divisa del terminal (depende del processor_id) |
| Clave secreta | Clave secreta de seguridad | Clave secreta de seguridad | Secreto compartido | *no aplicable* |
| Clave secreta para pruebas | *no aplicable* | Clave secreta de seguridad para realizar pruebas | *no aplicable* | *no aplicable* |
| Llave pública | *no aplicable* | *no aplicable* | *no aplicable* | Key ID (123456789) |
| Llave privada | *no aplicable* | *no aplicable* | *no aplicable* | Clave secreta de seguridad |
| Validación extendida | Tipo de validación (en caso de error de configuración, pruebe a activar este valor) | *no aplicable* | *no aplicable* | *no aplicable* |

*  *

Además de los datos propios del TPV, tendrás que indicar unos valores para la gestión en Symposium:

| Propiedad | Descripción |
|---|---|
| Correo electrónico de contacto para reclamaciones e incidencias | Este correo será indicado a los usuarios cuando realicen pagos en la plataforma como correo de contacto. Es necesario ofrecer un servicio funcional de soporte a los usuarios si se van a gestionar pagos desde la plataforma. |
| Nombre descriptivo | Nombre que identifica a este terminal de forma interna, para tareas de gestión. |
| Nombre que se mostrará al público durante el proceso de compra | Nombre descriptivo que se mostrará al usuario a la hora de seleccionar el método de pago, por ejemplo, TPV de Eventos |
| Aviso que se mostrará al público durante el proceso de compra | Mensaje adicional que se mostrará al usuario cuando seleccione este método de pago. No es obligatorio. |

Una vez creado el Receptor de pago en Symposium, será necesario realizar una prueba para que tu proveedor te permita activar completamente el TPV. Para ello, selecciona "Utilizar este TPV en modo pruebas" y crea un evento en Symposium que contenga un pago. Asigna este nuevo TPV al evento de pruebas y realiza entonces una inscripción para comprobar el funcionamiento del TPV.

Los datos necesarios para poder realizar un pago de pruebas están disponibles en la sección de Activación de métodos de pago.
