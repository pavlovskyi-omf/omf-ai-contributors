#!/usr/bin/env python3
"""
Fetch Confluence pages that contain score tables and produce a summarised
Markdown table:  | Name | Total Score |  sorted by score descending.

Usage
-----
    1. Copy .env.example → .env and fill in your credentials.
    2. Run:

    # Use default pages defined in PAGE_IDS
    python confluence_scores.py -o output-report/scores-summary.md

    # Single page – full URL or bare page ID
    python confluence_scores.py -p https://…atlassian.net/wiki/spaces/PE/pages/1433669146/…
    python confluence_scores.py -p 1433669146

    # Multiple pages
    python confluence_scores.py -p 1433669146 1672708119 1672708235

    # Mix of URLs and IDs
    python confluence_scores.py -p https://…/pages/1433669146/… 1672708119

    # Optional atlassian-python-api wrapper
    python confluence_scores.py --use-atlassian-api

API token: https://id.atlassian.com/manage-profile/security/api-tokens

Dependencies
------------
    pip install requests beautifulsoup4 python-dotenv   # always required
    pip install atlassian-python-api                    # only for --use-atlassian-api

---------------------------------------------------------------------------
CONNECTION OPTIONS  (see fetch_page_html() and fetch_page_atlassian() below)
---------------------------------------------------------------------------

  Option 1 – requests + Basic Auth  [default]
      Uses the Confluence Cloud REST API directly.
      Auth: email address + API token (generated from Atlassian account).
      No extra library needed beyond `requests`.

  Option 2 – atlassian-python-api  [--use-atlassian-api flag]
      A thin wrapper around the same REST API.  Provides a slightly more
      Pythonic surface and handles pagination automatically for list calls.
      Auth: same email + API token.  Install: pip install atlassian-python-api

  Option 3 – OAuth 2.0 (not implemented here)
      Required when building a multi-tenant app or when a service account
      is unavailable.  Needs an OAuth app registered at
      https://developer.atlassian.com/console/myapps/
      and is significantly more involved than a personal API token.
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import requests
    from requests.auth import HTTPBasicAuth
except ImportError:
    sys.exit("Missing dependency: pip install requests")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Missing dependency: pip install beautifulsoup4")

try:
    from dotenv import load_dotenv
except ImportError:
    sys.exit("Missing dependency: pip install python-dotenv")


# ---------------------------------------------------------------------------
# Configuration – loaded from .env (falls back to environment variables)
# ---------------------------------------------------------------------------

# Look for .env next to this script, then in the current working directory
_here = Path(__file__).parent
load_dotenv(_here / ".env")
load_dotenv()   # fallback: cwd

CONFLUENCE_URL   = os.environ.get("CONFLUENCE_URL",   "https://onemainfinancial.atlassian.net")
CONFLUENCE_EMAIL = os.environ.get("CONFLUENCE_EMAIL", "")
CONFLUENCE_TOKEN = os.environ.get("CONFLUENCE_TOKEN", "")

# Pages that contain score tables – add/remove as needed
PAGE_IDS = [
    "1433669146",   # Engineering - Phase 2
    "1672708119",   # Cross-Functional Lighthouse PDLC Sessions - Phase 2
    "1672708235",   # Cross-Functional Lighthouse AI Open Hours - Phase 2
]


# ---------------------------------------------------------------------------
# Page ID resolution
# ---------------------------------------------------------------------------

_PAGE_ID_FROM_URL = re.compile(r"/pages/(\d+)")


def resolve_page_id(source: str) -> str:
    """Accept a full Confluence URL or a bare numeric page ID."""
    m = _PAGE_ID_FROM_URL.search(source)
    if m:
        return m.group(1)
    if re.fullmatch(r"\d+", source.strip()):
        return source.strip()
    sys.exit(f"Cannot extract a page ID from: {source!r}\n"
             "Expected a full Confluence URL (.../pages/<id>/...) or a bare numeric ID.")


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(CONFLUENCE_EMAIL, CONFLUENCE_TOKEN)


def fetch_page_html(page_id: str) -> str:
    """
    Option 1: plain requests + HTTP Basic Auth.

    Requests body.view (fully rendered HTML) so that @mentions and date macros
    are resolved to their display text before we parse the tables.
    """
    url = f"{CONFLUENCE_URL}/wiki/rest/api/content/{page_id}"
    r = requests.get(url, params={"expand": "body.view"}, auth=_auth(), timeout=30)
    r.raise_for_status()
    return r.json()["body"]["view"]["value"]


def fetch_page_atlassian(page_id: str) -> str:
    """
    Option 2: atlassian-python-api wrapper.

    Install with:  pip install atlassian-python-api
    """
    try:
        from atlassian import Confluence  # type: ignore
    except ImportError:
        sys.exit("Missing dependency: pip install atlassian-python-api")

    conf = Confluence(url=CONFLUENCE_URL, username=CONFLUENCE_EMAIL, password=CONFLUENCE_TOKEN)
    page  = conf.get_page_by_id(page_id, expand="body.view")
    return page["body"]["view"]["value"]


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

_WS = re.compile(r"\s+")


def _clean_name(text: str) -> str:
    """Strip HTML tags, leading @, and normalise whitespace."""
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lstrip("@").strip()
    return _WS.sub(" ", text).strip()


def _parse_score(text: str) -> int:
    digits = re.sub(r"[^\d]", "", text)
    return int(digits) if digits else 0


def extract_scores(html: str) -> list[tuple[str, int]]:
    """
    Find every table whose header contains both a NAME and a SCORE column,
    then return (name, score) pairs from its data rows.
    """
    soup   = BeautifulSoup(html, "html.parser")
    result: list[tuple[str, int]] = []

    for table in soup.find_all("table"):
        header_row = table.find("tr")
        if not header_row:
            continue

        headers = [
            cell.get_text(" ", strip=True).upper()
            for cell in header_row.find_all(["th", "td"])
        ]

        if "NAME" not in headers or "SCORE" not in headers:
            continue

        name_idx  = headers.index("NAME")
        score_idx = headers.index("SCORE")

        for row in table.find_all("tr")[1:]:
            cells = row.find_all(["td", "th"])
            if len(cells) <= max(name_idx, score_idx):
                continue

            name  = _clean_name(cells[name_idx].get_text(" ", strip=True))
            score = _parse_score(cells[score_idx].get_text(strip=True))

            if name and score > 0:
                result.append((name, score))

    return result


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def build_summary_table(totals: dict[str, int]) -> str:
    ranked = sorted(totals.items(), key=lambda x: (-x[1], x[0]))
    lines  = ["| Name | Total Score |", "| --- | --- |"]
    for name, total in ranked:
        lines.append(f"| {name} | {total} |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Summarise Confluence participant scores.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "--pages", "-p", nargs="+", metavar="URL_OR_ID",
        help="One or more Confluence page URLs or numeric IDs. "
             "Defaults to the PAGE_IDS list in the script.",
    )
    ap.add_argument("--output", "-o", metavar="FILE",
                    help="Write Markdown table to this file instead of stdout")
    ap.add_argument("--use-atlassian-api", action="store_true",
                    help="Use atlassian-python-api instead of plain requests")
    args = ap.parse_args()

    if not CONFLUENCE_EMAIL or not CONFLUENCE_TOKEN:
        sys.exit(
            "Credentials not found.\n"
            "Copy .env.example → .env and fill in CONFLUENCE_EMAIL and CONFLUENCE_TOKEN.\n"
            "Generate an API token at:\n"
            "  https://id.atlassian.com/manage-profile/security/api-tokens"
        )

    page_ids = [resolve_page_id(s) for s in args.pages] if args.pages else PAGE_IDS

    fetch = fetch_page_atlassian if args.use_atlassian_api else fetch_page_html
    totals: defaultdict[str, int] = defaultdict(int)

    for page_id in page_ids:
        print(f"Fetching page {page_id} ...", file=sys.stderr)
        html  = fetch(page_id)
        pairs = extract_scores(html)
        print(f"  {len(pairs)} scored rows found", file=sys.stderr)
        for name, score in pairs:
            totals[name] += score

    print(f"\nTotal unique participants: {len(totals)}", file=sys.stderr)

    table = build_summary_table(dict(totals))

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(table + "\n")
        print(f"Saved → {args.output}", file=sys.stderr)
    else:
        print(table)


if __name__ == "__main__":
    main()
