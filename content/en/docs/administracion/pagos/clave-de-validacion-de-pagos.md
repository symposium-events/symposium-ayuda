---
title: "Password for payment validation"
weight: 4
lastmod: 2019-09-10T12:57:14Z
dokuwiki: clave_de_validacion_de_pagos
---
This password serves as an additional security measure and can be configured and changed by an Administrator from the Administration panel.

![](/media/admin/clave_pagos.png?w=250&align=center)

The system lets you add a password to limit the ability of Economic administrators to reject payments that are shown as confirmed. Since rejecting payments shown as confirmed can cause the accounts not to balance, you can restrict this possibility to a small group of economic administrators to minimize the chance of errors.

![](/media/admin/clave_pagoss.png?w=800&align=center)

The form lets you set and change the password. The password is not visually hidden, to avoid having to change it if it is lost and then communicate it again to all economic administrators.

If you delete the password, the requirement is removed and any Economic administrator will be able to reject a payment shown as confirmed.

## How and when it works

When the Economic administrator wants to reject a payment, Symposium will ask for the password in a field called Accounting password. If the password is correct, they will finally be able to reject the payment.

![](/media/panel_admin/verificacion_contrasena.png?w=400&align=center)
