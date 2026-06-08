# omf-ai-contributors

A small utility repository used to extract text from DOCX files and produce simple score reports (Markdown) for OMF sessions and champion syncs.

## Project structure

- `docx2txt.py` — DOCX-to-text extraction script
- `merge_reports.py` — merges per-session Markdown score reports into one combined report
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

## Notes

- This repository intentionally ignores large input/output directories; keep raw data out of git.

## License

MIT (add LICENSE file if desired)
