#!/usr/bin/env python3
"""
Build the inline SVG icon sprite from Font Awesome Free 5.15.1.

    python3 tools/build-icon-sprite.py

Writes _includes/icon-sprite.html, which base.html injects once per page.

Why inline rather than an external sprite file: Safari does not support
cross-file `<use href="sprite.svg#id">` references, so an external sprite would
silently render nothing there. Inlining costs a few KB per page and replaces a
~70KB render-blocking third-party stylesheet.

Icons are CC BY 4.0 (https://fontawesome.com/license/free). Attribution is
emitted into the generated file.
"""

import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_includes" / "icon-sprite.html"

VERSION = "5.15.1"
BASE = f"https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@{VERSION}/svgs"

# name -> style. Keep in sync with the `icon:` values used in page front matter
# and with the hardcoded icons in nav.html.
ICONS = {
    "calendar-alt": "solid",
    "cloud": "solid",
    "cloud-upload-alt": "solid",
    "code": "solid",
    "cogs": "solid",
    "envelope": "solid",
    "globe": "solid",
    "github": "brands",
    "linkedin": "brands",
}


def fetch(name, style):
    url = f"{BASE}/{style}/{name}.svg"
    with urllib.request.urlopen(url, timeout=20) as r:
        svg = r.read().decode()

    viewbox = re.search(r'viewBox="([^"]+)"', svg)
    path = re.search(r'<path[^>]*\sd="([^"]+)"', svg)
    if not viewbox or not path:
        sys.exit(f"could not parse {url}")
    return viewbox.group(1), path.group(1)


def main():
    symbols = []
    for name, style in ICONS.items():
        viewbox, d = fetch(name, style)
        # Symbol ids match the `fa-*` values already used in front matter, so no
        # page content had to change when moving off the icon font.
        symbols.append(
            f'  <symbol id="fa-{name}" viewBox="{viewbox}"><path d="{d}"/></symbol>'
        )
        print(f"  fa-{name} ({style})")

    body = "\n".join(symbols)
    OUT.write_text(
        "{% comment %}\n"
        "  GENERATED FILE - do not edit by hand.\n"
        "  Rebuild with: python3 tools/build-icon-sprite.py\n\n"
        f"  Font Awesome Free {VERSION} icons, CC BY 4.0\n"
        "  https://fontawesome.com/license/free\n"
        "{% endcomment %}\n"
        '<svg xmlns="http://www.w3.org/2000/svg" class="icon-sprite" aria-hidden="true" focusable="false">\n'
        f"{body}\n"
        "</svg>\n",
        encoding="utf-8",
    )
    print(f"\nwrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
