# Adobe India Hackathon 2025 - Challenge 1A: PDF Heading Extraction

## 🧠 Overview

This repository presents a complete solution for **Challenge 1A** of the Adobe India Hackathon 2025. The goal of this challenge is to process PDF files and extract structured heading outlines in a specific JSON format. The solution uses **machine learning (LayoutLMv3)** combined with **OCR (Tesseract)** and has been designed for robustness, performance, and Docker-based execution without internet access.

---

## 📂 Project Structure

```
Connecting-The-Dots-Round-1A/
├── round1a/
│   ├── input/                       # PDF files will be mounted here during runtime
│   ├── output/                     # JSON outputs will be saved here
│   ├── ml_model/
│   │   └── layoutlm_pipeline.py    # LayoutLMv3-based heading extractor
│   ├── processor/
│   │   └── extract.py              # Main pipeline for processing PDFs
│   └── run.py                      # Entry point for Docker execution
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧪 Technologies Used

| Tool                       | Purpose                                           |
| -------------------------- | ------------------------------------------------- |
| Python 3.10                | Primary programming language                      |
| Docker                     | Containerized execution                           |
| Tesseract OCR              | Text and layout extraction from scanned PDF pages |
| LayoutLMv3                 | ML model for layout-aware heading detection       |
| Transformers (HuggingFace) | Model loading and tokenization                    |
| PyMuPDF / pdf2image        | PDF to image conversion for processing            |
| PIL (Pillow)               | Image operations                                  |

---

## 📥 Installation (For Development)

```bash
# Clone the repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Dockerized Execution (As Adobe Will Do)

### 1. Build Docker Image

```bash
docker build --platform linux/amd64 -t pdf-processor .
```

### 2. Prepare Input and Output Folders

```bash
# Create the folder structure on your local machine
mkdir -p test_mount/input
mkdir -p test_mount/output/my_repo_id

# Copy test PDF(s) into input folder
cp sample.pdf test_mount/input/
```

### 3. Run the Container (PowerShell-compatible example):

```powershell
docker run --rm `
  -v "C:\Users\ajays\adobe-test\test_mount\input:/app/input:ro" `
  -v "C:\Users\ajays\adobe-test\test_mount\output\my_repo_id:/app/output" `
  --network none pdf-processor
```

This mimics the exact evaluation setup:

* `/app/input` is **read-only**
* Output will be written to `/app/output`
* No internet access (`--network none`)

---

## 📄 Output Format

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

## ⚙️ Components & Their Roles

* **run.py**: Orchestrates folder-wise processing, one PDF at a time.
* **extract.py**: Handles OCR, image conversion, heading merging, and JSON export.
* **layoutlm\_pipeline.py**: Loads the pre-trained LayoutLMv3 model and infers heading candidates using text, bounding boxes, and layout context.

---

## 📦 Libraries and Their Purpose

| Library                   | Purpose                      |
| ------------------------- | ---------------------------- |
| `transformers`            | LayoutLMv3 model & tokenizer |
| `torch`                   | Model inference              |
| `pytesseract`             | OCR word extraction          |
| `pdf2image` / `PyMuPDF`   | Convert PDF pages to images  |
| `Pillow` (PIL)            | Handle image formats         |
| `json` / `os` / `pathlib` | File I/O and path handling   |

---

## ✅ Validation Checklist

* [x] PDF files read from `/app/input`
* [x] JSON written to `/app/output` per PDF
* [x] Headings are complete and grouped (not single words)
* [x] Works fully offline, CPU-only
* [x] No internet access required
* [x] Works within 10 seconds for 50 pages (PDFs tested)
* [x] Model size under 200MB

---

## 🧪 Local Testing with Dummy Data (Optional)

```bash
# Run Python directly if you want to debug
python round1a/run.py
```

Ensure your local folders mimic the Docker ones for consistency.

---

## 📝 Notes

* The model and logic are tuned for document-style PDFs with distinguishable headings.
* For scanned or low-quality PDFs, performance may vary depending on OCR accuracy.
* The heading merging logic groups adjacent words that visually form a heading block.

---

## 📬 Contact

For any questions, raise an issue on the repository or email `yourname@example.com`.

---

## 📌 License

This project is open-source and complies with the [Adobe Hackathon 2025](https://www.adobe.com/) guidelines. Libraries used are under MIT/Apache-compatible licenses.
