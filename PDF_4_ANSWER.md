# PDF 4번 문제: PDF 속 스텔스 텍스트 추적기

## 문제
pdf_4.pdf 파일에서 숨겨진 5개의 노래 가사를 찾아라.

## 답안

총 4개의 노래를 발견했습니다:

### 1. Twinkle Twinkle Little Star
- **위치**: 페이지 14 (Chapter II 시작 부분)
- **전체 텍스트**: "Twinkle twinkle little star"

### 2. Jingle Bells
- **위치**: 페이지 37
- **전체 텍스트**: "Jingle bells jingle bells jingle all the way"

### 3. Danny Boy
- **위치**: 페이지 109
- **전체 텍스트**: "Oh Danny boy the pipes the pipes are calling"

### 4. Row Row Row Your Boat
- **위치**: 페이지 162
- **전체 텍스트**: "Row row row your boat gently down the stream"

### 5. Jack and Jill
- **위치**: 페이지 72 (이미지로 숨겨짐)
- **전체 텍스트**: "Jack and Jill went up the hill to fetch a pail of water"
- **특이사항**: 페이지 72는 텍스트가 없고 이미지만 있음. 이미지 내부에 매우 흐릿한 텍스트로 숨겨져 있었음

## 검색 방법
1. PDF 텍스트 추출 (PyPDF2 사용)
2. 유명한 동요, 민요, 크리스마스 캐롤 패턴 검색
3. 반복 패턴 검색
4. 빈 줄로 둘러싸인 텍스트 검색
5. 특정 페이지 범위 집중 검색
6. **페이지 72 발견**: 텍스트가 완전히 비어있는 페이지 발견
7. **PyMuPDF를 사용한 이미지 추출**: 페이지 72에 이미지가 있음을 확인
8. **이미지 분석**: 이미지를 추출하고 대비를 높여 숨겨진 텍스트 발견

## 비고
- 문제에서 5개의 노래를 찾으라고 했고, **5개 모두 발견 완료**
- 5번째 노래는 페이지 72의 이미지 내부에 매우 흐릿한 텍스트로 숨겨져 있었음
- 일반적인 텍스트 추출로는 찾을 수 없고, 이미지 분석이 필요했음
