#!/usr/bin/env python3
"""
Generate the social preview (Open Graph) images.

    python3 tools/generate-og-images.py

Writes 1200x630 PNGs into assets/img/. Re-run after changing any card text.
Requires rsvg-convert (brew install librsvg).

Inter is not installed locally, so the cards render in Helvetica Neue, which is
the nearest match to the site's webfont. If Inter is ever installed system-wide,
change FONT below and re-run.
"""

import html
import pathlib
import shutil
import tempfile
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"

FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"
NAVY = "#0f172a"
BLUE = "#2563eb"
W, H = 1200, 630


def svg(eyebrow, title_lines, chip, chip_dot=False, footer="prlic.io"):
    """Build one card. title_lines is a list so line breaks stay deliberate."""
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="1.5" fill="#ffffff" opacity="0.05"/>'
        for x in range(20, W, 28)
        for y in range(20, H, 28)
    )

    title_size = 68 if len(title_lines) > 1 else 88
    y0 = 250 if len(title_lines) > 1 else 232
    titles = "".join(
        f'<text x="80" y="{y0 + i * (title_size + 14)}" font-family="{FONT}" '
        f'font-size="{title_size}" font-weight="700" fill="#ffffff" '
        f'letter-spacing="-2">{html.escape(line)}</text>'
        for i, line in enumerate(title_lines)
    )

    # Hang the chip off the last baseline, not off the block height, or a
    # two-line title leaves a dead band between the title and the chip.
    chip_y = y0 + (len(title_lines) - 1) * (title_size + 14) + 62
    # Rough advance-width estimate; only needs to look right, not be exact.
    chip_w = int(len(chip) * 9.6) + (56 if chip_dot else 40)
    dot = f'<circle cx="102" cy="{chip_y + 22}" r="5" fill="#4ade80"/>' if chip_dot else ""
    text_x = 118 if chip_dot else 100

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="{NAVY}"/>
  <defs>
    <radialGradient id="glowA" cx="0.18" cy="0.62" r="0.6">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="{BLUE}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="0.86" cy="0.18" r="0.55">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#glowA)"/>
  <rect width="{W}" height="{H}" fill="url(#glowB)"/>
  {dots}
  <text x="80" y="150" font-family="{FONT}" font-size="22" font-weight="600"
        fill="#93c5fd" letter-spacing="3.5">{html.escape(eyebrow)}</text>
  <rect x="80" y="178" width="60" height="5" rx="2.5" fill="{BLUE}"/>
  {titles}
  <rect x="80" y="{chip_y}" width="{chip_w}" height="44" rx="22"
        fill="{BLUE}" fill-opacity="0.14" stroke="{BLUE}" stroke-opacity="0.45"/>
  {dot}
  <text x="{text_x}" y="{chip_y + 29}" font-family="{FONT}" font-size="20"
        font-weight="600" fill="#bfdbfe">{html.escape(chip)}</text>
  <text x="80" y="{H - 60}" font-family="{FONT}" font-size="22" font-weight="500"
        fill="#64748b">{html.escape(footer)}</text>
</svg>"""


CARDS = {
    "og-image.png": dict(
        eyebrow="IVAN PRLIĆ",
        title_lines=["Solutions Architect", "AI & DevOps Consultant"],
        chip="Available for projects",
        chip_dot=True,
    ),
    "og-image-hr.png": dict(
        eyebrow="IVAN PRLIĆ",
        title_lines=["Solutions Architect", "AI i DevOps konzultant"],
        chip="Dostupan za projekte",
        chip_dot=True,
    ),
    "og-advisory.png": dict(
        eyebrow="AI ADVISORY · REGULATED EU COMPANIES",
        title_lines=["AI that reaches production", "inside your perimeter"],
        chip="Fixed scope · Published prices",
    ),
    "og-advisory-hr.png": dict(
        eyebrow="AI SAVJETOVANJE ZA HRVATSKE TVRTKE",
        title_lines=["AI koji se isplati", "i koji dođe do produkcije"],
        chip="Fiksan opseg · Objavljene cijene",
    ),
}


def main():
    if not shutil.which("rsvg-convert"):
        sys.exit("rsvg-convert not found. Install it with: brew install librsvg")

    OUT.mkdir(parents=True, exist_ok=True)
    # The SVG is an intermediate, not a source of truth — this script is. Render
    # it through a temp dir so the repo only ever holds the PNGs.
    with tempfile.TemporaryDirectory() as tmp:
        for name, kwargs in CARDS.items():
            src = pathlib.Path(tmp) / name.replace(".png", ".svg")
            src.write_text(svg(**kwargs), encoding="utf-8")
            subprocess.run(
                ["rsvg-convert", "-w", str(W), "-h", str(H), str(src), "-o", str(OUT / name)],
                check=True,
            )
            print(f"  wrote {name} ({(OUT / name).stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
