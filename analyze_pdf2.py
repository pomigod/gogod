#!/usr/bin/env python3
"""
PDF 2 분석 스크립트: 흰색의 작은 텍스트 찾기
"""

import fitz  # PyMuPDF
import sys

def analyze_pdf2(pdf_path):
    """PDF에서 흰색이거나 작은 텍스트를 찾습니다."""

    doc = fitz.open(pdf_path)
    print(f"총 페이지 수: {len(doc)}")
    print("\n" + "="*80)

    all_hidden_texts = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        print(f"\n페이지 {page_num + 1} 분석 중...")

        # 텍스트 블록 추출 (위치, 폰트, 색상 정보 포함)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        font_size = span["size"]
                        color = span["color"]

                        # 색상 분석 (RGB 값)
                        # fitz의 color는 정수로 인코딩되어 있음
                        # 0xRRGGBB 형태
                        r = (color >> 16) & 0xFF
                        g = (color >> 8) & 0xFF
                        b = color & 0xFF

                        # 흰색(또는 매우 밝은 색상) 체크
                        is_white = r > 250 and g > 250 and b > 250

                        # 작은 폰트 체크 (일반적으로 6pt 이하)
                        is_small = font_size < 8

                        if text and (is_white or is_small):
                            print(f"  발견!")
                            print(f"    텍스트: {text}")
                            print(f"    폰트 크기: {font_size:.2f}")
                            print(f"    색상 RGB: ({r}, {g}, {b})")
                            print(f"    흰색?: {is_white}, 작은 폰트?: {is_small}")

                            if is_white and is_small:
                                all_hidden_texts.append((page_num + 1, text, font_size, (r, g, b)))

    doc.close()

    print("\n" + "="*80)
    print("\n발견된 흰색의 작은 텍스트:")
    if all_hidden_texts:
        for page_num, text, size, rgb in all_hidden_texts:
            print(f"  페이지 {page_num}: '{text}' (크기: {size:.2f}, RGB: {rgb})")
    else:
        print("  없음")

    return all_hidden_texts

if __name__ == "__main__":
    pdf_path = "AI_TOP_100/ai_top_100_textfinder 5번/pdf_2.pdf"

    print("PDF 2 분석 시작...")
    print(f"파일: {pdf_path}\n")

    hidden_texts = analyze_pdf2(pdf_path)
