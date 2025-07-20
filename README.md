# PDF Structure Extractor - Adobe Hackathon Submission

A Dockerized solution that extracts document structure (title and headings) from PDF files, compliant with Adobe's Round 2 requirements.

## Features

- Extracts document title and hierarchical headings (H1, H2, H3)
- Processes PDFs up to 50 pages in <10 seconds
- Multilingual support (English, Japanese, Arabic, etc.)
- Strict compliance with Adobe's JSON output format
- Runs offline in a constrained environment

## Technology Stack

- Python 3.9
- PyMuPDF (fitz) - Fast PDF text extraction
- Docker - Containerization

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/adobe-pdf-extractor.git
   cd adobe-pdf-extractor
Build the Docker image:

bash
docker build --platform linux/amd64 -t pdf-extractor .
Usage
Basic Execution
bash
docker run --rm \
  -v /path/to/pdf/folder:/app/input \
  -v /path/to/output/folder:/app/output \
  --network none \
  pdf-extractor
Testing Locally
Create test folders:

bash
mkdir -p input output
cp test.pdf input/
Run the container:

bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-extractor
Output Format
The solution generates JSON files with this structure:

json
{
  "title": "Document Title",
  "outline": [
    {"level": "H1", "text": "Main Heading", "page": 1},
    {"level": "H2", "text": "Subheading", "page": 2}
  ]
}
Solution Approach
Title Extraction: First meaningful text from the first page

Heading Detection:

Pattern matching (numbered sections, chapters)

Formatting heuristics (font size, bold text)

Multilingual support through Unicode normalization

Performance Optimization:

Page-by-page processing

Early termination for long documents

Minimal text processing

Adobe Requirements Compliance
✅ AMD64 compatible Docker image
✅ No GPU dependencies
✅ No network access required
✅ ≤10 second processing for 50-page PDFs
✅ Output matches specified JSON schema

Directory Structure
text
/adobe-pdf-extractor/
├── Dockerfile
├── README.md
├── requirements.txt
└── src/
    ├── main.py             # Entry point
    └── pdf_processor.py    # Core logic
Testing
Test cases should include:

Documents with clear heading hierarchy

Mixed-language PDFs

Edge cases (short documents, scanned PDFs)