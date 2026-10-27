# Ayuda de Symposium

Manual de ayuda de [Symposium](https://symposium.events), la plataforma de gestión de eventos académicos y
científicos. Sitio estático hecho con [Hugo](https://gohugo.io) y el tema
[hextra](https://imfing.github.io/hextra/), adaptado a la identidad visual de Symposium.

Sustituye al antiguo DokuWiki de ayuda, del que se importó todo el contenido el 2026-10-27.

- Español (idioma por defecto): `/`
- English: `/en/`

## Requisitos

- Hugo **extended** ≥ 0.146 (probado con 0.160.1).
- Nada más: el tema está vendorizado en `_vendor/`, no hace falta Go ni Node.

## Uso

```sh
hugo server            # http://localhost:1313  ·  http://localhost:1313/en/
hugo --gc --minify     # genera el sitio en ./public
python3 scripts/check-links.py   # tras el build: enlaces internos y anclas rotas
```

## Publicación

Cada push a `main` construye y publica el sitio en GitHub Pages con GitHub Actions
(`.github/workflows/pages.yaml`). La pipeline falla si hay enlaces internos o anclas rotas. Al crear el
repositorio en GitHub hay que activar *Settings → Pages → Source: GitHub Actions*; para un dominio propio,
añade `static/CNAME`.

## Escribir y editar contenido

Las páginas están en `content/es/docs/` y su traducción en `content/en/docs/`, **con la misma ruta de
fichero**. El orden del menú lateral lo marca `weight` en el *front matter*.

```sh
hugo new content docs/eventos/herramientas/mi-pagina.md          # español
hugo new content --contentDir content/en docs/eventos/herramientas/mi-pagina.md   # inglés
```

Imágenes: `![texto](/media/carpeta/imagen.png?w=500&align=center)` (ficheros en `static/media/`), o junto a
la página si se usa un *page bundle*. Enlaces internos: `/docs/ruta/de/la/pagina#ancla`.

Los enlaces apuntan siempre a contenido de este sitio, nunca al wiki antiguo ni a Freshdesk; los ficheros
descargables están en `static/descargas/`. Las normas completas (traducción, vocabulario oficial, anclas, diseño) están en [AGENTS.md](AGENTS.md).

## Estructura

```
content/{es,en}/        contenido por idioma
  docs/                 el manual (partes → grupos → páginas)
i18n/{es,en}.yaml       textos de la interfaz
data/sections.yaml      secciones de la portada
data/icons.yaml         iconos de la web corporativa (sym-*)
layouts/                sobrescrituras de hextra (portada, pie, imágenes, shortcodes)
assets/css/symposium/   design system: fuentes, tokens de color, componentes
static/                 logos, fuentes, favicon y media importada del wiki
scripts/                importador DokuWiki → Hugo y comprobador de enlaces
_vendor/                hextra v0.12.2 (no editar)
```

## Importación desde DokuWiki

`scripts/dokuwiki2hugo.py` convirtió el volcado del wiki
(`/www/symposium/symposium_knowledge_base/src/dokuwiki`). Desde entonces el Markdown de `content/` es la
fuente de verdad: **no vuelvas a ejecutarlo con `--force`**, borraría `content/*/docs/` (traducciones
incluidas). Cada página conserva `dokuwiki: <id>` para trazarla con el wiki original.
