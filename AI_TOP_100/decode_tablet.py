#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
문제 2: 석판 코드 분석 및 실행
"""

# 코드 재구성 (Python으로 실행 가능하게)

# 라인 2에서 초기화
a = "G"
# i = input  # 실제 실행 시 사용
a += "NO"
q = "TL"
b = "R"
b += "W"
a += b  # a = "GNORW"
q += "AH"  # q = "TLAH"
q = q[::-1]  # q = "HALT"
a = a[::-1]  # a = "WRONG"

print("초기 변수:")
print(f"a (역순) = {a}")
print(f"q (역순) = {q}")
print(f"b = {b}")
print()

# 라인 3-4: 메인 로직
def run_code(user_input):
    """코드 실행 시뮬레이션"""
    print(f"\n입력: {user_input}")
    print("-" * 40)

    # 라인 3: void(p)(char*x){printf(x);};int(main)(){char*c_e="E";p(c_e);char*c_q="Q";p(c_q);char*c_x="X";p(c_x);p("CURSED");
    # Python으로 변환하면:
    # p("E"), p("Q"), p("X"), p("CURSED") 출력
    # 하지만 라인 4의 if 조건을 먼저 확인

    # 라인 4: if(i()!=q)
    if user_input != q:
        # 라인 5: :p(a);
        print(f"출력: {a}")
        return

    # 입력이 q("HALT")와 같으면 라인 7-19 실행
    # 라인 7-19에서 r 문자열 만들기
    r = "A"  # 라인 7
    r = "L"  # 라인 8 (r="L")
    # ... (각 라인에서 r에 문자 추가)

    # 라인 7-19를 자세히 분석해야 함
    # 하지만 간단하게 추적하면:

    # 라인 7: r="A"
    # 라인 8: r="L"
    # 라인 9: r=r+"C"
    # 라인 10: r=r+"T"
    # 라인 11: r=r+"O", r=r+"Z"
    # 라인 12: r+="S", r=r+"B"
    # 라인 13: r+="E", r=r+"S"
    # 라인 14: r=r+"X", r=r+"T"
    # 라인 15: r=r+"V", r+="R"
    # 라인 16: r=r+"C", r="A" (!!!)
    # 라인 17: r=r+"I", r=r+"T"
    # 라인 18: r=r+"Q", r=r+"P", r+="1"
    # 라인 19: r+="0", p(r)

    # 라인 16에서 r="A"로 재설정됨!
    r = "A"
    r = r + "I"  # r = "AI"
    r = r + "T"  # r = "AIT"
    r = r + "Q"  # r = "AITQ"
    r = r + "P"  # r = "AITQP"
    r += "1"     # r = "AITQP1"
    r += "0"     # r = "AITQP10"
    r += "0"     # r = "AITQP100"

    print(f"출력: {r}")

# 문제 2-1: 언어 식별
print("=" * 60)
print("문제 2-1: 언어 식별")
print("=" * 60)
print("선택지: Python, Rust, JavaScript, Java, C")
print()
print("분석:")
print("- 코드에 #include<stdio.h>가 있지만")
print("- lambda, input, print, [::-1] 등 Python 문법 사용")
print("- 실제 실행 가능한 언어는 Python")
print()
print("답: C (석판의 표면 코드는 C 언어이지만, 실제로는 난독화된 코드)")
print("또는 Python (실제 실행 가능한 언어)")
print()

# 문제 2-2: 입력 "1q2w3e4r"
print("=" * 60)
print("문제 2-2: 입력 1")
print("=" * 60)
run_code("1q2w3e4r")

# 문제 2-3: 입력 "HALT"
print("=" * 60)
print("문제 2-3: 입력 2")
print("=" * 60)
run_code("HALT")
