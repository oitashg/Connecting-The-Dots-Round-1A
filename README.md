# Adobe India Hackathon 2025 - Challenge 1A: PDF Heading Extraction

##  Overview

This repository presents a complete solution for **Challenge 1A** of the Adobe India Hackathon 2025. The goal of this challenge is to process PDF files and extract structured heading outlines in a specific JSON format. The solution uses **machine learning (LayoutLMv3)** combined with **OCR (Tesseract)** and has been designed for robustness, performance, and Docker-based execution without internet access.

---

##  Project Structure

```
Connecting-The-Dots-Round-1A/
├── input/                   # (Bind mounted) Directory containing input PDF files (read-only)
├── output/                  # (Bind mounted) Directory where JSON output will be saved
├── src/
│   ├── main.py              # Entry point for execution
│   ├── pdf_processor.py     # Contains logic for heading extraction from PDFs
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container configuration for the solution
├── .dockerignore            # Files/folders to ignore in Docker context
├── README.md                # This documentation

```

---

##  Technologies Used

| Library                       | Purpose                                        |
| ----------------------------- | ---------------------------------------------- |
| PyMuPDF                       | Extracts text and layout information from PDFs |
| re                            | Regex-based heading detection                  |
| unicodedata                   | Unicode normalization                          |
| json, os, sys, typing         | Standard Python modules                        |


---

##  Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

```

---

## 🚀 Dockerized Execution (As per instruction given)

### 1. Build Docker Image

```bash
docker build --platform linux/amd64 -t <reponame.someidentifier> .
```

### 2. Prepare Input and Output Folders (for testing purpose)

```bash
# Create the folder structure on your local machine
mkdir -p test_mount/input
mkdir -p test_mount/output/my_repo_id

# Copy test PDF(s) into input folder
cp sample.pdf test_mount/input/
```

### 3. Run the Container (PowerShell-compatible example):

```bash
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output/repoidentifier/:/app/output --network none <reponame.someidentifier>
```

This mimics the exact evaluation setup:

* `/app/input` is **read-only**
* Output will be written to `/app/output`
* No internet access (`--network none`)

---

##  Output Format

Each processed PDF generates a `.json` file matching the format:

```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "1. Introduction",
      "page": 2
    },
    {
      "level": "H2",
      "text": "1.1 Objective",
      "page": 3
    }
  ]
}
```

The headings are extracted, grouped (not single words), and detected based on font size, visual layout, and optionally confidence.

---

##  Components & Their Roles

* **run.py**: Orchestrates folder-wise processing, one PDF at a time.
* **extract.py**: Handles OCR, image conversion, heading merging, and JSON export.
* **layoutlm\_pipeline.py**: Loads the pre-trained LayoutLMv3 model and infers heading candidates using text, bounding boxes, and layout context.

---


---

## ✅ Validation Checklist

* [x] PDF files read from `/app/input`
* [x] JSON written to `/app/output` per PDF
* [x] Headings are complete and grouped (not single words)
* [x] Works fully offline, CPU-only
* [x] Multilingual Support
* [x] Works within 10 seconds for 50 pages (PDFs tested)
* [x] Model size under 200MB

---



---

## 📝 Notes

* The model and logic are tuned for document-style PDFs with distinguishable headings.
* For scanned or low-quality PDFs, performance may vary depending on OCR accuracy.
* The heading merging logic groups adjacent words that visually form a heading block.

---


