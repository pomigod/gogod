#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
문제 2: 고대 유적의 비밀 - 이상한 코드 석판 분석

decoded_code.c 파일을 분석하여 문제 해결
"""

# 코드를 읽고 분석
# 1. 언어 식별
# 2. 입력 1: "1q2w3e4r" 입력 시 출력
# 3. 입력 2: "HALT" 입력 시 출력

# decoded_code.c 파일의 주요 부분 분석:
# - 라인 1: #include<stdio.h>가 있지만 Python lambda도 있음
# - 라인 2-3: Python과 C가 섞여 있음
# - 라인 4: if(i()!=q) - i는 input 함수
# - 라인 7-19: 문자열 r을 만들고 있음

# 코드의 핵심 로직:
# q = "TLAHWRONG"를 역순으로 -> "GNORWHAT"? 아니면 다른 값?
# a = "G" + "NO" + "RW" = "GNORW"를 역순으로 -> "WRON G"?

# 실제 코드를 정리해보면:
code_analysis = """
라인 2:
a="G";i=input;a+="NO";q="TL";b="R";b+="W";a+=b;q+="AH";q=q[::1];a=a[::1];
- a = "G" + "NO" + "RW" = "GNORW"
- q = "TL" + "AH" = "TLAH"
- q=q[::1]은 역순이 아니라 그대로 (Python에서 [::1]은 전체)
- a=a[::1]도 그대로

아 잠깐, q=q[::-1], a=a[::-1]이 아니라 q[::1], a[::1]이면 그대로입니다.

이미지를 다시 보니:
q=q[::-1];a=a[::-1] 일 수도 있습니다.

이미지를 다시 확인해야 합니다.
"""

print(code_analysis)

# 코드를 직접 실행 가능하도록 정리
print("\n" + "=" * 60)
print("코드 재구성 필요 - decoded_code.c 파일을 Python으로 실행 가능하게 변환")
print("=" * 60)
