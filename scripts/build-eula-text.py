#!/usr/bin/env python3
"""Render terms.md as the plain-text EULA to paste into App Store Connect.

App Store Connect's custom licence agreement is a plain-text field: it strips
and escapes HTML and keeps only line breaks, so the Markdown source cannot be
pasted as-is without users reading literal `**bold**` and `[text](./file.md)`.
This script is the single step between the two, so `terms.md` stays the source
of truth and the pasted text can always be regenerated rather than hand-edited.

    python3 scripts/build-eula-text.py           # rewrite terms-appstore.txt
    python3 scripts/build-eula-text.py --check   # fail if it is out of date

Run it after any change to terms.md, then re-paste the result into
App Store Connect (Apps > Budgie > General > App Information > License
Agreement). Editing terms-appstore.txt by hand will be overwritten.
"""

import argparse
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "terms.md"
OUTPUT = ROOT / "terms-appstore.txt"

# Relative links in the Markdown resolve against the published site; the pasted
# text has no page to be relative to, so they have to become absolute.
SITE = "https://etienneptl2.github.io/budgie-support/"

# The emoji carry meaning in the rendered page (they label the contact details)
# and become noise once stripped, so they are spelled out instead.
EMOJI_LABELS = {"\U0001F4E7": "Email: ", "\U0001F4EE": "Address: "}

# Typographic characters that survive the paste but render inconsistently in a
# monospaced plain-text field. Em dashes are left alone -- they read fine.
PUNCTUATION = {
    "‑": "-",  # non-breaking hyphen, used throughout terms.md
    "’": "'",
    "‘": "'",
    "“": '"',
    "”": '"',
}


def resolve_link(url: str) -> str:
    """Turn a repo-relative Markdown link into a URL on the published site."""
    if url.startswith("./") and url.endswith(".md"):
        return SITE + url[2:-3] + ".html"
    return url


def render(markdown: str) -> str:
    text = markdown

    # Jekyll front matter is site plumbing, not part of the agreement.
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.DOTALL)

    # [label](url) -> label (url), dropping the parenthetical when the label
    # already is the URL.
    def link(match: re.Match) -> str:
        label, url = match.group(1), resolve_link(match.group(2))
        return label if label == url else f"{label} ({url})"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)

    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"\1", text)

    for emoji, label in EMOJI_LABELS.items():
        text = text.replace(emoji + " ", label)
    # Anything else pictographic would paste as a stray glyph.
    text = "".join(c for c in text if unicodedata.category(c) != "So")

    for source, replacement in PUNCTUATION.items():
        text = text.replace(source, replacement)

    lines = []
    for line in text.split("\n"):
        line = line.rstrip()
        if re.fullmatch(r"-{3,}", line):  # horizontal rule
            continue
        heading = re.match(r"(#{1,6})\s+(.*)", line)
        if heading:
            line = heading.group(2).upper()
        lines.append(line)

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if the committed text is stale instead of rewriting it",
    )
    args = parser.parse_args()

    rendered = render(SOURCE.read_text(encoding="utf-8"))

    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else None
        if current != rendered:
            print(
                f"{OUTPUT.name} is out of date with {SOURCE.name}. "
                f"Run: python3 scripts/{pathlib.Path(__file__).name}",
                file=sys.stderr,
            )
            return 1
        print(f"{OUTPUT.name} is up to date.")
        return 0

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"Wrote {OUTPUT.name} ({len(rendered.splitlines())} lines).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
