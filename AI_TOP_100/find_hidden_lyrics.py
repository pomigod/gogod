#!/usr/bin/env python3
"""
Find 5 hidden song lyrics in pdf_4.pdf
"""
import PyPDF2
import re

def find_hidden_lyrics(pdf_path):
    """Search for song lyrics/nursery rhymes in PDF"""

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Common song/nursery rhyme patterns
        song_patterns = [
            r'twinkle.*star',
            r'row.*row.*boat',
            r'mary.*had.*little.*lamb',
            r'london.*bridge',
            r'humpty.*dumpty',
            r'jack.*jill',
            r'old.*macdonald',
            r'itsy.*bitsy.*spider',
            r'wheels.*bus',
            r'happy.*birthday',
            r'jingle.*bells',
            r'silent.*night',
            r'abc.*song',
        ]

        found_lyrics = []

        print(f"Searching {len(reader.pages)} pages for hidden song lyrics...")
        print("=" * 80)

        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()

            if text:
                text_lower = text.lower()

                # Check each pattern
                for pattern in song_patterns:
                    matches = re.finditer(pattern, text_lower, re.IGNORECASE | re.DOTALL)
                    for match in matches:
                        # Get context around the match (50 chars before and after)
                        start = max(0, match.start() - 50)
                        end = min(len(text), match.end() + 100)
                        context = text[start:end].strip()

                        found_lyrics.append({
                            'page': page_num,
                            'text': context,
                            'pattern': pattern
                        })

                        print(f"\n*** FOUND on Page {page_num} ***")
                        print(f"Pattern: {pattern}")
                        print(f"Context: {context}")
                        print("-" * 80)

        print(f"\n\nTotal song lyrics found: {len(found_lyrics)}")
        print("=" * 80)

        return found_lyrics

if __name__ == "__main__":
    pdf_path = "/home/user/gogod/AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf"
    lyrics = find_hidden_lyrics(pdf_path)

    print("\n\nSUMMARY OF FOUND LYRICS:")
    print("=" * 80)
    for i, lyric in enumerate(lyrics, 1):
        print(f"{i}. Page {lyric['page']}: {lyric['text'][:80]}...")
