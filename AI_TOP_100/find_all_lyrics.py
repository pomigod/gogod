#!/usr/bin/env python3
"""
Find ALL 5 hidden song lyrics in pdf_4.pdf
Search page by page for complete song lyrics
"""
import PyPDF2
import re

def find_all_lyrics(pdf_path):
    """Extract text from all pages and find song lyrics"""

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        found_lyrics = []

        print(f"Searching {len(reader.pages)} pages...")
        print("=" * 80)

        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()

            if text:
                # Look for patterns that look like song titles or lyrics
                # (multiple words on a single line, often with repetition)
                lines = text.split('\n')

                for i, line in enumerate(lines):
                    line_stripped = line.strip()

                    # Skip very long lines (likely regular text) and empty lines
                    if len(line_stripped) > 60 or len(line_stripped) == 0:
                        continue

                    # Check for repetitive patterns (like "row row row" or "jingle bells jingle bells")
                    words = line_stripped.lower().split()
                    if len(words) >= 3:
                        # Check for repeated words
                        for word in set(words):
                            if words.count(word) >= 2:
                                # Get context
                                start_idx = max(0, i-2)
                                end_idx = min(len(lines), i+3)
                                context = '\n'.join(lines[start_idx:end_idx])

                                found_lyrics.append({
                                    'page': page_num,
                                    'line': line_stripped,
                                    'context': context
                                })

                                print(f"\n*** Potential lyric on Page {page_num} ***")
                                print(f"Line: {line_stripped}")
                                print(f"Context:\n{context}")
                                print("-" * 80)
                                break

        return found_lyrics

if __name__ == "__main__":
    pdf_path = "/home/user/gogod/AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf"
    lyrics = find_all_lyrics(pdf_path)

    print(f"\n\nTotal potential lyrics found: {len(lyrics)}")
