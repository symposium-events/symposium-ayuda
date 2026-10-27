#!/usr/bin/env python3
"""Check internal links and #anchors in the built site (./public).

Run after `hugo --gc --minify`. Reports links to pages that do not exist and
fragments that match no id on the target page. Exit status 1 if any is found.

Usage: python3 scripts/check-links.py [public_dir]
"""

import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links = set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.links.append(a["src"])


def target_file(public, path):
    path = unquote(path)
    full = os.path.join(public, path.lstrip("/"))
    if os.path.isdir(full):
        full = os.path.join(full, "index.html")
    return full


def main():
    public = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "public")
    pages = {}
    for dirpath, _, files in os.walk(public):
        for f in files:
            if f.endswith(".html"):
                p = os.path.join(dirpath, f)
                c = Collector()
                with open(p, encoding="utf-8") as fh:
                    c.feed(fh.read())
                pages[p] = c

    problems = []
    for page, c in pages.items():
        rel_page = os.path.relpath(page, public)
        for href in c.links:
            u = urlparse(href)
            if u.scheme or href.startswith("//") or href.startswith("mailto:"):
                continue
            if u.path:
                if not u.path.startswith("/"):
                    continue  # relative links: hextra internals only
                tgt = target_file(public, u.path)
                if not os.path.exists(tgt):
                    problems.append(f"{rel_page}: missing {u.path}")
                    continue
            else:
                tgt = page
            if u.fragment and tgt.endswith(".html"):
                ids = pages.get(tgt).ids if tgt in pages else set()
                if unquote(u.fragment) not in ids:
                    problems.append(f"{rel_page}: missing anchor {u.path or ''}#{u.fragment}")

    for p in sorted(set(problems)):
        print(p)
    print(f"checked {len(pages)} pages, {len(set(problems))} problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
