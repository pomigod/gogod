#!/usr/bin/env python3
"""
AI_TOP_100 문제 2번: 고대 유적의 비밀 - 이상한 코드 석판
Claude Code 독립 솔루션 - 완료!
"""

import sys

def main():
    print("="*70)
    print("[문제 2] 고대 유적의 비밀: 이상한 코드 석판")
    print("="*70)

    print("\n[분석] 코드 구조:")
    print("-" * 70)
    print("decoded_code.c는 C와 Python이 섞인 폴리글롯(polyglot) 코드입니다.")
    print()
    print("주요 특징:")
    print("  • Line 1: #include<stdio.h> (C 스타일)")
    print("  • Line 2-3: Python 코드가 포함됨 (lambda, string operations)")
    print("  • Line 4+: Python 코드 본문")
    print("  • Python 특징: lambda, input, print, string slicing [::1], += 연산")
    print()
    print("실제 실행 언어: Python")
    print("  (C 구문은 장식/난독화 목적)")

    print("\n" + "="*70)
    print("[문제 2-1] 언어 식별")
    print("="*70)
    print("\n✓ 답: Python")
    print("\n이유:")
    print("  - lambda 함수 사용")
    print("  - input() 함수")
    print("  - String slicing q[::1], a[::1]")
    print("  - String concatenation with +=")
    print("  - list() syntax")

    print("\n" + "="*70)
    print("[코드 동작 분석]")
    print("="*70)
    print("\n핵심 로직:")
    print("  1. a = 'GNORW' (역순하면 'WRONG')")
    print("  2. q = 'TLAH' (역순하면 'HALT')")
    print("  3. if input() != q: print(a) and exit")
    print("  4. else: build string r and print it")
    print()
    print("힌트 해석: '멈추어야 비로소 보이리라'")
    print("  → 'HALT'를 역순으로 하면 'TLAH'")
    print("  → 출력 'GNORW'를 역순으로 하면 'WRONG'")

    print("\n" + "="*70)
    print("[문제 2-2] '1q2w3e4r' 입력 시 출력")
    print("="*70)
    print("\n✓ 답: GNORW")
    print("\n설명:")
    print("  입력 '1q2w3e4r' ≠ 'TLAH'")
    print("  → if 조건이 True")
    print("  → a ('GNORW')를 출력하고 종료")
    print("\n  (역순 해석: 'GNORW' → 'WRONG')")

    print("\n" + "="*70)
    print("[문제 2-3] 'HALT' 입력 시 출력")
    print("="*70)
    print("\n✓ 답: GNORW")
    print("\n설명:")
    print("  입력 'HALT' ≠ 'TLAH'")
    print("  → if 조건이 True")
    print("  → a ('GNORW')를 출력하고 종료")
    print("\n  (역순 해석: 'GNORW' → 'WRONG')")
    print("\n참고: 'TLAH'를 입력하면 'AITQP100'이 출력됩니다.")

    print("\n" + "="*70)
    print("최종 답안 요약:")
    print("-" * 70)
    print("  2-1. 언어: Python")
    print("  2-2. '1q2w3e4r' 입력 시 출력: GNORW")
    print("  2-3. 'HALT' 입력 시 출력: GNORW")
    print("="*70)

if __name__ == "__main__":
    main()
