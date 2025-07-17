import re


def is_title_candidate(line):
    words = line.split()
    cap_words = sum(1 for word in words if word[0].isupper())
    return 5 <= len(line) <= 100 and cap_words >= len(words) * 0.5


def is_noise_final(line):
    line_lower = line.lower()

    if len(line) < 4:
        return True
    if line.count('.') > len(line) * 0.5:
        return True
    if re.search(r'\d{4}', line_lower):
        return True
    if re.search(r'\s+\d{1,3}$', line):
        return True
    if re.match(r'^v?\d+\.\d+', line_lower):
        return True

    return False


def is_final_heading(line):
    if re.match(r'^\d+\.\s+[^\d]+', line) and len(line.split()) <= 12:
        return True
    if re.match(r'^\d+\.\d+\s+[^\d]+', line) and len(line.split()) <= 10:
        return True
    if re.match(r'^\d+\.\d+\.\d+\s+[^\d]+', line) and len(line.split()) <= 8:
        return True
    if re.match(r'^Chapter\s+\d+', line, re.IGNORECASE):
        return True

    words = line.split()
    if 1 <= len(words) <= 4 and line[0].isupper():
        if all(word[0].isupper() for word in words if len(word) > 2):
            return True

    return False


def determine_levels(headings):
    for h in headings:
        text = h['text']
        if re.match(r'^\d+\.\s+', text):
            h['level'] = 'H1'
        elif re.match(r'^\d+\.\d+\s+', text):
            h['level'] = 'H2'
        elif re.match(r'^\d+\.\d+\.\d+\s+', text):
            h['level'] = 'H3'
        elif re.match(r'^Chapter\s+\d+', text, re.IGNORECASE):
            h['level'] = 'H1'
        elif len(text.split()) <= 3:
            h['level'] = 'H1'
        else:
            h['level'] = 'H2'
    return headings
