#!/usr/bin/env python3
"""
Comprehensive search for the 5th song lyric
"""
import PyPDF2

pdf_path = '/home/user/gogod/AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf'

# Pages where we found lyrics: 14, 37, 109, 162
# Let's search ALL pages for lines that look like song lyrics

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    print("Searching ALL pages for potential song lyrics...")
    print("Looking for lines with repetition or musical patterns")
    print("=" * 80)

    for page_num in range(1, len(reader.pages) + 1):
        text = reader.pages[page_num - 1].extract_text()

        if text:
            lines = text.split('\n')

            for line in lines:
                stripped = line.strip()

                # Skip very short or very long lines
                if not (15 <= len(stripped) <= 70):
                    continue

                # Look for patterns with repetition
                words = stripped.lower().split()

                # Check for word repetition (at least 2 times)
                word_counts = {}
                for word in words:
                    if len(word) > 2:  # Skip short words
                        word_counts[word] = word_counts.get(word, 0) + 1

                has_repetition = any(count >= 2 for count in word_counts.values())

                # Also look for musical/song keywords
                song_keywords = [
                    'sing', 'song', 'la la', 'doo doo', 'tra la',
                    'merrily', 'gently', 'happy', 'birthday',
                    'skip', 'hop', 'clap', 'dance', 'play',
                    'abc', 'alphabet', 'yankee', 'doodle',
                    'my bonnie', 'shine', 'shining'
                ]

                has_keyword = any(kw in stripped.lower() for kw in song_keywords)

                if has_repetition or has_keyword:
                    print(f"\nPage {page_num}: {stripped}")
