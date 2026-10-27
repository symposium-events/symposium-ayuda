---
title: "What's new on the platform"
linkTitle: "Version history"
weight: 1
lastmod: 2016-04-26T14:05:24Z
dokuwiki: changelog
---
=

## What's new

=

## Version 2016.03.10

### 10 March 2016

- Added the option to close an event
- Updated the ReCaptcha version to support more devices

## Version 2015.11.15

### 15 November 2015

- Added support for Santander ELAVON POS terminals
- Added functionality to create diplomas and badges
- Added a compact view for products
- Added new encryption to REDSYS/SERMEPA POS terminals

## Version 2015.09.15

### 15 September 2015

- Added support for using the [RedIris SIR login](https://www.rediris.es/sir/). It can be tried out from the [Eventos CRUE](http://eventos.crue.org/login.html) environment.
- Updated and completed the Portuguese translation of the tool.

## Version 2015.07.15

### 15 July 2015

- Added an event query API. For more information contact [symposium@emagister.com](mailto:mailto:symposium@emagister.com).

## Version 2015.06.07

### 07 June 2015

- Added support for browsing under SSL security (HTTPS browsing)

To use it on the platform, we need you to generate a suitable certificate for the subdomain of the events platform. For more information contact [symposium@emagister.com](mailto:mailto:symposium@emagister.com).

- Added the option to raise money at events through [crowdfunding](/docs/eventos/asistentes/inscripcion#donaciones).

## Version 2015.05.26

### 26 May 2015

- New language options available (Tools > Enable multilanguage):
      - Change the default language of an event
      - Only show in the language menu the languages that have a translation (the event description is used to determine whether a language has a translation)
      - Hide certain languages in the event menu

## Version 2015.04.21

### 21 April 2015

- It is now possible to create a new edition of an event from an existing one. [You can read the help here.](/docs/eventos/creando-y-editando-un-evento/duplicar-evento)

## Version 2015.04.15

### 15 April 2015

- A group of users can be registered for an event using a CSV file. [You can read the help here.](/docs/eventos/asistentes/batch-registration)

## Version 2015.03.24

### 24 March 2015

- New users and event attendees now have their first name and surname in two separate database fields.
- Multiple users can be registered with a single email account. This account will manage those registrations as if they were its own or can transfer them to another user.
- Added the Other event type, which allows a custom event type to be specified.
- Added support for [CECA](https://comercios.ceca.es) POS terminals.

## Version 2015.01.27

### 27 January 2015

- Changed the IP security check in cookie validation; it affected users behind a load-balanced proxy or with rapidly changing IPs.
- Meta tag to force the latest version of Internet Explorer; IE 8 and earlier will not be supported.

### 15 January 2015

- Changed Emagister SEO links

## Version 2014.11.10

### 10 November 2014

- Added TLS encryption support for email servers
- Added the option to mark some registration form answers as public so that they are visible in the attendee list. When this is the case, the form will show a message where appropriate saying that the answer will be public, and the attendee can hide that information if they wish by marking their attendance as private.
- Added the sender to the body of an event contact email to fix problems caused by some email servers and clients being incompatible with the reply-to field
- Improved the visual feedback of the product editing form
- Added "Course" as an event type
- Bug fixes and other improvements

## Version 2014.10.10

### 10 October 2014

- Warning when editing the registration form if any attendee has already answered it, to prevent loss of information
- New functionality that allows HTML code to be added directly to the event template, giving versatility to event organizers with knowledge of style sheets and JavaScript
- In event editing, when searching for attendees in the list, you can filter by the answers given in the registration form

## Version 2014.10.06

### 6 October 2014

- Improved the user interface of the attendee list for greater clarity
- Improved the rich text editor to allow adding other file types, such as documents, in addition to images

## Version 2014.09.23

### 23 September 2014

- Added support for different time zones, both the partner's and each event's according to its venue
- More detail when displaying the dates of accepted transactions in the financial management panel
- Better user interaction during the abstract and paper submission process
- Added the option to link to any part of the platform in a preset language
- Greater system robustness through fixing minor issues

## Version 2014.07.28

### 28 July 2014

- Improved user interaction when rejecting payments in the financial management panel
- Automatic change of the status of any registrations if the organizer disables validation
- Agenda: improved styles and implemented text and calendar search
- Optional notification to the organizer of a new registration, regardless of the validation type
- Added multi-language support to the event files section
- Improved the list of upcoming events on the home page to show current events throughout the whole day
- Improvement in the financial management panel that allows part of the amount to be withheld as a penalty when a payment is rejected
- Improvement in the event registration process that allows, during the following 48 hours, changing the payment method for a user who chose to pay by bank transfer
- Improved the styles of the mobile version of the home page
- Bug fixes

## Version 2014.06.11

### 11 June 2014

- Export to Excel in different formats
- Improved texts and translations
- Fixed top menu in some administration sections, acting as an index (pilot test)
- When editing an item in the various event editing sections, the screen now scrolls to the newly opened form
- Various platform stability improvements

## Version 2014.04.29

### 29 April 2014

- Integration with the Rovira i Virgili University Agenda:
- Widget showing agenda events on the home page
- [New section](/docs/administracion/configuracion/rss-faculties) with an editable list of faculties
- Multiple RSS feeds, by faculty and event type
- Exclusive views for agenda events
- Adaptation of the corporate styles of [www.urv.cat](http://www.urv.cat) for the Rovira i Virgili University [events platform](http://events.urv.cat)
- Various improvements to user interaction
- The rich text editor used in various sections of the event editing menu can now be viewed full screen. In addition, the basic version now includes the paste text option.
- Improved the warning message before deleting registration form items
- The event search environment in the financial management panel is more user-friendly
- Date editing fields that include minutes now allow 5-minute intervals to be selected
- Added a link to make it easier to reply to several emails that report on events
- Bug fixes
- Implementation of a responsive theme in the demo environment
- Updated the Emagister lead capture page
- Adaptation of the corporate styles of [campusmarenostrum.es](http://campusmarenostrum.es) for the Campus Mare Nostrum [events platform](http://eventos.campusmarenostrum.es)
- Financial managers can now belong to as many groups as necessary **NOTE:** we have added a [documentation page](/docs/anexos/eventos-de-demostracion/evento-demo) explaining how to use the platform to run tests with events.

## Version 2014.01.29

### 29 January 2014

- Added a new [system template](/docs/eventos/diseno/plantillas) for events: compact extended.
- Added a [new section](/docs/eventos/contenido/organizadores) that allows the organizers of an event to be shown.
- Added one more column to the Excel file of the financial management panel statistics.
- Display of a help link that shows the corresponding Wiki section.
- Visual notification in the mail server settings reporting on the connectivity of the configured server and port.

## Version 2014.01.13

### 13 January 2014

- Added a new option to export the financial management panel statistics to Excel.
- System bug fixes.

## Version 2013.12.17

### 17 December 2013

- Better user interaction when editing payment receivers.
- Added a search option in the management of received submissions.
- Greater clarity in attendee lists, Excel and print view.
- Greater flexibility when editing the event menu: new submenus can now be created and menu items nested in them by dragging and dropping.
- Better terminology throughout the event's submission management process.
- Added a new option for Universitat Rovira i Virgili that lets them show the members of an event's organizing team on the event page.

## Version 2013.11.4

### 4 November 2013

- For partners who request it, notifications addressed to the event organizer are sent to all members of the event's organizing committee.
- Before changing the registration type, confirmation is requested, detailing the data that will be lost.
- Dynamic generation of system template kits so that they never become outdated.

## Version 2013.10.29

### 29 October 2013

- The subject of emails sent in relation to an event can be customised.
- Various system bug fixes.

## Version 2013.10.21

### 21 October 2013

- Added a privacy link in the footer to comply with the European directive on the use of cookies.
- The list of accepted abstracts on the event page is now paginated.
- The category a received submission belongs to, whether an abstract or a paper, can now be changed.
- Added an Excel export option for abstracts and papers.
- Various system bug fixes.

## Version 2013.10.3

### 3 October 2013

- Improved the event summary to show more data on attendances, tickets and products.
- Added linking products to attendees in the registration process.
- Added a system for showing help by section, managed by administrators.
- Added the event summary to the financial management panel.
- Applied alphabetical order to product lists.
- Migrated the platform to more powerful servers.
- Various system bug fixes.

## Version 2013.9.2

### 2 September 2013

- Improved the overall response time of the platform.
- Updated all maps to use the latest version of Google Maps.

## Version 2013.8.5

### 5 August 2013

- When generating the Excel file of event attendees, you can now filter by cancelled attendance.
- The list of events on the front page now shows the internationalised event title if the event has multi-language enabled.
- The payment management Excel file now repeats common values to make filtering and sorting easier.
- New [general notification form](/docs/administracion/herramientas/push-general) for platform administrators to send notifications to all users of the attendees mobile app.
- The University of La Laguna now allows its members to access the platform through CAS.
- Improved the response time of the event's public page.
- Various system bug fixes.

## Version 2013.7.8

### 8 July 2013

- New comprehensive submission management system: configure [submission intake](/docs/eventos/doc-cientifica/recepcion-comunicaciones) and view [received submissions](/docs/eventos/doc-cientifica/comunicaciones-recibidas).
- New data layout in the export of payments to Excel.
- Payment receivers sorted by administrative unit.
- Attendees sorted alphabetically in the export of the product list to Excel.
- Added an informative message about multiple registration in the event registration process.
- Improved the response time of the event's public page.
- Various system bug fixes.

## Version 2013.6.17

### 17 June 2013

- Expanded the platform documentation.
- New "landing" page.
- New template for events, showing the menu vertically in the Compact style.
- New field in the registration form for selecting countries, in any platform language.
- Added compatibility with the latest version of the Twitter API.
- Added the option to translate predefined answers in the single and multiple choice questions of the registration form.
- Various system bug fixes.

## Version 2013.6.3

### 3 June 2013

- Added a new permission available to committees that gives access to the related product lists.
- Visual improvement when showing the list of payment receivers.
- The attendee list can now be filtered by payment status.
- The event [registration form](/docs/eventos/asistentes/formulario-de-inscripcion) now allows files to be attached.
- Faster listing of payments in the financial management panel.
- The platform's cache system has been improved.
- It is now possible to [export an event's payments](/docs/gestion-economica/herramientas/gestionar-pagos-de-un-evento) to an Excel file.
- Various system bug fixes.

## Version 2013.5.20

### 20 May 2013

- Products can now be purchased and linked to an existing registration. This can be done from the email containing the receipt or from the [attendee panel](/docs/panel-de-usuario/eventos-a-los-que-asisto).
- The event [registration form](/docs/eventos/asistentes/formulario-de-inscripcion) now allows questions with predefined answers.
- Improved management of pending payments. If the current user is detected to have a pending payment, they are helped to find out whether they had any problem. In that case, they can resume the payment or cancel it. ([see FAQ](/docs/faq#gestion-de-errores-en-los-pagos))
- Schedule dates are now automatically adjusted to the event start as a suggestion.
- Various system bug fixes.

## Version 2013.5.6

### 6 May 2013

- The event list is now accessible in the administration panel.
- Improvements to the information in the event list, reflecting accounting.
- Pagination in the event list.
- Payment receivers grouped by type.
- Improvement when copying registration form questions, allowing you to select which ticket type to copy them to.
- Option to delete event templates already uploaded.
- Email notifications when a product on sale goes out of stock.
- Option to reduce the stock of a product already on sale down to a minimum of the sales already made.
- Improvements to the loading process and progress indicators while data is loaded in the background.
- Various system bug fixes.

## Version 2013.4.25

### 25 April 2013

- New functionality for configuring [administrative units](/docs/gestion-economica/configuracion/accounting-units) to make financial management easier
- New functionality for adding [support users](/docs/administracion/usuarios/helpdesk-users), intended to provide help
- New functionality that shows an [event list](/docs/gestion-economica/herramientas/events-list) in the financial management panel
- New functionality for configuring a [custom domain](/docs/eventos/herramientas/custom-domain) for your event
- Added to the accounting panel a list of events pending assignment of a payment receiver
- Registrations no longer require an availability period; if none is specified, the registration period is used
- Improved the system for copying questions between registrations to include translations, required status, etc.
- Improved the attendee list, which now also includes cancelled attendances.
- Improved the administration of REDSYS POS terminals to support the different message signing types.
- Improved the behaviour of REDSYS POS terminals in cases where the terminal omits the URLOK response.

## Version 2013.4.15

### 15 April 2013

- Improvements to the event cancellation process. As well as keeping an accounting trail of the payments, a form is shown for contacting the event organizers.
- The link to the Facebook page shown on the main screen, in the social networks box, can be configured from the administration panel
- You can now put the event into draft mode if the registration period has not yet started; in addition, confirmation is requested before publishing the event
- Several attendees can be selected to send an email to from the event editing menu
- Several typos have been fixed
- The Editum publications form has been updated (University of Murcia only)
- More help texts have been added to event editing
- New functionality for configuring the [outgoing email server](/docs/administracion/configuracion/email-server) and updating the contact email
- The text shown in the footer of emails has been updated
- You can now change more details of a payment receiver in use
- You can now choose whether your payment receiver is in test mode or ready to be used
- Improved the display of the attendee list file, discarding repeated questions in the registration form
- Improvements to custom template management; they can now be downloaded for editing
- The option to show events on the Emagister Events portal is now available to organizers, from Basic details in event editing
