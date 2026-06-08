"""
Merge all markdown score reports in a folder into a single combined report.
Usage: python merge_reports.py <input_folder> [--output-dir <dir>]
Default output: output-report/ next to the input folder.
"""

import argparse
import os
import re
import sys
from pathlib import Path


def parse_markdown_report(filepath: Path) -> tuple[str, list[str]]:
    """Return (session_date, list_of_table_data_rows) from a score report."""
    content = filepath.read_text(encoding="utf-8")

    # Extract session date from header
    date_match = re.search(r"\*\*Session Date:\*\*\s*(.+)", content)
    session_date = date_match.group(1).strip() if date_match else filepath.stem

    # Find the table: collect lines after the header row and separator
    lines = content.splitlines()
    in_table = False
    header_seen = False
    separator_seen = False
    data_rows: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not in_table:
            # Detect table header row
            if re.match(r"\|\s*Name\s*\|", stripped, re.IGNORECASE):
                in_table = True
                header_seen = True
                continue
        else:
            if not separator_seen:
                # Skip the separator line (|---|---|...|)
                if re.match(r"\|[-|: ]+\|", stripped):
                    separator_seen = True
                    continue
            else:
                if stripped.startswith("|") and stripped.endswith("|"):
                    data_rows.append(stripped)
                else:
                    # Table ended
                    break

    return session_date, data_rows


def merge_reports(input_folder: Path, output_dir: Path) -> Path:
    md_files = sorted(input_folder.glob("*.md"))
    if not md_files:
        print(f"No markdown files found in {input_folder}")
        sys.exit(1)

    all_rows: list[str] = []
    date_range: list[str] = []

    for filepath in md_files:
        session_date, rows = parse_markdown_report(filepath)
        if rows:
            all_rows.extend(rows)
            date_range.append(session_date)
            print(f"  + {filepath.name}: {len(rows)} row(s)")
        else:
            print(f"  ! {filepath.name}: no table rows found, skipping")

    if not all_rows:
        print("No data rows collected. Aborting.")
        sys.exit(1)

    # Build merged document
    first_date = date_range[0] if date_range else "—"
    last_date = date_range[-1] if date_range else "—"
    date_label = first_date if first_date == last_date else f"{first_date} – {last_date}"

    lines = [
        "# AI Enablement: ENGINEERING Champion Sync — Combined Score Report",
        f"**Period:** {date_label}",
        "**Session Type:** AI Champions Sync",
        "",
        "---",
        "",
        "## AI Champions Sessions",
        "",
        "| Name | Date | Activity | Score |",
        "|---|---|---|---|",
        *all_rows,
    ]

    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / f"{input_folder.name}.md"
    out_file.write_text("\n".join(lines), encoding="utf-8")
    return out_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge markdown score reports.")
    parser.add_argument("input_folder", nargs="?", help="Folder containing .md reports")
    parser.add_argument("--output-dir", "--o", "-o", default=None, dest="output_dir", help="Output directory (default: output-report/ beside input)")
    args = parser.parse_args()

    if args.input_folder:
        input_folder = Path(args.input_folder)
    else:
        # Default to the champions-syncs example folder when run without args
        script_dir = Path(__file__).parent
        input_folder = script_dir / "output" / "champions-syncs"

    if not input_folder.is_dir():
        print(f"Error: {input_folder} is not a directory.")
        sys.exit(1)

    output_dir = Path(args.output_dir) if args.output_dir else input_folder.parent / "output-report"

    print(f"Input:  {input_folder}")
    print(f"Output: {output_dir}")
    print()

    out_file = merge_reports(input_folder, output_dir)
    print(f"\nSaved -> {out_file}")


if __name__ == "__main__":
    main()
