#!/usr/bin/env python3
"""One-shot import of the Symposium DokuWiki into this Hugo site.

Reads a DokuWiki data export (pages/, media/, meta/) and writes:

  content/es/docs/<part>/<group>/<page>.md   Spanish pages (default language)
  content/en/docs/...                        the few pages the wiki had in English
  static/media/<namespace>/<file>            only the media files that pages reference

The section tree is rebuilt from the wiki's own help indexes: `indicegeneral`
first, then `indice_general_crowdfunding`, then the partner indexes. A page is
placed where it first appears; partner-specific pages go to docs/instituciones/.

After the import, Markdown under content/ is the source of truth. Re-running the
script refuses to overwrite content/ unless --force is given; --force deletes
everything under content/{es,en}/docs/ except the hand-written docs/_index.md,
English translations included.

Usage:
  python3 scripts/dokuwiki2hugo.py /www/symposium/symposium_knowledge_base/src/dokuwiki [--force]
"""

import argparse
import os
import re
import shutil
import sys
import unicodedata
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Section tree ──────────────────────────────────────────────────────────────
# (regex on the index "==== part ====" heading, slug, es title, en title, weight)
PARTS = [
    (r"^Introducci", "introduccion", "Introducción", "Introduction", 1),
    (r"^Parte I\.", "administracion", "Panel de administración", "Administration panel", 10),
    (r"Gesti[oó]n Econ[oó]mica|contable", "gestion-economica", "Gestión económica", "Financial management", 20),
    (r"de un proyecto", "crowdfunding", "Crowdfunding", "Crowdfunding", 70),
    (r"de un evento", "eventos", "Creación y gestión de eventos", "Creating and managing events", 30),
    (r"Panel de usuario", "panel-de-usuario", "Panel de usuario", "User panel", 40),
    (r"Perspectiva", "uso-de-la-plataforma", "Uso de la plataforma", "Using the platform", 50),
    (r"Aplicaciones m[oó]viles", "apps-moviles", "Aplicaciones móviles", "Mobile apps", 60),
    (r"^Anexo", "anexos", "Anexos", "Appendices", 80),
    (r"^Novedades", "novedades", "Novedades", "What's new", 90),
]
INSTITUTIONS = ("instituciones", "Instituciones", "Institutions", 95)

# Partner indexes, in the order they are read. Value: partner display name.
PARTNER_INDEXES = {
    "indiceupf": "Universitat Pompeu Fabra", "indiceum": "Universidad de Murcia",
    "indiceull": "Universidad de La Laguna", "indiceucm": "Universidad Complutense de Madrid",
    "indiceupct": "Universidad Politécnica de Cartagena", "indiceurv": "Universitat Rovira i Virgili",
    "indiceusal": "Universidad de Salamanca", "indiceupsa": "Universidad Pontificia de Salamanca",
    "indiceenae": "ENAE Business School", "indiceunex": "Universidad de Extremadura",
    "indiceucam": "Universidad Católica de Murcia", "indicecrue": "CRUE Universidades Españolas",
}
PARTNER_SUFFIX = re.compile(r"_(um|upf|ull|ucm|upct|urv|usal|upsa|enae|unex|ucam|crue)$")

