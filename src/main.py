# main.py
import os
import sys
import json
from pdf_processor import PDFOutlineExtractor

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory {INPUT_DIR} not found!", file=sys.stderr)
        sys.exit(1)

    print(f"[DEBUG] Looking for PDFs in: {INPUT_DIR}")
    files = os.listdir(INPUT_DIR)
    print(f"[DEBUG] Found files: {files}")

    extractor = PDFOutlineExtractor()

    for filename in files:
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}.json")

            print(f"[DEBUG] Processing: {input_path}")
            result = extractor.extract_structure(input_path)

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"✅ Processed {filename} → {output_path}")
        else:
            print(f"[DEBUG] Skipping non-PDF: {filename}")

if __name__ == "__main__":
    main()
