#!/usr/bin/env python3
"""
PDF에서 숨겨진 노래 가사 찾기 - 고급 분석
"""

import pdfplumber
import re

def analyze_pdf_detailed(pdf_path):
    """PDF의 모든 텍스트 객체를 분석하여 숨겨진 노래 찾기"""

    songs_found = []

    with pdfplumber.open(pdf_path) as pdf:
        print(f"총 페이지: {len(pdf.pages)}\n")

        # 각 페이지를 상세히 분석
        for page_num, page in enumerate(pdf.pages, 1):
            # 모든 텍스트 추출
            text = page.extract_text()

            if not text:
                continue

            # 짧은 라인들을 찾기 (노래 가사일 가능성)
            lines = text.split('\n')
            for line in lines:
                line = line.strip()

                # 유명한 동요/노래 패턴 검색
                patterns = [
                    r'twinkle\s+twinkle\s+little\s+star',
                    r'row\s+row\s+row\s+your\s+boat',
                    r'mary\s+had\s+a\s+little\s+lamb',
                    r'hickory\s+dickory\s+dock',
                    r'humpty\s+dumpty',
                    r'baa\s+baa\s+black\s+sheep',
                    r'london\s+bridge',
                    r'ring\s+around\s+the\s+rosie',
                    r'old\s+macdonald',
                    r'wheels\s+on\s+the\s+bus',
                    r'itsy\s+bitsy\s+spider',
                    r'jack\s+and\s+jill',
                    r'hey\s+diddle\s+diddle',
                    r'little\s+bo\s+peep',
                    r'little\s+miss\s+muffet',
                    r'three\s+blind\s+mice',
                    r'this\s+old\s+man',
                    r'if\s+you[\'\']re\s+happy',
                    r'head\s+shoulders\s+knees',
                    r'five\s+little\s+ducks',
                    r'pop\s+goes\s+the\s+weasel',
                    r'here\s+we\s+go\s+round',
                    r'rock\s+a\s+bye\s+baby',
                ]

                for pattern in patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        song_text = match.group()
                        # 가사의 더 많은 부분 추출
                        start_idx = lines.index(line)
                        full_song = '\n'.join(lines[start_idx:min(start_idx+4, len(lines))])

                        songs_found.append({
                            'page': page_num,
                            'song': song_text,
                            'full_text': full_song
                        })
                        print(f"✓ 페이지 {page_num}에서 발견: {song_text}")
                        print(f"  전체 텍스트: {full_song[:200]}\n")
                        break

        # 중복 제거
        unique_songs = {}
        for song in songs_found:
            key = song['song'].lower().strip()
            if key not in unique_songs:
                unique_songs[key] = song

        print(f"\n=== 최종 결과: {len(unique_songs)}개의 노래 발견 ===")
        for i, (key, song) in enumerate(unique_songs.items(), 1):
            print(f"{i}. {song['song']} (페이지 {song['page']})")

        return list(unique_songs.values())

if __name__ == "__main__":
    pdf_path = "AI_TOP_100/ai_top_100_textfinder 5번/pdf_4.pdf"
    songs = analyze_pdf_detailed(pdf_path)

    # 결과 저장
    with open('pdf_4_songs_found.txt', 'w', encoding='utf-8') as f:
        f.write(f"PDF 4번에서 발견된 노래: {len(songs)}개\n\n")
        for i, song in enumerate(songs, 1):
            f.write(f"{i}. {song['song']} (페이지 {song['page']})\n")
            f.write(f"   {song['full_text']}\n\n")

    print("\n결과가 pdf_4_songs_found.txt에 저장되었습니다.")
