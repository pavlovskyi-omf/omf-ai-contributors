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

1. Place source `.docx` files under `input/docx/`
2. Run the extractor:

```bash
python docx2txt.py
```

Outputs will be written to `docx2txt_output/` and `output/` as Markdown score files.

## Notes

- This repository intentionally ignores large input/output directories; keep raw data out of git.

## License

MIT (add LICENSE file if desired)