# Pages no index links to, placed by hand: id -> (folder under docs/, weight)
MANUAL = {
    "faq": ("", 85),
    "changelog": ("novedades", 1),
    "que_es_y_para_que_sirve": ("introduccion", 1),
    "tipos_de_usuario": ("introduccion", 2),
    "panel_de_administracion": ("administracion", 1),
    "accounting_units": ("gestion-economica/configuracion", 90),
    "cookie_consent": ("administracion/cobertura-legal", 90),
    "cookie_consent_crowdfunding": ("crowdfunding", 90),
    "editor_integrado": ("eventos/contenido", 90),
    "enviar_correo_donantes_crowdfunding": ("crowdfunding/difusion", 90),
    "informes_de_videoconferencias": ("eventos/herramientas", 90),
    "informes_de_videoconferencias_en_la_plataforma": ("administracion/herramientas", 90),
    "noticias_crowdfunding": ("crowdfunding/herramientas", 90),
    "paypal_developer": ("administracion/pagos", 90),
    "plantilla_personalizada_anexo": ("administracion/diseno", 90),
    "plantillas_de_resumen_evento": ("administracion/diseno", 91),
    "plantillas_responsivas": ("eventos/diseno", 90),
    "push_general": ("administracion/herramientas", 91),
    "resumen_prevision": ("eventos/presupuesto", 1),
    "registro_ingresos": ("eventos/presupuesto", 2),
    "registro_gastos": ("eventos/presupuesto", 3),
    "rss_faculties": ("administracion/configuracion", 90),
    "tus_eventos_online_zoom": ("eventos/creando-y-editando-un-evento", 90),
    "valoracion_rubrica": ("eventos/doc-cientifica", 90),
    "zoom_account_manager": ("administracion/herramientas", 92),
    "zoom_account_manager_extended": ("administracion/herramientas", 93),
    # Only partner indexes link these, under groups the general index lacks.
    "noticias_o_destacados": ("administracion/herramientas", 94),
    "panel_de_twitter": ("administracion/herramientas", 95),
    "configuracion_lopd": ("administracion/cobertura-legal", 91),
    "publicar_con_editum": ("eventos/doc-cientifica", 91),
    "configusuario_redessociales": ("panel-de-usuario/configuracion-de-usuario", 90),
}
# Per-page repairs of broken wiki source: id -> [(regex, replacement)]
FIXUPS = {
    # The editor collapsed half of the changelog into one line.
    "changelog": [(r"<nowiki>\s*//\*%%</nowiki>", "\n    * "), (r"\s*%%\*%%\s*", "\n    * "),
                  (r"\s*(={4,5} [^=]+ ={4,5})\s*", r"\n\n\1\n\n"), (r"\s*//\s*$", ""), (r"^\* ", "    * ")],
}
# Titles that read badly out of the wiki: id -> (title, linkTitle)
TITLES = {"faq": ("Preguntas frecuentes", None), "changelog": ("Novedades de la plataforma", "Historial de versiones")}
# Folders that only MANUAL pages create: folder -> (es title, en title, weight)
MANUAL_SECTIONS = {"eventos/presupuesto": ("Presupuesto", "Budget", 20)}
# Index pages: links to them become links to the matching section
INDEX_URLS = {"indicegeneral": "/docs", "indice_general_crowdfunding": "/docs/crowdfunding",
              "inicio": "/docs/instituciones", "indicegeneral_crowdfunding": "/docs/crowdfunding"}
SKIP_NAMESPACES = ("wiki", "playground")
# documentacion_recibida is an abandoned draft of comunicaciones_recibidas.
SKIP_PAGES = {"inicio", "indicegeneral", "indice_general_crowdfunding", "documentacion_recibida"}


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def page_slug(pid):
    return pid.split(":")[-1].replace("_", "-")


def anchor(a):
    return a.replace("_", "-") if a else ""


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


# ── Index parsing ─────────────────────────────────────────────────────────────
HEADING = re.compile(r"^\s*(={2,6})\s*(.+?)\s*={2,6}\s*$")
LINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")


def clean_id(target):
    target = target.strip().split("?")[0].split("#")[0].strip()
    return target.lstrip(":").replace(" ", "_").lower()


def parse_index(text):
    """Yield (part_title, group_title, page_id, label) in reading order."""
    part = group = None
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            level = len(m.group(1))
            if level >= 4:
                part, group = m.group(2).strip(), None
            else:
                group = m.group(2).strip()
            continue
        for lm in LINK.finditer(line):
            target = lm.group(1)
            if target.startswith("http") or "{{" in target:
                continue
            label = (lm.group(2) or "").strip()
            if "{{" in label:
                label = ""
            yield part, group, clean_id(target), label


