---
title: "Custom domain"
weight: 13
lastmod: 2020-08-21T08:55:07Z
dokuwiki: custom_domain_crowdfunding
---
By default, all projects in Symposium have a page with an address like http://institución.symposium.events, where institución is the generic name of the institution that has contracted Symposium. The institution may have its own domain and you may want to use a specific web address for the project. This improves customization.

In the **Tools > Custom domain** menu you can enter the address you have for the project, which you must have purchased beforehand.

![](/media/crowdfunding/menu_custom_domain.png?w=290&align=center)

Enter in the text box the address you have purchased, preceded by the three Ws (www.domain.tpl), and click **Save**. For it to work, you must configure the DNS zone of the domain you purchased as follows:

| | | |
|---|---|---|
| **domain.tpl** | **A** | **63.32.241.141** |
| **www.domain.tpl** | **CNAME** | **domain.tpl** |

Replace *domain.tpl* with the domain you have purchased.
