---
title: "LDAP configuration"
weight: 11
lastmod: 2013-03-21T08:46:28Z
dokuwiki: configuracion_ldap
---
Lets you enter the parameters to connect to the corporate LDAP server and authenticate the portal's users with this method.

![](/media/admin/captura_de_pantalla_2013-03-21_a_la_s_09.42.10.png?align=center)

Users who log in through this method are considered native users of the portal and can have an organizer role if it has been requested.

A user could be a user of the portal without having logged in through LDAP. As soon as they log in with LDAP, if their email address is the same, a link is established between both accounts, and from then on they can access their account with either option: LDAP or the portal login for external users.

Another feature is that, once linked to an LDAP account, the option to change the password is disabled.
