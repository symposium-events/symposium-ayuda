---
title: "Como utilizar el entorno de pruebas de PayPal"
weight: 90
lastmod: 2013-03-27T12:31:15Z
dokuwiki: paypal_developer
---
Para utilizar el entorno de pruebas de PayPal, debemos dirigirnos a [su sitio web](https://developer.paypal.com) e identificarnos con nuestras credenciales de PayPal utilizando el botón de la barra superior.

![](/media/paypal_developer/login.png?w=740&align=center)

Una vez identificados, nuestra cuenta se habrá ampliado a cuenta de desarrollador PayPal. Denominaremos a esta cuenta nuestra "Cuenta Developer" a partir de ahora.

A continuación, nos dirigiremos a la opción **Applications** del menú, y dentro de esta localizaremos **Sandbox Accounts** en el menú de la izquierda.

Desde esta sección podremos gestionar nuestras cuentas de pruebas. Con el botón situado en la esquina superior derecha, **Create Account**, podremos crear nuevas cuentas de pruebas.

![](/media/paypal_developer/config.png?w=850&align=center)

Deberemos crear dos cuentas, una de tipo **Personal** que será la que utilicemos para comprar y una tipo **Business** que será la que utilicemos para configurar el receptor de pago.

Los datos **Email address** son para dar nombre a las cuentas, y no es necesario que existan como cuentas de correo electrónico reales. Por tanto, podemos usar cuentas como prueba-paypal@universidad.es o pruebas@mispruebas.com. Recomendamos utilizar contraseñas fáciles de recordar e introducir, ya que se hará muchas veces. Por ejemplo: 12345678.

Es interesante fijar un **PayPal balance** inicial, aunque no obligatorio. Podemos fijarlo en una cantidad muy alta, para evitar tener que editarlo en el futuro, por ejemplo, 5.000.

El resto de datos son optativos, aunque dejaremos **Bank verified account** fijado a Yes para ahorrarnos mensajes de confirmación y otras casuísticas.

Cuando hayamos creado ambas cuentas simplemente volveremos a la herramienta y [daremos de alta un receptor de pago](/docs/administracion/pagos/receptores-de-pago) de tipo PayPal con el dato Cuenta como la dirección de correo que hayamos utilizado en nuestra cuenta de pruebas Business. A continuación se lo [asignaremos a nuestro evento de prueba](/docs/gestion-economica/configuracion/asignar-receptor-de-pago) y realizaremos una [inscripción](/docs/uso-de-la-plataforma/inscripcion-a-un-evento).

En el momento de realizar el pago, seleccionaremos nuestro receptor de pruebas y al llegar a PayPal utilizaremos las credenciales de la cuenta Personal que acabamos de crear.

NOTA: Es necesario estar identificado con la "Cuenta Developer" para poder utilizar el entorno de pruebas de PayPal. Es decir, para poder pagar con nuestras cuentas de pruebas, debemos haber pasado por el entorno [PayPal Developer](https://developer.paypal.com) y habernos identificado con nuestra cuenta de PayPal.
