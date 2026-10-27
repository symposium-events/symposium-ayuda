---
title: "Event search"
weight: 1
lastmod: 2019-07-05T11:36:53Z
dokuwiki: accessia
---
You can read the new API documentation at the following address: [apiportal.symposium.events](https://apiportal.symposium.events)

To use it, API keys must be created in the platform's Administration panel.

---

### Old API

<u>The following documentation describes the old method for querying events. This method will be removed in the future, so we advise replacing any old code with the new one.</u>

The Symposium API provides a set of services so that external applications can list events, optionally filtered by parameters.

## Accesia search (JSON) **DO NOT USE**

```
Petición GET: /search/doAccessiaJSON/<PARTNER>/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/<DATE>/EMPTY_PARAMETER/<TAG>
```

```
Respuesta: JSON
```

Parameters (all optional):

- partner = Partner identifier
- id = Event identifier
- name = Event title or description
- place = Event venue
- category = Event category or keyword (tag)
- dateIni = Event start date. Format: YYYY-MM-DD
- dateEnd = Event end date. Format: YYYY-MM-DD
- tag = Keyword

## Accesia search (JSONP) **DO NOT USE**

```
Petición GET: /search/doAccessiaJSON2/<PARTNER>/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/<DATE>/<TAG>
```

```
Respuesta: JSONP
```

Parameters (all optional):

- partner = Partner identifier
- id = Event identifier
- name = Event title or description
- place = Event venue
- category = Event category
- dateEnd = Event end date. Format: YYYY-MM-DD
- dateIni = Event start date. Format: YYYY-MM-DD
- tag = Keyword

## Events **DO NOT USE**

```
Petición POST: /api/events
```

```
Respuesta: JSON
```

Parameters:

- paging_limit = Maximum number of results
- paging_offset = Starting item of the search
- partner = Partner code
- event_id = Event identifier
- title_desc = Event title or description
- location = Event venue
- since = Event start date
- since_max = Latest event start date
- until = Event end date
- until_min = Earliest event end date
- organizer = Event organizer
- type = Event type
- category = Event category
- tag = Event keyword
- keyword = Broad search across title, description, location, category and keyword
