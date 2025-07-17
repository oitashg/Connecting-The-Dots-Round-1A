import PyPDF2
from collections import Counter
from processor.utils import is_title_candidate, is_noise_final, is_final_heading, determine_levels


def extract_pdf_outline(pdf_path):
    """Extract outline from a single PDF file."""
    all_lines = []

    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                if text:
                    for line in text.split('\n'):
                        line = line.strip()
                        if line:
                            all_lines.append({'text': line, 'page': page_num + 1})
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

    headings = filter_final_headings(all_lines)
    title = extract_document_title(all_lines)

    return {
        "title": title,
        "outline": [
            {"level": h["level"], "text": h["text"], "page": h["page"]}
            for h in headings
        ]
    }


def extract_document_title(all_lines):
    for line_data in all_lines[:10]:
        line = line_data['text']
        if len(line) >= 5 and is_title_candidate(line):
            return line
    return "Document"


def filter_final_headings(all_lines):
    counts = Counter(line['text'] for line in all_lines)
    repeated = {text for text, cnt in counts.items() if cnt > 2}
    final_headings = []

    for line_data in all_lines:
        line = line_data['text']
        if line in repeated or is_noise_final(line):
            continue
        if is_final_heading(line):
            final_headings.append(line_data)

    return determine_levels(final_headings)
