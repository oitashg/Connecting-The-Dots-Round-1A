# Adobe India Hackathon 2025 
# Round 1A: PDF Heading Extraction

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

## ❗❗Execution

1. Clone the repository using **Clone Command** in the parent folder. You’ll get a new folder named after the repository.

2. Now, move into the child folder with the help of **Move Command**

3. Build the Docker image by running the provided **Build Command** in that folder (it uses the Dockerfile in the project root).

4. To run the container, we must change the directory to the parent folder with help of **Change Command**

4. Run the container with the supplied **Run Command**, which mounts your local input folder into the container and mounts the output/repoidentifier folder into container to get the output folder locally in host machine.

### Clone Command
```bash
git clone https://github.com/oitashg/Connecting-The-Dots-Round-1A.git
```

### Move Command
```bash
cd Connecting-The-Dots-Round-1A/
```

### Build Command
```bash
docker build --platform linux/amd64 -t <reponame.someidentifier> .
```

### Change Command
```bash
cd ..
```

### Run Command
```bash
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output/repoidentifier/:/app/output --network none <reponame.someidentifier>
```

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



## 🌐 Multilingual Support

This solution provides basic multilingual support through:

- **Unicode normalization using Python’s `unicodedata` module**  
  Ensures consistent character handling across scripts (e.g., Latin, Devanagari, Cyrillic, etc.)

- **Language-agnostic text extraction using PyMuPDF**  
  PyMuPDF can extract text from PDFs in a wide range of languages and character sets, including:

  - **English**
  - **Hindi**
  - **Chinese**
  - **Arabic**
  - **Tamil**
  - **And many more...**

---

##  Components & Their Roles

* **main.py**: Orchestrates folder-wise processing, one PDF at a time.
* **pdf_processor.py**: Handles OCR, image conversion, heading merging, and JSON export.

---

## Constraints  
 
* Execution time - ≤ 10 seconds for a 50-page PDF  
* Network  No internet access allowed 
* Model size  ≤ 200MB (if used)   
* Runtime  Must run on CPU (amd64), your solution should run on the system with 8 CPUs and 16 GB RAM * configurations   

---

##  Notes

* The model and logic are tuned for document-style PDFs with distinguishable headings.
* For scanned or low-quality PDFs, performance may vary depending on OCR accuracy.
* The heading merging logic groups adjacent words that visually form a heading block.

---

## ⚠️ Disclaimer
During development, we experimented with a machine learning–based heading extraction approach using state-of-the-art models like LayoutLMv3, which provided significantly more accurate and context-aware results for complex PDFs.

However, due to the strict constraints imposed by the challenge — particularly:

🚫 Execution time (≤ 10 seconds for 50-page PDFs)
🚫 Model size limit (≤ 200MB)
🚫 No internet access or GPU usage
🚫 CPU-only inference on AMD64 architecture

we opted for a lightweight, rule-based alternative using PyMuPDF + regex heuristics, which meets all the challenge requirements.
