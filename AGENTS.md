# AGENTS.md · Symposium help site (symposium-ayuda)

Help manual for **Symposium**, the multi-tenant SaaS platform for academic and scientific events
(registration, payments, papers, websites) run by Digio since 2007. This repository is a static
[Hugo](https://gohugo.io) site that replaces the old partner-facing DokuWiki
(`ayuda.symposium.emagister.com` / `demopremium.symposium.events/ayuda-symposium`).

Audience: event organisers, platform administrators (partners: universities and institutions),
economic managers, attendees and authors. Not developers: never document internals here.

## Stack

- **Hugo extended ≥ 0.146** (developed with 0.160.1). No Node, no Go required.
- Theme **[hextra](https://imfing.github.io/hextra/docs/) v0.12.2** as a Hugo module, **vendored** in
  `_vendor/github.com/imfing/hextra` (`_vendor/modules.txt`), so builds work offline and without Go.
  To upgrade it you need Go: `hugo mod get github.com/imfing/hextra@vX.Y.Z && hugo mod vendor`.
- **Never edit `_vendor/`.** Customise by overriding at project level (Hugo looks up project files first).

## Tasks

```sh
hugo server                    # http://localhost:1313 (es) and http://localhost:1313/en/ (en)
hugo --gc --minify             # build into ./public (git-ignored)
hugo new content docs/eventos/herramientas/mi-pagina.md   # new page (then add the en/ twin)
```

Before finishing any change run `hugo --gc --minify` and check it ends with no `ERROR` and no new `WARN`
(the `deprecated` warnings about `.Site.Data`/`.Site.Languages`/`.Site.Sites` come from hextra itself).

## Languages

- **Spanish is the default** (`content/es/`, served without prefix). **English** in `content/en/`, served under `/en/`.
- A translation is the **same relative file path** in the other language tree: that is how Hugo links
  both versions and how the language switcher finds the twin. Never rename a file in one language only.
- File names and folder names are Spanish slugs in both languages (URLs: `/docs/eventos/...` and
  `/en/docs/eventos/...`). Translate `title`/`linkTitle`, not paths.
- Every UI string lives in `i18n/es.yaml` and `i18n/en.yaml` (add the key to both). Menu labels are looked
  up by menu `identifier`. No hardcoded copy in templates.
- `data/sections.yaml` holds the home tiles; texts are `{es, en}` maps.
- `docs/instituciones/` (old partner-specific indexes and pages) is **Spanish only** by decision; do not
  create English twins for it.

### Translation rules (es → en)

- Product vocabulary: use the product's own English UI labels. Sources, in this order:
  1. `/www/symposium/symposium/system/application/i18n/en/LC_MESSAGES/symposium.po` — official gettext
     catalogue (Spanish `msgid` → English `msgstr`). When the Spanish text names a menu, button or
     field (usually in **bold**), grep its `msgid` and use the `msgstr` verbatim.
  2. `/www/symposium/symposium_knowledge_base/docs/vocabulary-index.md` and `docs/glossary.md`.
- Core terms: evento → event; organizador → organizer; inscripción → registration; inscrito/asistente →
  attendee; entrada → ticket; receptor de pago → payment receiver; panel de gestión económica → financial
  management panel; comunicación (científica) → paper/submission; comité → committee; ponente → speaker;
  plantilla → template; administrador de la plataforma → platform administrator;
  difusión → promotion; factura → invoice; recibo → receipt; temática → topic.
- US spelling (organizer, customize), as in the product UI.
- Keep front matter keys (`weight`, `lastmod`, `dokuwiki`, `toc`) unchanged; translate `title`/`linkTitle`.
- Keep links (`/docs/...`) and image paths (`/media/...?w=...&align=...`) exactly as in Spanish.
- **Anchors**: links like `/docs/faq#borrando-un-evento` target the Spanish heading id. In the English page,
  keep that id on the translated heading: `## Deleting an event {#borrando-un-evento}`. Do it for every
  heading that some page links to with `#...` (grep `content/es` for `#<id>)`).
- Screenshots are of the Spanish UI; keep them (do not remove images).

## Content structure

```
content/<lang>/
  _index.md                     home (layout: layouts/home.html)
  docs/_index.md                manual landing (hand-written)
  docs/<part>/_index.md         part: introduccion, administracion, gestion-economica, eventos,
                                panel-de-usuario, uso-de-la-plataforma, apps-moviles, crowdfunding,
                                anexos, novedades, instituciones
  docs/<part>/<group>/_index.md group inside a part (e.g. eventos/asistentes)
  docs/<part>/<group>/<page>.md page; file name = DokuWiki page id with "_" → "-"
  docs/faq.md
```

- Order is the `weight` front matter (copied from the order of the wiki's own indexes).
- Section `_index.md` files only contain `{{< section-cards >}}`, which renders their children as tiles.
- Every imported page keeps `dokuwiki: <page id>` (traceability to the old wiki) and `lastmod` = date of
  its last wiki edit. When you edit a page, update `lastmod` to the current date or remove it.

### Markdown conventions

- Images: `![alt](/media/<namespace>/<file>.png?w=400&align=center)`. Files live in `static/media/`.
  `w` (width in px) and `align=center` are read by `layouts/_markup/render-image.html` and stripped from
  the URL. Prefer page bundles (`page/index.md` + images) for new pages.
- Internal links: absolute content paths `/docs/eventos/asistentes/inscripcion#validacion`; hextra's link
  hook resolves them per language and base path.
- **Links must point to this site's own content.** Never link to the old DokuWiki
  (`ayuda.symposium.emagister.com`, `demopremium.symposium.events/ayuda-symposium`, `doku.php`), old domains
  (`sym.posium.com`) or Freshdesk solution articles: bring that content into a page here and link to it.
  There are no redirects from old URLs by decision. Downloadable files (CSV/PSD templates) live in
  `static/descargas/` and are linked as `/descargas/<file>`.
- hextra shortcodes are available: `callout`, `cards`/`card`, `steps`, `tabs`, `details`, `icon`, `badge`, `filetree`.
  Icons: hextra heroicons plus `sym-*` from `data/icons.yaml`.

## Design system (Symposium brand)

Taken from https://symposium.events (logo, WordPress child theme, Google Fonts):

- Colours (`assets/css/symposium/10-tokens.css`): orange `#F86A00` (primary), flame `#FF4301`,
  magenta `#D0005B`, violet `#4D13BC`, blue `#0F97D6`, ink `#343A40`; gradient `#F37335 → #FDC830`;
  brand gradient violet → magenta → flame → orange (hero, navbar strip).
- hextra primary colour is set in `assets/css/custom.css` (HSL 25° 100%, darker in light mode for AA contrast).
- Fonts (self-hosted, `static/fonts/`, `assets/css/symposium/00-fonts.css`): **Ubuntu** for headings,
  **Open Sans** for text.
- Favicons (`static/favicon*`, `apple-touch-icon.png`, `android-chrome-*`) are rendered from the logo mosaic and
  replace hextra's.
- Logo: `static/images/brand/symposium-logo.svg` (+ `-dark.svg`, wordmark in white). The diamond mosaic
  of the logo is `layouts/_partials/svg/mosaic.html`.
- Icons: the line icons of the corporate site, in `data/icons.yaml` (`sym-calendar`, `sym-payments`, …).

Overrides on top of hextra:

| File | Purpose |
|---|---|
| `layouts/home.html` | Home: hero + section tiles from `data/sections.yaml` |
| `layouts/_partials/custom/head-end.html` | Loads `assets/css/symposium/*.css` concatenated as `css/symposium.css` |
| `layouts/_partials/custom/footer.html` | Brand footer |
| `layouts/_partials/svg/mosaic.html` | Logo mosaic used in the hero |
| `layouts/_markup/render-image.html` | hextra image hook + `?w=`/`align=center` |
| `layouts/_shortcodes/section-cards.html` | Tiles for a section's children |
| `assets/css/custom.css` | hextra variables only |
| `assets/css/symposium/*.css` | Brand tokens, base typography, components (concatenated by file name) |

Every URL must work under a sub-path: use `relURL`, `relLangURL`, `.RelPermalink`.

## The DokuWiki import

`scripts/dokuwiki2hugo.py` converted the wiki export at
`/www/symposium/symposium_knowledge_base/src/dokuwiki` (pages, media, meta) on 2026-10-27. It rebuilds the
section tree from the wiki's indexes (`indicegeneral`, `indice_general_crowdfunding`, partner `indice*`),
places orphan pages through its `MANUAL` table, copies only referenced media and records broken links.

**Markdown in `content/` is now the source of truth.** Do not re-run the importer with `--force`: it wipes
`content/{es,en}/docs/` (except `docs/_index.md`), English translations included. Keep it only as
documentation of how each page was produced, or to re-import into a scratch checkout for comparison.

Known import leftovers: the wiki's content is largely stale (most pages last edited 2013–2021); some
screenshots show old UIs; `archivos_asistentes/componente_noticias2_1.png` is missing from the export;
partner indexes link to a page that never existed (`panel_de_actividad_global`).

## Context: the Symposium project

- Product knowledge base (English, evidence-backed): `/www/symposium/symposium_knowledge_base`
  (start at `docs/onboarding.md`; feature pages under `docs/domains/`). Use it to check whether a feature
  described in the old wiki still exists before rewriting a page.
- Application code: `/www/symposium/symposium` (Classic, CodeIgniter/PHP) and
  `/www/symposium/symposium-symfony` (Core).
- Infrastructure / deployments: `/www/symposium/symposium-devops`.

## Deployment (GitHub Actions → GitHub Pages)

`.github/workflows/pages.yaml`, same scheme as `pando-docs` and `sevir.org`:

- On every push to `main` (and `workflow_dispatch`): checks links/anchors on a build with `--baseURL /`
  (`scripts/check-links.py`), builds with `--baseURL` from `actions/configure-pages`, uploads `public/` and
  deploys with `actions/deploy-pages`. Pull requests run the checks and build only.
- One-time setup in the GitHub repository: Settings → Pages → Source: **GitHub Actions**.
- Custom domain: add `static/CNAME` with the domain and set it in Settings → Pages; `baseURL` in `hugo.toml`
  is only the local default.
- Hugo version is pinned in the workflow (`0.160.1`); keep it in sync with the version you develop with.
- A broken internal link or anchor fails the build.

## Git

- Commit messages in English, conventional style (`docs:`, `feat(theme):`, `fix:`…).
- Never rebase or cherry-pick to linearise history; integrate remote changes with merge.
- `public/` and `resources/_gen/` are build output and git-ignored.
