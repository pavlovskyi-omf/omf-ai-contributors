#!/usr/bin/env python3
import sys
import os
from pathlib import Path
from docx import Document


def convert(docx_path: str) -> None:
    src = Path(docx_path).resolve()
    if not src.exists():
        sys.exit(f"Error: file not found: {src}")
    if src.suffix.lower() != ".docx":
        sys.exit(f"Error: expected a .docx file, got: {src.suffix}")

    # output_dir = Path(__file__).parent / "docx2txt_output"
    output_dir = Path(__file__).parent / "input/txt/champions-syncs"
    output_dir.mkdir(exist_ok=True)

    doc = Document(src)
    paragraphs = [p.text for p in doc.paragraphs]
    text = "\n".join(paragraphs)

    out = output_dir / (src.stem + ".txt")
    out.write_text(text, encoding="utf-8")
    print(f"Saved: {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python docx2txt.py <file.docx>")
    convert(sys.argv[1])
