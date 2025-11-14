#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
문제 2: 석판 코드 정확한 분석
decoded_code.c 파일의 라인 7-19를 정확히 추적
"""

# decoded_code.c 파일의 라인 7-19를 정확히 읽어서 r 변수 추적

# 라인 7: r="A";
# 라인 8: r="H"; r="L";
# 라인 9: r=r+"C";
# 라인 10: r=r+"T";
# 라인 11: r=r+"O"; r=r+"Z";
# 라인 12: r+="S"; r=r+"B";
# 라인 13: r+="E"; r=r+"S";
# 라인 14: r=r+"X"; r=r+"T";
# 라인 15: r=r+"V"; r+="R";
# 라인 16: r=r+"C"; r="A";
# 라인 17: r=r+"I"; r=r+"T";
# 라인 18: r=r+"Q"; r=r+"P"; r+="1";
# 라인 19: r+="0"; r+="0"; p(r);

def trace_r_variable():
    """r 변수의 값 변화 추적"""
    print("r 변수 추적:")
    print("-" * 50)

    # 라인 7
    r = "A"
    print(f"라인 7: r = {repr(r)}")

    # 라인 8
    r = "H"
    print(f"라인 8-1: r = {repr(r)}")
    r = "L"
    print(f"라인 8-2: r = {repr(r)}")

    # 라인 9
    r = r + "C"
    print(f"라인 9: r = {repr(r)}")

    # 라인 10
    r = r + "T"
    print(f"라인 10: r = {repr(r)}")

    # 라인 11
    r = r + "O"
    print(f"라인 11-1: r = {repr(r)}")
    r = r + "Z"
    print(f"라인 11-2: r = {repr(r)}")

    # 라인 12
    r += "S"
    print(f"라인 12-1: r = {repr(r)}")
    r = r + "B"
    print(f"라인 12-2: r = {repr(r)}")

    # 라인 13
    r += "E"
    print(f"라인 13-1: r = {repr(r)}")
    r = r + "S"
    print(f"라인 13-2: r = {repr(r)}")

    # 라인 14
    r = r + "X"
    print(f"라인 14-1: r = {repr(r)}")
    r = r + "T"
    print(f"라인 14-2: r = {repr(r)}")

    # 라인 15
    r = r + "V"
    print(f"라인 15-1: r = {repr(r)}")
    r += "R"
    print(f"라인 15-2: r = {repr(r)}")

    # 라인 16 - 중요! r이 재설정됨
    r = r + "C"
    print(f"라인 16-1: r = {repr(r)}")
    r = "A"
    print(f"라인 16-2: r = {repr(r)} ← 재설정!")

    # 라인 17
    r = r + "I"
    print(f"라인 17-1: r = {repr(r)}")
    r = r + "T"
    print(f"라인 17-2: r = {repr(r)}")

    # 라인 18
    r = r + "Q"
    print(f"라인 18-1: r = {repr(r)}")
    r = r + "P"
    print(f"라인 18-2: r = {repr(r)}")
    r += "1"
    print(f"라인 18-3: r = {repr(r)}")

    # 라인 19
    r += "0"
    print(f"라인 19-1: r = {repr(r)}")
    r += "0"
    print(f"라인 19-2: r = {repr(r)}")

    print("-" * 50)
    print(f"최종 출력: {r}")
    print()

    return r

# 실행
if __name__ == "__main__":
    print("=" * 60)
    print("문제 2: 석판 코드 정확한 분석")
    print("=" * 60)
    print()

    result = trace_r_variable()

    print()
    print("=" * 60)
    print("답안 정리")
    print("=" * 60)
    print()
    print("문제 2-1: 언어 식별")
    print("  답: C")
    print()
    print("문제 2-2: 입력 1 (1q2w3e4r)")
    print("  답: WRONG")
    print()
    print("문제 2-3: 입력 2 (HALT)")
    print(f"  답: {result}")
