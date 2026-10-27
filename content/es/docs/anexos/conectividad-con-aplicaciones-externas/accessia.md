---
title: "Búsqueda de eventos"
weight: 1
lastmod: 2019-07-05T11:36:53Z
dokuwiki: accessia
---
Puedes consultar la nueva documentación de la API en la siguiente dirección: [apiportal.symposium.events](https://apiportal.symposium.events)

Para utilizarla, es necesario dar de alta API keys en el Panel de administración de la plataforma.

---

### Antigua API

<u>La documentación siguiente corresponde al antiguo método de consulta de eventos. Este método será eliminado en el futuro, por lo que aconsejamos reemplazar cualquier código antiguo por el nuevo.</u>

La API de Symposium proporciona una serie de servicios para que las aplicaciones externas puedan listar eventos, opcionalmente filtrados por parámetros.

## Accesia search (JSON) **NO UTILIZAR**

```
Petición GET: /search/doAccessiaJSON/<PARTNER>/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/<DATE>/EMPTY_PARAMETER/<TAG>
```

```
Respuesta: JSON
```

Parámetros (todos opcionales):

- partner = Identificador del partner
- id = Identificador del evento
- name = Título o Descripción del evento
- place = Lugar de celebración del evento
- category = Categoría del evento o Palabra clave (tag)
- dateIni = Fecha de inicio del evento. Formato: AAAA-MM-DD
- dateEnd = Fecha de fin del evento. Formato: AAAA-MM-DD
- tag = Palabra clave

## Accesia search (JSONP) **NO UTILIZAR**

```
Petición GET: /search/doAccessiaJSON2/<PARTNER>/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/EMPTY_PARAMETER/<DATE>/<TAG>
```

```
Respuesta: JSONP
```

Parámetros (todos opcionales):

- partner = Identificador del partner
- id = Identificador del evento
- name = Título o Descripción del evento
- place = Lugar de celebración del evento
- category = Categoría del evento
- dateEnd = Fecha de fin del evento. Formato: AAAA-MM-DD
- dateIni = Fecha de inicio del evento. Formato: AAAA-MM-DD
- tag = Palabra clave

## Events **NO UTILIZAR**

```
Petición POST: /api/events
```

```
Respuesta: JSON
```

Parámetros:

- paging_limit = Número máximo de resultados
- paging_offset = Elemento inicial de la búsqueda
- partner = Código del partner
- event_id = Identificador del evento
- title_desc = Título o Descripción del evento
- location = Lugar de celebración del evento
- since = Fecha de inicio del evento
- since_max = Fecha máxima de inicio del evento
- until = Fecha de fin del evento
- until_min = Fecha mínima de fin del evento
- organizer = Organizador del evento
- type = Tipo del evento
- category = Categoría del evento
- tag = Palabra clave del evento
- keyword = Búsqueda amplia en título, descripción, localización, categoría y palabra clave
