# round1a/run.py

import os
import json
from processor.extract import extract_pdf_outline

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def main():
    if not os.path.exists(INPUT_DIR):
        print(f"[ERROR] Input folder '{INPUT_DIR}' not found.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("[INFO] No PDF files found in input folder.")
        return

    print(f"[INFO] Found {len(pdf_files)} PDF file(s) to process.\n")

    for filename in pdf_files:
        pdf_path = os.path.join(INPUT_DIR, filename)
        result = extract_pdf_outline(pdf_path)

        if result:
            json_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, json_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"✓ {filename} → {json_filename}")
            print(f"  Title: {result['title']}")
            print(f"  Headings: {len(result['outline'])}\n")
        else:
            print(f"✗ Failed to process {filename}\n")

if __name__ == "__main__":
    main()
