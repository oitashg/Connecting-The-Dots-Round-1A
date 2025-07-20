import fitz  # PyMuPDF
import re
import json
from typing import List, Dict, Optional
import unicodedata

class PDFOutlineExtractor:
    def __init__(self):
        self.heading_patterns = [
            (r'^(chapter|section|part)\s+\d+', 'H1'),
            (r'^\d+\.\d+', 'H2'),  # 1.1 style
            (r'^\d+\.\d+\.\d+', 'H3'),  # 1.1.1 style
            (r'^[A-Z][A-Z0-9]*$', 'H1'),  # ALL CAPS
            (r'^[IVX]+\.', 'H1'),  # Roman numerals
        ]
        
    def extract_structure(self, pdf_path: str) -> Dict:
        """Main method to extract document structure"""
        doc = fitz.open(pdf_path)
        
        # Extract title (first non-empty line on first page)
        title = self._extract_title(doc)
        
        # Extract headings with hierarchy
        outline = self._extract_headings(doc)
        
        return {
            "title": title,
            "outline": outline
        }
    
    def _extract_title(self, doc) -> str:
        """Extract document title from first page"""
        first_page = doc[0]
        text = first_page.get_text("text")
        
        # Get first non-empty line
        for line in text.split('\n'):
            stripped = line.strip()
            if stripped:
                return self._normalize_text(stripped)
        return "Untitled Document"
    
    def _extract_headings(self, doc) -> List[Dict]:
        """Extract hierarchical headings from all pages"""
        headings = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            blocks = page.get_text("dict")["blocks"]
            
            for block in blocks:
                if "lines" not in block:
                    continue
                    
                for line in block["lines"]:
                    text = "".join([span["text"] for span in line["spans"]])
                    text = self._normalize_text(text)
                    
                    if not text:
                        continue
                        
                    # Check for heading patterns
                    level = self._classify_heading(text)
                    if level:
                        headings.append({
                            "level": level,
                            "text": text,
                            "page": page_num + 1  # 1-based
                        })
        
        return headings
    
    def _classify_heading(self, text: str) -> Optional[str]:
        """Determine if text is a heading and its level"""
        # Check for common heading patterns
        for pattern, level in self.heading_patterns:
            if re.match(pattern, text, re.IGNORECASE):
                return level
        
        # Check formatting clues (bold, large font, etc.)
        if self._looks_like_heading(text):
            # Heuristic: shorter text is more likely to be heading
            if len(text.split()) <= 8:
                return "H2"  # Default to H2 if uncertain
        
        return None
    
    def _looks_like_heading(self, text: str) -> bool:
        """Heuristic to identify heading-like text"""
        # Simple checks - can be enhanced
        if text.isupper():
            return True
        if text.endswith(':'):
            return True
        if text[0].isupper() and not text[1:].islower():
            return True
        return False
    
    def _normalize_text(self, text: str) -> str:
        """Clean and normalize text (supports multilingual)"""
        text = text.strip()
        text = unicodedata.normalize('NFKC', text)  # Normalize unicode
        text = re.sub(r'\s+', ' ', text)  # Collapse whitespace
        return text