#!/usr/bin/env python3
"""
Analyze pdf_4.pdf to find 5 hidden sentences (song lyrics)
"""
import PyPDF2
import sys

def analyze_pdf4(pdf_path):
    """Extract and analyze text from pdf_4.pdf"""

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        print("=" * 80)

        all_text = []

        for page_num, page in enumerate(reader.pages, 1):
            print(f"\n--- Page {page_num} ---")

            # Extract text
            text = page.extract_text()

            if text.strip():
                print(f"Visible text length: {len(text)} characters")
                print("First 500 characters:")
                print(text[:500])
                print("\n...")
                all_text.append(text)
            else:
                print("No visible text extracted")

            # Check for annotations
            if '/Annots' in page:
                print("\nAnnotations found on this page")

            # Try to get hidden text by checking text rendering mode
            try:
                content = page.get_contents()
                if content:
                    content_data = content.get_data()
                    # Look for text rendering mode 3 (invisible text)
                    if b'3 Tr' in content_data:
                        print("\n*** INVISIBLE TEXT FOUND (Rendering mode 3) ***")

                    # Look for white or very light colored text
                    if b'1 1 1 rg' in content_data or b'1 1 1 RG' in content_data:
                        print("\n*** WHITE TEXT FOUND ***")

                    # Look for very small text
                    if b'0.1 ' in content_data or b'0.01 ' in content_data:
                        print("\n*** VERY SMALL TEXT FOUND ***")
            except:
                pass

        print("\n" + "=" * 80)
        print("\nFULL EXTRACTED TEXT:")
        print("=" * 80)
        for i, text in enumerate(all_text, 1):
            print(f"\n--- Page {i} Full Text ---")
            print(text)
            print("\n")

if __name__ == "__main__":
    pdf_path = "/home/user/gogod/AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf"
    analyze_pdf4(pdf_path)
