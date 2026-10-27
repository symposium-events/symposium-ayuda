---
title: "Flow diagram"
weight: 5
lastmod: 2019-07-05T11:34:12Z
dokuwiki: los_estados_de_una_inscripcion
---
![](/media/los_estados_de_una_inscripcion/inscripcion_estado.png?w=650)

## Base case

A registration is generally set to *Pending* status when it is created. It will then be *Confirmed* or *Rejected* by manual validation or by the automatic validation performed through payment.

There are two special cases that change this behaviour. If the registration is free and has no validation, for example, the registration automatically becomes *Confirmed*. If the registration is paid and has manual validation, the attendance will have the status set manually, ignoring the payment status.

It is worth noting that there is an additional setting: the registration can be *Cancelled*. A cancelled registration is not taken into account in any calculation; it is simply stored for record-keeping purposes. Cancelled is not a status as such, but a flag on a registration. Therefore, a registration can be pending and cancelled, or confirmed and cancelled. This is because the Cancelled status is set by the attendee, whereas the other statuses are set by the organizer or the platform.

## Types of event attendee

**Confirmed** attendees are those who have followed one of these paths:

- they registered for a free event without validation
- they registered for a free event with validation and were accepted by the organizer
- they registered for a paid event without validation and made a bank transfer payment that was accepted by the accountant
- they registered for a paid event with validation and were accepted by the organizer

**Pending** attendees are those who have followed one of these paths:

- they registered for a free event with validation and have not yet been validated by the organizer
- they registered for a paid event without validation and made a bank transfer payment that has not yet been validated by the accountant
- they registered for a paid event with validation and have not yet been validated by the organizer

**Rejected** attendees are those who have followed one of these paths:

- they registered for a free event with validation and their registration was denied by the organizer
- they registered for a paid event without validation and made a bank transfer payment that was denied by the accountant
- they registered for a paid event with validation and their registration was denied by the organizer

**Cancelled** attendees are those who have followed one of these paths:

- they decided to cancel their attendance, an option available from their attendee panel
- they registered for a paid event with or without validation and made a payment with automatic validation that was denied
