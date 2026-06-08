# omf-ai-contributors

A small utility repository used to extract text from DOCX files and produce simple score reports (Markdown) for OMF sessions and champion syncs.

## Project structure

- `docx2txt.py` — main extraction script
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

## Notes

- This repository intentionally ignores large input/output directories; keep raw data out of git.

## License

MIT (add LICENSE file if desired)
