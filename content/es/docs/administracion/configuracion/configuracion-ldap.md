---
title: "Configuración LDAP"
weight: 11
lastmod: 2013-03-21T08:46:28Z
dokuwiki: configuracion_ldap
---
Permite introducir los parámetros para conectar con el servidor LDAP corporativo y autenticar a los usuarios del portal mediante este método.

![](/media/admin/captura_de_pantalla_2013-03-21_a_la_s_09.42.10.png?align=center)

Los usuarios que entren a través de este método será considerado usuario nativo del portal y puede tener un rol organizador si así se ha solicitado.

Un usuario podría ser usuario del portal sin haber entrado a través de LDAP. En el momento que entre con LDAP, si su cuenta de correo es la misma, se establecerá un vínculo entre ambas cuentas pudiendo a partir de ese momento, entrar a su cuenta desde cualquiera de las dos opciones LDAP y login del portal para usuarios externos.

Otra características, es que al vincularse con una cuenta de LDAP, la opción de cambiar contraseña se desactiva.
