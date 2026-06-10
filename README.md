# omf-ai-contributors

A small utility repository used to extract text from DOCX files and produce simple score reports (Markdown) for OMF sessions and champion syncs.

## Project structure

- `docx2txt.py` — DOCX-to-text extraction script
- `merge_reports.py` — merges per-session Markdown score reports into one combined report
- `confluence_scores.py` — fetches Confluence pages and aggregates participant scores into a summary table
- `.env.example` — credentials template for `confluence_scores.py` (copy to `.env` and fill in)
- `input/` — source DOCX and TXT files (not committed)
- `docx2txt_output/`, `output/` — generated outputs (ignored)
- `_prompts/` — prompt templates

## Requirements

- Python 3.8+
- Recommended: create a virtual environment

## Usage

1. Place source `.docx` files under `input/docx/` (or any folder you prefer).

2. Run the extractor. The script now accepts either a single `.docx` file or a directory containing `.docx` files, plus an optional output directory:

```bash
# Convert a single file (writes to default output folder next to the script)
python docx2txt.py input/docx/example.docx

# Convert all .docx files in a folder (non-recursive)
python docx2txt.py input/docx/champions-syncs

# Convert and specify an output folder
python docx2txt.py input/docx/champions-syncs -o output/txt/champions-syncs
```

Notes about behavior:

- If `input` is a file, only that file is converted.
- If `input` is a directory, the script iterates non-recursively over all `*.docx` files in that directory and converts them.
- Use `-o/--output` to set the destination folder for generated `.txt` files; if omitted, the default is `docx2txt_output/` located next to the script.
- The script creates the output directory if it does not exist, skips non-`.docx` files, and reports missing files without aborting the whole run.

Dependency: the script uses the `python-docx` package. Install with:

```bash
pip install python-docx
```

## Merging score reports — `merge_reports.py`

Combines all per-session Markdown score reports in a folder into a single consolidated report. The output file is named after the input folder and written to `output-report/` by default.

```bash
# Merge all .md reports in a folder (output -> output-report/<folder-name>.md)
python merge_reports.py output/champions-syncs

# Specify a custom output directory
python merge_reports.py output/champions-syncs --output-dir path/to/output

# Short forms for the output directory flag
python merge_reports.py output/champions-syncs --o path/to/output
python merge_reports.py output/champions-syncs -o path/to/output
```

Notes about behavior:

- Input must be a directory; all `*.md` files inside are processed in alphabetical (date) order.
- Each file must follow the standard score report template: a `**Session Date:**` header and a `| Name | Date | Activity | Score |` table.
- The merged report's **Period** line is set automatically from the first and last session dates found.
- Files with no parseable table rows are skipped with a warning; the run continues.
- The output directory is created if it does not exist.
- Running without arguments defaults to `output/champions-syncs/` as input.

No additional dependencies — stdlib only.

## Summarising scores from Confluence — `confluence_scores.py`

Fetches Confluence pages that contain score tables (`| Name | Date | Activity | Score |`) and produces a single summary Markdown table aggregated by participant, sorted by total score descending.

### Setup

1. Copy `.env.example` to `.env` and fill in your credentials (the file is gitignored):

```
CONFLUENCE_URL=https://onemainfinancial.atlassian.net
CONFLUENCE_EMAIL=you@example.com
CONFLUENCE_TOKEN=your-api-token
```

Generate an API token at: https://id.atlassian.com/manage-profile/security/api-tokens

2. Install dependencies:

```bash
pip install requests beautifulsoup4 python-dotenv
```

### Usage

```bash
# Use the default pages defined in PAGE_IDS inside the script
python confluence_scores.py

# Save output to a file
python confluence_scores.py -o output-report/scores-summary.md

# Single page – full URL
python confluence_scores.py -p https://onemainfinancial.atlassian.net/wiki/spaces/PE/pages/1433669146/Engineering+-+Phase+2

# Single page – bare numeric ID
python confluence_scores.py -p 1433669146

# Multiple pages (URLs, IDs, or a mix)
python confluence_scores.py -p 1433669146 1672708119 1672708235
python confluence_scores.py -p https://.../pages/1433669146/... 1672708119

# Save output while specifying pages
python confluence_scores.py -p 1433669146 1672708119 -o output-report/scores-summary.md
```

When `-p` / `--pages` is omitted, the script falls back to the `PAGE_IDS` list defined at the top of the file.

### Output format

```markdown
| Name             | Total Score |
| ---              | ---         |
| Sukalya Rajendran | 35         |
| Jason Daggs       | 28         |
| ...               | ...        |
```

### Optional: atlassian-python-api wrapper

```bash
pip install atlassian-python-api
python confluence_scores.py --use-atlassian-api
```

Uses the same Confluence REST API under the hood; useful if you already have `atlassian-python-api` in your environment.

## Notes

- This repository intentionally ignores large input/output directories; keep raw data out of git.

## License

MIT (add LICENSE file if desired)
