#!/usr/bin/env python3
"""
Search for remaining song lyrics in pdf_4.pdf
Focus on complete nursery rhyme lines
"""
import PyPDF2
import re

def search_for_specific_patterns(pdf_path):
    """Search for specific nursery rhyme patterns"""

    # Patterns to search for (full lines)
    patterns = [
        r'mary\s+had\s+a\s+little\s+lamb',
        r'baa\s+baa\s+black\s+sheep',
        r'humpty\s+dumpty',
        r'london\s+bridge\s+is\s+falling',
        r'old\s+macdonald\s+had\s+a\s+farm',
        r'itsy\s+bitsy\s+spider',
        r'hickory\s+dickory\s+dock',
        r'jack\s+and\s+jill',
        r'little\s+miss\s+muffet',
        r'hey\s+diddle\s+diddle',
        r'pat-a-cake',
        r'ring\s+around\s+the\s+rosie',
        r'three\s+blind\s+mice',
        r'pop\s+goes\s+the\s+weasel',
        r'hot\s+cross\s+buns',
        r'peter\s+piper',
        r'sing\s+a\s+song\s+of\s+sixpence',
    ]

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        print(f"Searching {len(reader.pages)} pages for nursery rhymes...")
        print("=" * 80)

        found = []

        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()

            if text:
                text_lower = text.lower()

                for pattern in patterns:
                    matches = re.finditer(pattern, text_lower, re.IGNORECASE)
                    for match in matches:
                        # Get the full line
                        lines = text.split('\n')
                        for line in lines:
                            if pattern.replace(r'\s+', ' ').replace('\\', '') in line.lower():
                                found.append({
                                    'page': page_num,
                                    'line': line.strip(),
                                    'pattern': pattern
                                })

                                print(f"\n*** FOUND on Page {page_num} ***")
                                print(f"Pattern: {pattern}")
                                print(f"Line: {line.strip()}")
                                print("-" * 80)
                                break

        return found

if __name__ == "__main__":
    pdf_path = "/home/user/gogod/AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf"
    results = search_for_specific_patterns(pdf_path)

    print(f"\n\nTotal nursery rhymes found: {len(results)}")
