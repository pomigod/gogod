# AI_TOP_100 문제 답안

## 문제 2: 고대 유적의 비밀 - 이상한 코드 석판

### 문제 설명
석판 이미지의 문자를 판독해 텍스트를 얻고, 그 의미를 해석하여 정답 형식에 맞춰 제출하는 문제입니다.
- 힌트: "멈추어야 비로소 보이리라" - HALT와 관련
- 힌트: "스스로를 되돌아보는 주문" - 역순/반전과 관련

### 코드 분석 과정

1. **석판 이미지 확인**: `AI_TOP_100/ai_top_100_ocr 2번/ai_top_100_crypto.png`
2. **디코딩된 코드**: `AI_TOP_100/ai_top_100_ocr 2번/decoded_code.c`
3. **코드 특징**: C와 Python이 섞인 polyglot 코드

### 주요 변수 분석

코드 2번째 줄에서 변수들을 초기화합니다:
```python
a = "G" + "NO" + "RW" = "GNORW"
a[::-1] = "WRONG"  # 역순

q = "TL" + "AH" = "TLAH"
q[::-1] = "HALT"  # 역순
```

코드 7-19번 줄에서 `r` 변수를 구성합니다:
- 16번 줄에서 `r = "A"`로 리셋됨
- 최종적으로 `r = "AITQP100"`

### 프로그램 로직

```python
user_input = input()
if user_input != q:  # q = "HALT"
    print(a)  # "WRONG"
else:
    print(r)  # "AITQP100"
```

### 답안

#### 2-1. 언어 식별
**답: Python**

코드는 C와 Python이 섞인 polyglot이지만, 실제로 실행 가능한 형태는 Python입니다.
- C로 컴파일 시도: 실패 (다수의 구문 오류)
- Python으로 실행: 성공

#### 2-2. 입력 "1q2w3e4r"의 출력
**답: WRONG**

입력값 "1q2w3e4r"는 q("HALT")와 다르므로, a 변수의 값인 "WRONG"을 출력합니다.

#### 2-3. 입력 "HALT"의 출력
**답: AITQP100**

입력값 "HALT"는 q("HALT")와 같으므로, r 변수의 값인 "AITQP100"을 출력합니다.

---

### 검증 스크립트

답안 검증에 사용한 Python 스크립트는 다음 위치에 있습니다:
- `AI_TOP_100/ai_top_100_ocr 2번/analyze.py` - 변수 분석
- `AI_TOP_100/ai_top_100_ocr 2번/test_r.py` - r 변수 최종값 확인
- `AI_TOP_100/ai_top_100_ocr 2번/final_test.py` - 최종 검증

