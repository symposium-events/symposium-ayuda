---
title: "Customizing the Event summary template"
weight: 91
lastmod: 2020-03-09T09:07:11Z
dokuwiki: plantillas_de_resumen_evento
---
The tool for distributing event summaries by email uses a generic template designed by Symposium. Platform administrators can create additional templates based on the generic one. This article documents the conceptual background on which this tool has been built, so that each institution's template designers have the knowledge needed to maintain compatibility with email clients.

## Technologies used

The tool has been designed using three technologies:

- [Handlebars](https://handlebarsjs.com/)
- [Foundation email templates CSS](https://cdnjs.cloudflare.com/ajax/libs/foundation-emails/2.2.1/foundation-emails.min.css)
- Style inliner

## Fundamentals

The main template is written using Handlebars and the Foundation framework. Handlebars is used for the template logic and Foundation for compatibility with browsers and different devices. The style inliner, in turn, inserts the styles into the layout tags to provide compatibility with the various email clients. In this regard, however, some applications may still not interpret the code correctly, depending on their degree of adherence to standards.

## What a template looks like

The main container looks like this:

```html4strict
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="icon" href="../../assets/img/icons/foundation-favicon.ico" type="image/x-icon">
    <meta name="viewport" content="width=device-width">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/foundation-emails/2.2.1/foundation-emails.min.css"
        rel="stylesheet">
    <title>{{templateTitle}}</title>
</head>
<body>
    <!-- Docs - https://foundation.zurb.com/emails/docs/css-guide.html -->
    <!-- Wrapper for the body of the email -->
    <table class="body" data-made-with-foundation>
        <tr>
            <!-- The class, align, and <center> tag center the container -->
            <td class="float-center" align="center" valign="top">
                <center>
                    <!-- The content of your email goes here. -->
                    <table class="container">
                        <tr>
                            <td>
                                <!-- Header -->
                                <table class="row padding">
                                    <tr>
                                        <th class="partner-logo">
                                            <a href="{{partnerUrl}}" target="_blank"><img src="{{partnerLogoUrl}}" /></a>
                                        </th>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        {{#if eventImageUrl}}
                    </table>
                </center>
            </td>
        </tr>
    </table>
</body>
```

The header element inside the body is an example of how to create a row with a link to the event image.

```
{{partnerUrl}}
```

and

```
{{partnerLogoUrl}}
```

are variables that, when the summary is generated from the template, will be replaced by the content they refer to.

## Available variables, when to use them and what they represent

| variable | content |
|---|---|
| contactEmail | The event's contact email (left blank if there is none) |
| contactInfo | True or False, depending on whether there is contact information |
| contactName | The event's contact name (left blank if there is none) |
| contactPhone | The event's contact phone number (left blank if there is none) |
| eventDate | Event dates, already formatted |
| eventDateStartYear | Year of the event start date in YYYY format |
| eventDateStartMonth | Month of the event start date in mm format (with leading zeros) |
| eventDateStartDay | Day of the event start date in dd format (with leading zeros) |
| eventDateStartHour | Hour of the event start date in HH format (24h with leading zeros) |
| eventDateStartMinute | Minute of the event start date in ii format (with leading zeros) |
| eventDateEndMonth | Same as for the start date |
| eventDateEndHour | Same as for the start date |
| eventDateEndMinute | Same as for the start date |
| eventTypeName | Event type |
| eventDateEndDay | Same as for the start date |
| eventDateEndYear | Same as for the start date |
| eventDescription | Full HTML description of the event shown on the home page of its website. It should be used with caution because it could break the template style if it contains inline styles or tables |
| eventIcsUrl | URL of the ICS file for integration with personal calendar applications |
| eventImageUrl | Main event image (left blank if there is none) |
| eventInscriptionUrl | URL of the event registration page, if the event is configured to accept attendees. Otherwise, it is left blank |
| eventMapUrl | URL of the event location provided by Google Maps |
| eventPlace | Event venue |
| eventPlaceDetail | If available, additional information about the event location |
| eventShortDescription | Short description of the event, if any (this content is not translatable in Symposium) |
| eventTitle | Event title |
| partnerLogoUrl | URL of the institution logo configured on the platform |
| partnerUrl | Partner URL, that is, the home page of the events platform |
| templateTitle | Name of this summary's template |
|  |  |

## Additional notes

Since Symposium uses Handlebars for this tool, it is possible to create a specific template that uses any logic Handlebars allows. For example, you can use

```
 {{#if}}
```

statements and variable calls

```
{{variable}}
```

and

```
{{{variable}}}
```

The latter when it contains HTML that must not be escaped.
