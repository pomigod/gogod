#!/usr/bin/env python3
"""
PDF 4번 문제: 숨겨진 5개의 노래 가사 찾기
"""

import PyPDF2
import sys

def extract_hidden_text(pdf_path):
    """PDF에서 모든 텍스트 추출 (숨겨진 텍스트 포함)"""

    print(f"분석 중: {pdf_path}\n")

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"총 페이지 수: {len(reader.pages)}\n")

            all_text = []

            for page_num, page in enumerate(reader.pages, 1):
                print(f"=== 페이지 {page_num} ===")

                # 기본 텍스트 추출
                text = page.extract_text()
                print(f"추출된 텍스트 길이: {len(text)} 글자")

                if text.strip():
                    all_text.append(f"\n--- 페이지 {page_num} ---\n{text}")
                    print(f"내용 미리보기: {text[:200]}...")

                print()

            # 전체 텍스트 저장
            output_file = "pdf_4_extracted_text.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("\n".join(all_text))

            print(f"\n전체 텍스트가 {output_file}에 저장되었습니다.")

            # 노래 가사로 보이는 패턴 찾기
            print("\n=== 노래 제목 및 가사 패턴 분석 ===")
            full_text = "\n".join(all_text)

            # 가능한 노래 제목 키워드
            keywords = ["노래", "가사", "제목", "곡명", "Song", "Title", "Lyrics"]
            for keyword in keywords:
                if keyword in full_text:
                    print(f"'{keyword}' 키워드 발견!")

            return full_text

    except Exception as e:
        print(f"오류 발생: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    pdf_path = "AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf"

    text = extract_hidden_text(pdf_path)

    if text:
        print("\n처리 완료!")
