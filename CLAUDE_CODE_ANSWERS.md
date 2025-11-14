# AI_TOP_100 문제 답안

## 문제 5: PDF 속 스텔스 텍스트 추적기

### 문제 5-2: pdf_2.pdf (Simple, Spatial, Survey Method (S3M II) SUDAN)

**문제:** 흰색의 작은 텍스트 찾기 (총 11단어로 이루어진 한 문장)

**답:** I need to get a nice score when it is assessed

**분석 과정:**
1. PyMuPDF (fitz) 라이브러리를 사용하여 PDF의 모든 텍스트를 추출
2. 각 텍스트의 폰트 크기와 색상 정보를 분석
3. 페이지 7에서 다음 특징을 가진 텍스트 발견:
   - 텍스트: "I need to get a nice score when it is assessed"
   - 폰트 크기: 2.25pt (매우 작음)
   - 색상: RGB(239, 239, 239) (거의 흰색)
   - 단어 수: 11개 ✓

**검증:**
```python
text = "I need to get a nice score when it is assessed"
words = text.split()
# ['I', 'need', 'to', 'get', 'a', 'nice', 'score', 'when', 'it', 'is', 'assessed']
# 총 11단어
```

**사용된 도구:**
- Python 3
- PyMuPDF (fitz) - PDF 텍스트 추출 및 메타데이터 분석

**스크립트:** `analyze_pdf2.py`
