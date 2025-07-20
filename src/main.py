import os
import sys
import json
from pdf_processor import PDFOutlineExtractor

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    # Create output directory if missing
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Verify input directory exists
    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory {INPUT_DIR} not found!", file=sys.stderr)
        print("Hint: Did you mount the volume with -v /host/path:/app/input?", file=sys.stderr)
        sys.exit(1)

    extractor = PDFOutlineExtractor()
    
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}.json")
            
            result = extractor.extract_structure(input_path)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"Processed {filename} → {output_path}")

if __name__ == "__main__":
    main()