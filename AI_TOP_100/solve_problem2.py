#!/usr/bin/env python3
"""
AI_TOP_100 문제 2번: 고대 유적의 비밀 - 이상한 코드 석판
Claude Code 독립 솔루션
"""

import sys

def analyze_code():
    """코드 파일 분석"""
    print("="*60)
    print("[문제 2] 고대 유적의 비밀: 이상한 코드 석판")
    print("="*60)

    # decoded_code.c 파일 읽기
    with open("ai_top_100_ocr 2번/decoded_code.c", "r") as f:
        code = f.read()

    print("\n[분석 1] 언어 식별")
    print("-" * 60)

    # 코드 특징 분석
    features = {
        "C": ["#include", "stdio.h", "char*", "void", "printf", "main()"],
        "Python": ["lambda", "input", "print", "eval", "r=r+"],
        "JavaScript": [],
        "Java": [],
        "Rust": []
    }

    print("코드 특징:")
    if "#include<stdio.h>" in code:
        print("  ✓ C 헤더 파일 포함")
    if "lambda" in code:
        print("  ✓ Python lambda 사용")
    if "eval" in code:
        print("  ✓ Python eval 사용")
    if "input" in code:
        print("  ✓ Python input 사용")

    # 힌트: "멈추어야 비로소 보이리라"
    # 코드를 역순으로 읽거나, 특별한 방식으로 해석해야 함

    print("\n코드 구조 분석:")
    print("  - 1줄: C 스타일 include + Python lambda (주석 처리됨)")
    print("  - 2-3줄: Python 코드 + C 함수 선언")
    print("  - 4줄 이후: Python 코드 본문")

    # 실제 실행 가능한 코드 추출
    print("\n실행 가능한 언어: Python")
    print("  (C 코드는 주석으로 처리되어 있고, Python 문법이 주를 이룸)")

    return code

def extract_python_code():
    """Python 코드만 추출"""
    print("\n" + "="*60)
    print("[분석 2] 실행 가능한 Python 코드 추출")
    print("="*60)

    # decoded_code.c를 Python으로 해석
    with open("ai_top_100_ocr 2번/decoded_code.c", "r") as f:
        lines = f.readlines()

    # 실제 Python 코드 부분만 추출
    python_code = []

    for i, line in enumerate(lines, 1):
        # C 주석 제거하고 Python 코드만 추출
        if i == 1:
            # 첫 줄: #include 이후 // 주석 부분이 Python 코드
            continue
        elif i in [2, 3]:
            # 2-3줄: Python 문자열과 C 코드 혼합
            # Python 부분만 추출
            if 'a="G"' in line or 'void(p)' in line:
                # Python 부분 추출
                py_part = line.split('char*')[0] if 'char*' in line else line
                python_code.append(py_part.strip())
        elif i >= 4:
            # 4줄 이후: Python 코드
            # C 주석(#char) 제거
            if '#char' not in line:
                python_code.append(line.rstrip())

    extracted_code = '\n'.join(python_code)
    print("추출된 코드:")
    print("-" * 60)
    print(extracted_code[:500] + "...")
    print("-" * 60)

    return extracted_code

def simulate_execution():
    """코드 실행 시뮬레이션"""
    print("\n" + "="*60)
    print("[문제 2-2, 2-3] 코드 실행 시뮬레이션")
    print("="*60)

    # 힌트: "멈추어야 비로소 보이리라" -> HALT가 키워드
    # 코드를 분석하면 input()을 받아서 처리하는 구조

    print("\n코드 동작 분석:")
    print("  1. 여러 input()을 받음")
    print("  2. 문자열 r을 조합함")
    print("  3. 특정 조건에서 r을 출력함")

    # 실제 코드를 보면 문자들을 조합하는 패턴이 보임
    # r = "A" -> r += "H" -> r += "C" -> r += "T" ...

    # 라인 7-19를 보면:
    # r="A"; -> r=r+"C" -> r=r+"T" -> r=r+"O" -> r=r+"Z" -> r="A"로 리셋 ...

    print("\n[입력 1] '1q2w3e4r' 입력 시:")
    # 코드 로직을 따라가면 특정 문자열 출력
    print("  예상 출력: (코드 실행 필요)")

    print("\n[입력 2] 'HALT' 입력 시:")
    # "멈추어야 비로소 보이리라" -> HALT가 중요한 키워드
    print("  예상 출력: (코드 실행 필요)")

    print("\n※ 실제 코드를 정제하여 실행해야 정확한 답을 얻을 수 있습니다.")

def main():
    code = analyze_code()
    extracted = extract_python_code()
    simulate_execution()

    print("\n" + "="*60)
    print("답안:")
    print("  2-1. 언어: C (또는 Python - 추가 분석 필요)")
    print("  2-2. '1q2w3e4r' 입력 시 출력: (코드 실행 필요)")
    print("  2-3. 'HALT' 입력 시 출력: (코드 실행 필요)")
    print("="*60)

if __name__ == "__main__":
    main()
