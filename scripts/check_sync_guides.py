#!/usr/bin/env python3
"""Check both synchronization guides in every language after mkdocs build."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CONFIG = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
LANGUAGES = {"it", "en", "fr", "de", "es", "pt-BR", "pt-PT"}
PAGES = ("sections/hero-sync", "companion/dndino-sync")
BASE_URL = CONFIG["site_url"]
BASE_PATH = urlsplit(BASE_URL).path


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links = []
        self.anchors = set()
        self.titles = []
        self.in_title = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.anchors.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "h1":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.titles.append(data)


def navigation_paths(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from navigation_paths(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from navigation_paths(item)


i18n = next(plugin["i18n"] for plugin in CONFIG["plugins"] if isinstance(plugin, dict) and "i18n" in plugin)
assert {entry["locale"] for entry in i18n["languages"]} == LANGUAGES
for entry in i18n["languages"]:
    nav = list(navigation_paths(entry["nav"]))
    for page in PAGES:
        assert nav.count(page + ".md") == 1, (entry["locale"], page, "navigation")

for page in PAGES:
    titles = set()
    for language in sorted(LANGUAGES):
        suffix = "" if language == "en" else "." + language
        source = ROOT / "docs" / (page + suffix + ".md")
        text = source.read_text()
        assert "iOS/iPadOS 26" in text and "!!! info" in text, source
        assert all(str(number) + ". " in text for number in range(1, 6)), source
        locale_path = "" if language == "en" else language + "/"
        url = urljoin(BASE_URL, locale_path + page + "/")
        output = SITE / locale_path / page / "index.html"
        rendered = Page(output.read_text())
        title = "".join(rendered.titles).strip()
        assert title and title not in titles, (language, page, "missing localized title")
        titles.add(title)
        peer = PAGES[1] if page == PAGES[0] else PAGES[0]
        peer_url = urljoin(BASE_URL, locale_path + peer + "/")
        assert peer_url in [urljoin(url, link) for link in rendered.links], (language, page, "cross-link")
        for link in rendered.links:
            target = urlsplit(urljoin(url, link))
            if target.netloc != urlsplit(BASE_URL).netloc or not target.path.startswith(BASE_PATH):
                continue
            local = SITE / unquote(target.path[len(BASE_PATH):])
            if local.is_dir():
                local /= "index.html"
            assert local.is_file(), (output, link, "missing target")
            if target.fragment and local.suffix == ".html":
                assert unquote(target.fragment) in Page(local.read_text()).anchors, (output, link, "missing anchor")

print("PASS: 14 localized guides, both navigation entries, requirements, steps, cross-links and all rendered internal links/anchors.")
