#!/usr/bin/env python3
import sys
from pathlib import Path
from docx import Document
import argparse


def convert(docx_path: Path, output_dir: Path) -> None:
    src = Path(docx_path).resolve()
    if not src.exists():
        print(f"Error: file not found: {src}")
        return
    if src.suffix.lower() != ".docx":
        print(f"Skipping non-.docx file: {src}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    doc = Document(src)
    paragraphs = [p.text for p in doc.paragraphs]
    text = "\n".join(paragraphs)

    out = output_dir / (src.stem + ".txt")
    out.write_text(text, encoding="utf-8")
    print(f"Saved: {out}")


def main():
    parser = argparse.ArgumentParser(description="Convert .docx files to .txt")
    parser.add_argument("input", help="Path to a .docx file or directory containing .docx files")
    parser.add_argument("-o", "--output", help="Output directory for .txt files. Defaults to ./docx2txt_output",
                        default=None)
    args = parser.parse_args()

    input_path = Path(args.input)
    if args.output:
        output_base = Path(args.output)
    else:
        output_base = Path(__file__).parent / "docx2txt_output"

    if not input_path.exists():
        sys.exit(f"Error: input path not found: {input_path}")

    if input_path.is_file():
        convert(input_path, output_base)
    elif input_path.is_dir():
        # iterate non-recursively over .docx files in directory
        docx_files = [p for p in input_path.iterdir() if p.is_file() and p.suffix.lower() == ".docx"]
        if not docx_files:
            print(f"No .docx files found in directory: {input_path}")
            return
        for f in sorted(docx_files):
            convert(f, output_base)
    else:
        sys.exit(f"Error: unsupported input path: {input_path}")


if __name__ == "__main__":
    main()
