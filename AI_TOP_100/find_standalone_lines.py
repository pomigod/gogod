#!/usr/bin/env python3
"""
Find short standalone lines that might be hidden song lyrics
"""
import PyPDF2

def find_standalone_lines(pdf_path):
    """Find short standalone lines that could be hidden lyrics"""

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        print(f"Searching {len(reader.pages)} pages for standalone short lines...")
        print("=" * 80)

        found_lines = []

        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()

            if text:
                lines = text.split('\n')

                for i, line in enumerate(lines):
                    line_stripped = line.strip()

                    # Look for short lines (potential song lyrics)
                    # Between 10 and 60 characters, not just numbers
                    if 10 <= len(line_stripped) <= 60 and not line_stripped.isdigit():
                        # Check if it's not part of a paragraph (has empty lines around it)
                        # or if it contains repeated words
                        words = line_stripped.lower().split()

                        # Check for repetition (like "row row row" or "jingle bells jingle bells")
                        has_repetition = False
                        for word in set(words):
                            if len(word) > 2 and words.count(word) >= 2:
                                has_repetition = True
                                break

                        # Also check if line looks like it could be a song title/lyric
                        # (contains common song words)
                        song_indicators = ['twinkle', 'jingle', 'row', 'mary', 'little', 'old',
                                         'baa', 'humpty', 'jack', 'london', 'wheels', 'star',
                                         'boat', 'bell', 'sheep', 'farm', 'spider', 'bridge']

                        has_song_word = any(indicator in line_stripped.lower() for indicator in song_indicators)

                        if has_repetition or has_song_word:
                            found_lines.append({
                                'page': page_num,
                                'line': line_stripped
                            })

                            print(f"\nPage {page_num}: {line_stripped}")

        return found_lines

if __name__ == "__main__":
    pdf_path = "/home/user/gogod/AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf"
    lines = find_standalone_lines(pdf_path)

    print(f"\n\n{'=' * 80}")
    print(f"Total standalone lines found: {len(lines)}")
