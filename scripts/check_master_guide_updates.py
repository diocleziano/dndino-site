#!/usr/bin/env python3
"""Validate the localized Master guide updates after a local MkDocs build.

Coverage markers provide traceability, not proof of the app's runtime behavior.
"""
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CONFIG = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
BASE_URL = CONFIG["site_url"]
BASE_PATH = urlsplit(BASE_URL).path
LANGUAGES = ("it", "en", "de", "fr", "es", "pt-BR", "pt-PT")
COVERAGE = {
    "homepage": {"MOD-144"},
    "places": {"MOD-015", "MOD-016", "MOD-018", "MOD-031", "MOD-035", "MOD-036", "MOD-087"},
    "characters": {"MOD-021", "MOD-022", "MOD-031", "MOD-063", "MOD-064", "MOD-065"},
    "topbar": {"MOD-023", "MOD-024", "MOD-025", "MOD-034", "MOD-038", "MOD-039", "MOD-044", "MOD-045", "MOD-048", "MOD-054", "MOD-067", "MOD-069"},
    "settings": {"MOD-042", "MOD-043", "MOD-049", "MOD-051", "MOD-060", "MOD-061", "MOD-062", "MOD-070", "MOD-071", "MOD-073", "MOD-077", "MOD-078", "MOD-079", "MOD-080", "MOD-086", "MOD-088"},
    "combat": {"MOD-025", "MOD-026", "MOD-028", "MOD-029", "MOD-030", "MOD-039", "MOD-044", "MOD-055", "MOD-058", "MOD-059", "MOD-063", "MOD-069", "MOD-081", "MOD-082", "MOD-083", "MOD-088"},
    "official-content": {"MOD-009", "MOD-010", "MOD-013"},
    "interactive-maps": {"MOD-019", "MOD-020"},
    "live-session": {"MOD-026", "MOD-027", "MOD-028", "MOD-029", "MOD-030"},
    "import-export": {"MOD-063"},
    "adventure": {"MOD-014", "MOD-028", "MOD-029", "MOD-030", "MOD-065"},
}

# Labels match the app catalogs when MOD-088 was documented. Check rendered prose too.
PLAYER_SCREEN_LABELS = {
    "it": [
        "Gestione secondo schermo",
        "Visibilità giocatori",
        "Ripristina opzioni dello schermo",
        "Mostra a tutti",
        "Nascondi a tutti",
        "Misto"
    ],
    "en": [
        "Second-screen management",
        "Player visibility",
        "Reset screen options",
        "Show for all",
        "Hide for all",
        "Mixed"
    ],
    "de": [
        "Zweiten Bildschirm verwalten",
        "Spielersichtbarkeit",
        "Bildschirmoptionen zurücksetzen",
        "Für alle anzeigen",
        "Für alle ausblenden",
        "Gemischt"
    ],
    "fr": [
        "Gestion du second écran",
        "Visibilité pour les joueurs",
        "Réinitialiser les options d'écran",
        "Afficher pour tous",
        "Masquer pour tous",
        "Mixte"
    ],
    "es": [
        "Gestión de segunda pantalla",
        "Visibilidad para jugadores",
        "Restablecer opciones de pantalla",
        "Mostrar para todos",
        "Ocultar para todos",
        "Mixto"
    ],
    "pt-BR": [
        "Gerenciar segunda tela",
        "Visibilidade para jogadores",
        "Restaurar opções da tela",
        "Mostrar para todos",
        "Ocultar para todos",
        "Misto"
    ],
    "pt-PT": [
        "Gerir segundo ecrã",
        "Visibilidade para jogadores",
        "Repor opções do ecrã",
        "Mostrar para todos",
        "Ocultar para todos",
        "Misto"
    ]
}


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links = []
        self.images = []
        self.anchors = set()
        self.headings = []
        self.text = []
        self.current = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.anchors.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img" and attrs.get("src"):
            self.images.append((attrs["src"], attrs.get("alt", "")))
        if tag in ("h1", "h2", "h3"):
            self.current = []

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3") and self.current is not None:
            self.headings.append("".join(self.current).replace("¶", "").strip())
            self.current = None

    def handle_data(self, data):
        self.text.append(data)
        if self.current is not None:
            self.current.append(data)


@lru_cache(maxsize=None)
def rendered(path):
    return Page(path.read_text())