def part_for(title):
    for rx, slug, es, en, w in PARTS:
        if title and re.search(rx, title):
            return slug, es, en, w
    return None


# ── Converter ─────────────────────────────────────────────────────────────────
class Converter:
    def __init__(self, src, force):
        self.src = src
        self.force = force
        self.pages = {}       # id -> raw text
        self.place = {}       # id -> dict(folder, weight, label)
        self.sections = {}    # folder -> dict(es, en, weight)
        self.media = set()
        self.warnings = []

    # pages ----------------------------------------------------------------
    def load(self):
        base = os.path.join(self.src, "pages")
        for dirpath, _, files in os.walk(base):
            for f in files:
                if not f.endswith(".txt"):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, f), base)[:-4]
                pid = rel.replace(os.sep, ":")
                if pid.split(":")[0] in SKIP_NAMESPACES:
                    continue
                with open(os.path.join(dirpath, f), encoding="utf-8") as fh:
                    self.pages[pid] = fh.read()

    def add_section(self, folder, es, en, weight):
        self.sections.setdefault(folder, {"es": es, "en": en, "weight": weight})

    def place_page(self, pid, folder, weight, label=""):
        if pid in self.place or pid not in self.pages or pid in SKIP_PAGES:
            return
        self.place[pid] = {"folder": folder, "weight": weight, "label": label}

    def build_tree(self):
        indexes = ["indicegeneral", "indice_general_crowdfunding"] + list(PARTNER_INDEXES)
        counters = {}
        for idx in indexes:
            forced = "crowdfunding" if idx == "indice_general_crowdfunding" else None
            for part, group, pid, label in parse_index(self.pages.get(idx, "")):
                if pid in PARTNER_INDEXES or PARTNER_SUFFIX.search(pid) or pid in MANUAL:
                    continue
                info = part_for(part)
                if forced:
                    info = next((slug, es, en, w) for _, slug, es, en, w in PARTS if slug == forced)
                if not info:
                    continue
                slug, es, en, w = info
                folder = slug
                if slug == "anexos":
                    group = re.sub(r"^(Anexo [IVX]+\.\s*)?(El |La )?", "", part).capitalize()
                if group:
                    folder = f"{slug}/{slugify(group)}"
                groups = counters.setdefault(("g", slug), {})
                gw = groups.setdefault(folder, len(groups) + 1)
                n = counters.setdefault(folder, 0) + 1
                counters[folder] = n
                if pid in self.place or pid not in self.pages or pid in SKIP_PAGES:
                    continue
                self.add_section(slug, es, en, w)
                if group:
                    self.add_section(folder, group, "", gw)
                self.place_page(pid, folder, n, label)
        for folder, (es, en, w) in MANUAL_SECTIONS.items():
            self.add_section(folder, es, en, w)
        for pid, (folder, w) in MANUAL.items():
            if folder:
                info = next(p for p in PARTS if p[1] == folder.split("/")[0])
                self.add_section(info[1], info[2], info[3], info[4])
                if folder not in self.sections:
                    sys.exit(f"MANUAL folder {folder} does not exist; add it to MANUAL_SECTIONS")
            self.place_page(pid, folder, w)
        # Partner indexes and partner-specific pages
        slug, es, en, w = INSTITUTIONS
        self.add_section(slug, es, en, w)
        for i, (idx, name) in enumerate(PARTNER_INDEXES.items(), 1):
            partner = idx[len("indice"):]
            self.add_section(f"{slug}/{partner}", name, name, i)
            self.place[idx] = {"folder": f"{slug}/{partner}", "weight": 0, "label": name, "index": True}
        for pid in sorted(self.pages):
            m = PARTNER_SUFFIX.search(pid)
            if m and pid not in self.place:
                self.place_page(pid, f"{slug}/{m.group(1)}", 50)
        for pid in sorted(self.pages):
            if pid.startswith("en:") or pid in self.place or pid in SKIP_PAGES:
                continue
            m = re.search(r"(um|upf)$", pid)
            if m:
                self.place_page(pid, f"{slug}/{m.group(1)}", 60)
            else:
                self.add_section("otros", "Otras páginas", "Other pages", 99)
                self.place_page(pid, "otros", 50)

    def url_for(self, pid):
        if pid in INDEX_URLS:
            return INDEX_URLS[pid]
        p = self.place.get(pid)
        if not p:
            return None
        if p.get("index"):
            return f"/docs/{p['folder']}"
        prefix = f"/docs/{p['folder']}/" if p["folder"] else "/docs/"
        return prefix + page_slug(pid)

    # inline -----------------------------------------------------------------
    def stash(self, value):
        self._stash.append(value)
        return f"\x00{len(self._stash) - 1}\x00"

    def unstash(self, text):
        for _ in range(5):
            text = re.sub(r"\x00(\d+)\x00", lambda m: self._stash[int(m.group(1))], text)
        return text

    def media_url(self, target):
        """'{{ :ns:file.png?nolink&250x80 |alt}}' target -> (url, width, is_image)."""
        raw, _, query = target.strip().partition("?")
        # Images inserted with the old ckgedit editor point at the wiki host;
        # the same files are in the media/ export.
        ck = re.search(r"/lib/plugins/ckgedit/fckeditor/userfiles/image/(.+)$", raw)
        if ck:
            raw = ck.group(1).replace("/", ":")
        if raw.startswith("http"):
            return raw, None, True
        mid = re.sub(r"^:+", "", raw).lower()
        path = mid.replace(":", "/")
        self.media.add(path)
        width = None
        m = re.search(r"(?:^|&)(\d+)(?:x\d+)?(?:&|$)", query)
        if m:
            width = m.group(1)
        is_image = bool(re.search(r"\.(png|jpe?g|gif|svg|webp)$", path))
        return f"/media/{path}", width, is_image

    def image(self, m):
        inner = m.group(1)
        target, _, alt = inner.partition("|")
        if not re.search(r"\.[a-zA-Z0-9]{2,4}(\?|\s*$)", target.strip()) and not target.strip().startswith(":"):
            return self.stash("{{" + inner + "}}")
        center = target.startswith(" ") and target.endswith(" ")
        url, width, is_image = self.media_url(target)
        if not is_image:
            return self.stash(f"[{alt.strip() or os.path.basename(url)}]({url})")
        params = []
        if width:
            params.append(f"w={width}")
        if center:
            params.append("align=center")
        q = ("?" + "&".join(params)) if params else ""
        return self.stash(f"![{alt.strip()}]({url}{q})")

    def link(self, m, pid):
        lm = LINK.match(m.group(0))
        target, text = (lm.group(1).strip(), lm.group(2)) if lm else (m.group(1).strip(), None)
        if text is not None:
            text = text.strip()
            text = re.sub(r"\{\{(.+?)\}\}", self.image, text)
            text = self.inline(text, pid) if "\x00" not in text else text
        if re.match(r"^(https?|ftp)://", target) or target.startswith("www."):
            url = target if not target.startswith("www.") else "https://" + target
            return self.stash(f"[{text}]({url})" if text else f"<{url}>")
        if re.match(r"^[^@\s]+@[^@\s]+\.[a-z]+$", target):
            return self.stash(f"[{text or target}](mailto:{target})")
        if target.startswith("#"):
            return self.stash(f"[{text or target[1:]}](#{anchor(target[1:])})")
        frag = target.split("#", 1)[1].split("?")[0] if "#" in target else ""
        tid = clean_id(target)
        url = self.url_for(tid)
        if not url:
            self.warnings.append(f"{pid}: broken link to '{tid}'")
            return self.stash(text or tid)
        label = text or self.place[tid].get("label") or self.title_of(tid)
        return self.stash(f"[{label}]({url}{'#' + anchor(frag) if frag else ''})")

    def inline(self, text, pid):
        text = re.sub(r"%%(.*?)%%", lambda m: self.stash(escape_html(m.group(1))), text)
        text = re.sub(r"<nowiki>(.*?)</nowiki>", lambda m: self.stash(escape_html(m.group(1))), text)
        text = re.sub(r"''(.+?)''", lambda m: self.stash("`" + m.group(1) + "`"), text)
        text = re.sub(r"<code>(.*?)</code>", lambda m: self.stash("`" + m.group(1) + "`"), text)
        text = re.sub(r"\[\[(.+?)\]\]", lambda m: self.link(m, pid), text)
        text = re.sub(r"\{\{(.+?)\}\}", self.image, text)
        text = re.sub(r"(?:https?|ftp)://[^\s<>\]\[|\"')]+", lambda m: self.stash(m.group(0)), text)
        text = re.sub(r"</?font[^>]*>|</?center>", "", text)
        text = re.sub(r"<(/?)(del|sub|sup|u|b|i|em|strong)>", lambda m: self.stash(m.group(0)), text)
        text = text.replace("<br>", self.stash("<br>")).replace("<br/>", self.stash("<br>"))
        text = re.sub(r"<(?=[A-Za-z/!?])", "&lt;", text)
        text = re.sub(r"(?<!:)//(.+?)(?<!:)//", r"*\1*", text)
        text = re.sub(r"__(.+?)__", r"<u>\1</u>", text)
        # DokuWiki tolerates "** bold **"; CommonMark does not.
        text = re.sub(r"\*\*\s*([^*]+?)\s*\*\*", r"**\1**", text)
        text = re.sub(r"\s*\\\\(\s+|$)", lambda m: self.stash("<br>") + (" " if m.group(1) else ""), text)
        return text

    def title_of(self, pid):
        m = re.search(r"^\s*======\s*(.+?)\s*======", self.pages.get(pid, ""), re.M)
        if m:
            return m.group(1).strip()
        p = self.place.get(pid, {})
        return p.get("label") or pid.split(":")[-1].replace("_", " ").capitalize()

    # blocks -----------------------------------------------------------------
    def convert(self, pid):
        self._stash = []
        text = self.pages[pid].replace("\r\n", "\n").replace("​", "")
        for rx, repl in FIXUPS.get(pid, []):
            text = re.sub(rx, repl, text, flags=re.M)
        meta = {}
        if "~~NOTOC~~" in text:
            meta["toc"] = "false"
            text = text.replace("~~NOTOC~~", "")

        # Multi-line code and html blocks first, so nothing inside them is touched.
        def code_block(m):
            lang = (m.group(2) or "").strip().split()[0] if m.group(2) else ""
            body = m.group(3).strip("\n")
            body = body.replace("{{<", "{{</*").replace("{{%", "{{%/*")
            return "\n" + self.stash(f"```{lang}\n{body}\n```") + "\n"
        text = re.sub(r"<(code|file)([^>]*)>(.*?)</\1>",
                      lambda m: code_block(m) if "\n" in m.group(3) else m.group(0), text, flags=re.S)
        text = re.sub(r"<html>(.*?)</html>",
                      lambda m: "\n" + self.stash("```html\n" + m.group(1).strip("\n") + "\n```") + "\n", text, flags=re.S)

        # "Ir al Índice General..." back-links: the sidebar replaces them.
        text = re.sub(r"^\s*\[\[:?(indicegeneral|indice_general_crowdfunding|indicegeneral_crowdfunding|inicio)(\|[^\]]*)?\]\]\s*(\\\\)?\s*$",
                      "", text, flags=re.M | re.I)
        title = None
        lines = text.split("\n")
        levels = [len(m.group(1)) for m in (HEADING.match(l) for l in lines) if m]
        if levels and levels[0] == 6:
            title = HEADING.match(next(l for l in lines if HEADING.match(l))).group(2).strip()
        body_levels = levels[1:] if title else levels
        top = max(body_levels) if body_levels else 5

        out, i, in_list = [], 0, False
        title_done = False
        while i < len(lines):
            line = lines[i]
            hm = HEADING.match(line)
            if hm and not hm.group(2).strip("= "):
                i += 1  # "=====   =====": empty heading
                continue
            if hm:
                lvl = len(hm.group(1))
                if title and not title_done and lvl == 6:
                    title_done = True
                    i += 1
                    continue
                depth = min(6, 2 + (top - lvl)) if lvl <= top else 2
                out += ["", "#" * depth + " " + self.inline(hm.group(2).strip(), pid), ""]
                in_list = False
                i += 1
                continue
            if re.match(r"^\s*[|^]", line):
                rows = []
                while i < len(lines) and re.match(r"^\s*[|^]", lines[i]):
                    rows.append(lines[i].strip())
                    i += 1
                out += [""] + self.table(rows, pid) + [""]
                in_list = False
                continue
            # A "* " at column 0 is not a DokuWiki list, but Markdown would make
            # it one anyway; levels are relative to the first item of the list.
            lm = re.match(r"^( {2,}|\t+)?([*-])\s+(.*)$", line)
            if lm and (lm.group(1) or (lm.group(2) == "*" and not line.startswith("**"))):
                indent = len((lm.group(1) or "").expandtabs(2))
                if not in_list:
                    base = indent
                    out.append("")
                level = max(1, 1 + (indent - base) // 2)
                marker = "-" if lm.group(2) == "*" else "1."
                out.append("   " * (level - 1) + marker + " " + self.inline(lm.group(3).strip(), pid))
                in_list = True
                i += 1
                continue
            if re.match(r"^( {2,}|\t)\S", line) and "\x00" not in line:
                block = []
                while i < len(lines) and (re.match(r"^( {2,}|\t)", lines[i]) or not lines[i].strip()) \
                        and not re.match(r"^( {2,}|\t+)[*-]\s", lines[i]):
                    block.append(lines[i])
                    i += 1
                while block and not block[-1].strip():
                    block.pop()
                body = "\n".join(l[2:] if l.startswith("  ") else l.lstrip("\t") for l in block)
                body = body.replace("{{<", "{{</*").replace("{{%", "{{%/*")
                out += ["", self.stash("```text\n" + body + "\n```"), ""]
                in_list = False
                continue
            if re.match(r"^\s*-{4,}\s*$", line):
                out += ["", "---", ""]
                in_list = False
                i += 1
                continue
            stripped = line.strip()
            if not stripped or re.fullmatch(r"(\\\\\s*)+", stripped):
                out.append("")
                in_list = False
                i += 1
                continue
            if in_list:
                out.append("")
                in_list = False
            if stripped.startswith(">"):
                q = re.match(r"^(>+)\s*(.*)$", stripped)
                out.append("> " * len(q.group(1)) + self.inline(q.group(2), pid))
            else:
                out.append(self.inline(stripped, pid))
            i += 1

        md = "\n".join(out)
        md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
        md = self.unstash(md)
        return title, meta, md

    def table(self, rows, pid):
        parsed = []
        for row in rows:
            protected = self.inline(row, pid)
            protected = re.sub(r"\s*<br>\s*", "<br>", self.unstash_br(protected))
            cells = re.findall(r"([|^])([^|^]*)", protected)
            if cells and not cells[-1][1].strip():
                cells = cells[:-1]
            parsed.append([(sep == "^", c.strip().replace(":::", "")) for sep, c in cells])
        ncols = max(len(r) for r in parsed)
        lines = []
        header = parsed[0] if all(h for h, _ in parsed[0]) else None
        body = parsed[1:] if header else parsed

        def fmt(r):
            cells = [c for _, c in r] + [""] * (ncols - len(r))
            return "| " + " | ".join(cells) + " |"
        lines.append(fmt(header) if header else "|" + " |" * ncols)
        lines.append("|" + "---|" * ncols)
        lines += [fmt(r) for r in body]
        return lines

    def unstash_br(self, text):
        return re.sub(r"\x00(\d+)\x00", lambda m: self._stash[int(m.group(1))]
                      if self._stash[int(m.group(1))] == "<br>" else m.group(0), text)

    # output -----------------------------------------------------------------
    def lastmod(self, pid):
        f = os.path.join(self.src, "meta", pid.replace(":", os.sep) + ".changes")
        try:
            with open(f, encoding="utf-8") as fh:
                ts = int(fh.read().strip().splitlines()[-1].split("\t")[0])
            return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except (OSError, IndexError, ValueError):
            return None

    def write(self, lang, rel, fm, body):
        path = os.path.join(ROOT, "content", lang, "docs", rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        lines = ["---"] + [f"{k}: {v}" for k, v in fm.items() if v is not None] + ["---", ""]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + body)

    def run(self):
        out_es = os.path.join(ROOT, "content", "es", "docs")
        if os.path.exists(out_es) and not self.force:
            sys.exit(f"{out_es} exists; Markdown is now the source of truth. Use --force to overwrite.")
        for lang in ("es", "en"):
            docs = os.path.join(ROOT, "content", lang, "docs")
            for entry in os.listdir(docs) if os.path.isdir(docs) else []:
                if entry != "_index.md":
                    full = os.path.join(docs, entry)
                    shutil.rmtree(full) if os.path.isdir(full) else os.remove(full)
        self.load()
        self.build_tree()

        for folder, s in sorted(self.sections.items()):
            for lang in ("es", "en"):
                if lang == "en" and folder.startswith(INSTITUTIONS[0]):
                    continue  # partner-specific legacy pages stay Spanish-only
                title = s[lang] or s["es"]
                fm = {"title": yaml_str(title), "weight": s["weight"]}
                if lang == "en" and not s["en"]:
                    fm["title"] = yaml_str(s["es"])
                self.write(lang, f"{folder}/_index.md", fm, "{{< section-cards >}}\n")

        for pid, p in sorted(self.place.items()):
            title, meta, md = self.convert(pid)
            title = title or p.get("label") or self.title_of(pid)
            t_over, link_title = TITLES.get(pid, (None, None))
            title = t_over or title
            fm = {"title": yaml_str(title), "linkTitle": yaml_str(link_title) if link_title else None,
                  "weight": p["weight"], "lastmod": self.lastmod(pid),
                  "dokuwiki": pid}
            fm.update(meta)
            if p.get("index"):
                s = self.sections[p["folder"]]
                fm.update({"title": yaml_str(s["es"]), "weight": s["weight"]})
                self.write("es", f"{p['folder']}/_index.md", fm, md + "\n{{< section-cards >}}\n")
                continue
            rel = f"{p['folder']}/{page_slug(pid)}.md" if p["folder"] else f"{page_slug(pid)}.md"
            self.write("es", rel, fm, md)
            en_id = "en:" + pid
            if en_id in self.pages:
                self.pages[pid] = self.pages[en_id]
                t, m2, md2 = self.convert(pid)
                fm2 = dict(fm, title=yaml_str(t or title), lastmod=self.lastmod(en_id), dokuwiki=en_id)
                self.write("en", rel, fm2, md2)

        copied, missing = 0, []
        for path in sorted(self.media):
            src = os.path.join(self.src, "media", path)
            if not os.path.isfile(src):
                missing.append(path)
                continue
            dst = os.path.join(ROOT, "static", "media", path)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            copied += 1

        print(f"pages: {len(self.place)}  sections: {len(self.sections)}  media copied: {copied}")
        for w in self.warnings:
            print("WARN", w)
        for path in missing:
            print("WARN missing media", path)
        others = [pid for pid, p in self.place.items() if p["folder"] == "otros"]
        if others:
            print("unplaced (docs/otros):", " ".join(sorted(others)))


def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") \
        .replace("&amp;lt;", "&lt;").replace("&amp;gt;", "&gt;").replace("&amp;amp;", "&amp;")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", help="DokuWiki data directory (contains pages/, media/, meta/)")
    ap.add_argument("--force", action="store_true", help="overwrite content/ generated by a previous run")
    args = ap.parse_args()
    Converter(args.src, args.force).run()