for page, expected_ids in COVERAGE.items():
    localized_headings = set()
    for language in LANGUAGES:
        source = ROOT / f"docs/sections/{page}.{language}.md"
        text = source.read_text()
        markers = re.findall(r"<!-- guide-coverage: (.*?) -->", text)
        assert len(markers) == 1, (source, "coverage marker")
        assert set(markers[0].split()) == expected_ids, (source, "coverage IDs")
        after_marker = text.split("<!-- guide-coverage:", 1)[1].split("-->", 1)[1]
        heading = re.sub(r" \{#[^}]+\}$", "", re.search(r"^#{2,3} (.+)$", after_marker, re.M).group(1))
        assert heading not in localized_headings or language == "pt-PT", (source, "untranslated heading")
        localized_headings.add(heading)
        assert text.count("\n" + re.search(r"^#{2,3} .+$", after_marker, re.M).group(0) + "\n") == 1, (source, "duplicate section")

        prefix = "" if language == "en" else language + "/"
        output = SITE / prefix / "sections" / page / "index.html"
        assert output.is_file(), (source, "run mkdocs build first")
        html = rendered(output)
        assert heading in html.headings, (output, "new content not rendered")
        if page == "combat":
            assert text.count("{#player-screen-options}") == 1, source
            assert "player-screen-options" in html.anchors, output
            assert PLAYER_SCREEN_LABELS[language][0] in html.headings, output
            prose = " ".join(html.text)
            for label in PLAYER_SCREEN_LABELS[language]:
                assert label in text and label in prose, (output, label, "screen options not rendered")
        if page == "settings":
            assert "(combat.md#player-screen-options)" in text, source
        url = urljoin(BASE_URL, prefix + "sections/" + page + "/")
        for link in html.links:
            target = urlsplit(urljoin(url, link))
            if target.netloc != urlsplit(BASE_URL).netloc or not target.path.startswith(BASE_PATH):
                continue
            local = SITE / unquote(target.path[len(BASE_PATH):])
            if local.is_dir():
                local /= "index.html"
            assert local.is_file(), (output, link, "missing local target")
            if target.fragment and local.suffix == ".html":
                assert unquote(target.fragment) in rendered(local).anchors, (output, link, "missing anchor")

        if page == "characters":
            assert "(1d6+3)/2" in text and "(1d6+3)/2" in output.read_text(), source
        if page == "places":
            assert "MOD-087" in text and "MOD-087" in output.read_text(), source

print(f"PASS: {len(COVERAGE) * len(LANGUAGES)} localized Master pages, coverage markers, localized rendered sections, formulas and all internal links/anchors. Runtime behavior is not tested by this check.")

V2_ANCHORS = {
    "homepage": {"resume-adventure", "adventure-heroes", "first-adventure", "quick-access"},
    "adventure": {"character-health-attendance"},
    "combat": {"combat-participant-editor"},
    "places": {"local-creature-status"},
    "live-session": {"live-session-bottom-bar"},
    "topbar": {"live-session-control", "fill-main-window"},
}
V2_SCREENSHOTS = {
    "homepage": {"command-desk-2-0.jpg", "first-adventure-2-0.jpg"},
    "live-session": {"live-session-bottom-bar-2-0.jpg"},
}
for language in LANGUAGES:
    prefix = "" if language == "en" else language + "/"
    index = rendered(SITE / prefix / "index.html")
    assert "guide-2-0" in index.anchors, language
    for section in ("homepage", "live-session", "combat", "places", "hero-sync"):
        assert any(urlsplit(link).path.rstrip("/").endswith(f"sections/{section}") for link in index.links), (language, section)
    for section, anchors in V2_ANCHORS.items():
        output = SITE / prefix / "sections" / section / "index.html"
        html = rendered(output)
        assert anchors <= html.anchors, (language, section, anchors - html.anchors)
        expected_screenshots = {f"dashboard-{language}.jpg"} if section == "adventure" else V2_SCREENSHOTS.get(section, ())
        for expected in expected_screenshots:
            sources = [(src, alt) for src, alt in html.images if src.endswith("/" + expected)]
            assert len(sources) == 1 and sources[0][1].strip(), (language, section, expected)
            src, _ = sources[0]
            url = urlsplit(urljoin(BASE_URL + prefix + "sections/" + section + "/", src))
            assert url.path.startswith(BASE_PATH)
            assert (SITE / unquote(url.path[len(BASE_PATH):])).is_file(), (language, section, src)
        assert not any(src.endswith(("/en_home.png", "/en_sessionelive_attiva_topbar.png", "/en_dashboardavventura.png")) for src, _ in html.images), output

print("PASS: DnDino 2.0.0 overview links, guide anchors and screenshots in all seven languages.")
