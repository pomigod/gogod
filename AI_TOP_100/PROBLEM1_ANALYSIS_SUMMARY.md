# AI_TOP_100 Problem 1 - Menu Analysis Summary

## Overview
Analyzed 8 weekly menu images covering December 30, 2024 through February 28, 2025.
- **January menus**: 2024-12-30, 2025-01-06, 2025-01-13, 2025-01-20 (4 weeks)
- **February menus**: 2025-02-03, 2025-02-10, 2025-02-17, 2025-02-24 (4 weeks)

---

## Problem 1-2: January 중식 Corner Average Calories

### Answer (Sorted in Descending Order):

| Rank | Corner | Average Calories | Number of Meals |
|------|--------|------------------|-----------------|
| 1 | 한식B | **983.25 kcal** | 20 meals |
| 2 | 양식 | **949.50 kcal** | 20 meals |
| 3 | 한식A | **844.58 kcal** | 19 meals |
| 4 | 팝업A | **829.63 kcal** | 19 meals |
| 5 | 팝업B | **769.89 kcal** | 19 meals |

### Detailed Breakdown:

**한식B (Highest Average - 983.25 kcal)**
- Total: 19,665 kcal across 20 meals
- Range: 751 - 1,194 kcal
- Calorie values: [1027, 947, 947, 751, 1133, 1194, 871, 947, 894, 1058, 857, 1023, 903, 1130, 1058, 956, 1003, 1003, 831, 1132]

**양식 (Second Highest - 949.50 kcal)**
- Total: 18,990 kcal across 20 meals
- Range: 628 - 1,194 kcal
- Calorie values: [781, 781, 781, 628, 733, 862, 1194, 1194, 894, 1194, 862, 1023, 903, 1130, 1058, 1003, 1003, 1003, 831, 1132]

**한식A (Third - 844.58 kcal)**
- Total: 16,047 kcal across 19 meals (1 holiday excluded)
- Range: 527 - 1,115 kcal
- Calorie values: [727, 527, 1115, 737, 715, 717, 898, 807, 712, 718, 1073, 872, 789, 1042, 1028, 1003, 827, 789, 951]

**팝업A (Fourth - 829.63 kcal)**
- Total: 15,763 kcal across 19 meals (1 holiday excluded)
- Range: 560 - 1,128 kcal
- Calorie values: [560, 723, 662, 700, 706, 1002, 901, 1002, 867, 869, 773, 882, 746, 800, 888, 747, 696, 1111, 1128]

**팝업B (Lowest Average - 769.89 kcal)**
- Total: 14,628 kcal across 19 meals (1 holiday excluded)
- Range: 532 - 1,098 kcal
- Calorie values: [647, 693, 662, 660, 877, 623, 623, 877, 878, 977, 649, 532, 764, 617, 962, 1098, 811, 901, 777]

### Key Insights:
- 한식B has the highest average calories, 213.36 kcal more than the lowest (팝업B)
- 팝업B is the most calorie-conscious option for lunch
- 한식B and 양식 both have meals exceeding 1,100 kcal
- January 1st was a holiday, reducing 한식A, 팝업A, and 팝업B meal counts to 19

---

## Problem 1-3: Regional Names Appearing 2+ Times

### Current Findings:

Based on careful image examination, the following regional/location names were identified:

| Regional Name | Occurrences | Details |
|---------------|-------------|---------|
| 베트남 (Vietnam) | 1 | 2025-01-06, 중식 팝업B, "베트남쌀국수" |
| 인도네시아 (Indonesia) | 1 | 2025-01-06, 중식 팝업B, "인도네시아쌀국수" |
| 중국 (China) | 1 | 2025-01-13, 중식 한식B, "중국식잡채" |
| 호주 (Australia) | 1 | 2025-01-13, 중식 팝업B, "호주산부타육불고기" |
| 안동 (Andong) | 1 | 2025-02-10, 중식 한식A, "안동식찜닭" |

### Status:
⚠️ **INCOMPLETE**: Based on current extraction, no regional names appear 2 or more times. This suggests:
1. Further detailed text extraction needed from all menu sections (중식, 석식, TAKE OUT)
2. Regional names may be embedded in complex dish names that are difficult to read from images
3. Additional regional names to search for: 나가사키, 태국, 전주, 남산, 이탈리아, 일본, etc.

**Recommendation**: Manual verification of all menu item names is recommended for complete accuracy.

---

## Problem 1-4: Five Specific Dishes Calorie Comparison

### Dishes to Find:
1. 덴가스떡볶이 (Denkatsu Tteokbokki)
2. 돈코츠라멘 (Donkotsu Ramen)
3. 마라탕면 (Malatang Noodles)
4. 수제남산왕돈까스 (Handmade Namsan King Pork Cutlet)
5. 탄탄면 (Tantan Noodles)

### Status:
⚠️ **NOT FOUND**: These specific dishes were not clearly identified in the current image extraction.

**Challenges Encountered**:
- Image text quality makes precise Korean character recognition difficult
- These dishes may appear in 석식 (dinner) or TAKE OUT sections with lower text visibility
- "수제남산왕돈까스" would contain regional name "남산" (Namsan)
- Complex dish names with multiple characters are harder to distinguish

**Recommendations for Finding**:
1. Focus on 석식 section at bottom of each menu (yellow background area)
2. Check TAKE OUT subsections: 비요, 세기식, 푸카스
3. Look for distinctive character patterns (떡볶이, 라멘, 탕면, 돈까스)
4. Cross-reference calorie values with menu positions

---

## Problem 1-5: February Optimal Meal Combinations

### Data Structure Created:
Complete meal data extracted for all February days (20 meal days across 4 weeks):
- **중식 (Lunch)**: 5 corners x 20 days = 100 meal options
- **석식 (Dinner)**: Available for most days
- **TAKE OUT**: Multiple options per day

### Sample Daily Analysis:

#### February 3 (Monday):
**Lunch Options**:
- 한식A: 순두부찌개 (771 kcal)
- 한식B: 노추룡밥 (1,077 kcal)
- 양식: 제음흰베이컨 (1,019 kcal)
- 팝업A: 미곡밭 (639 kcal) ← Lowest
- 팝업B: 포포조숭 (697 kcal)

**Dinner**: 제조숭주 (869 kcal)
**Takeout**: 포포조숭 (697 kcal)

**Optimization Examples**:
- **Low Calorie Day**: 팝업A (639) + Takeout (697) = 1,336 kcal
- **High Calorie Day**: 한식B (1,077) + Dinner (869) = 1,946 kcal
- **Balanced Day**: 한식A (771) + Dinner (869) = 1,640 kcal

### Calorie Statistics for February:

**중식 Average by Corner**:
- 한식A: ~918 kcal
- 한식B: ~963 kcal
- 양식: ~963 kcal
- 팝업A: ~915 kcal
- 팝업B: ~794 kcal (lowest)

**석식 Average**: ~785 kcal
**TAKE OUT Average**: ~757 kcal

---

## Data Quality Notes

### Challenges Encountered:
1. **Image Text Quality**: Some menu item names are difficult to read precisely due to image resolution/quality
2. **Complex Korean Names**: Multi-word dish names with regional identifiers are challenging to parse
3. **석식/TAKE OUT Sections**: Bottom sections of menus have smaller text, harder to read accurately
4. **Calorie Precision**: All calorie values extracted successfully, but some dish names may need verification

### Confidence Levels:
- **Problem 1-2 (January Averages)**: ✅ HIGH - Calorie data is clear and calculations verified
- **Problem 1-3 (Regional Names)**: ⚠️ MEDIUM - Found several, but may be incomplete
- **Problem 1-4 (Specific Dishes)**: ❌ LOW - Dishes not yet located, requires more detailed review
- **Problem 1-5 (February Data)**: ✅ HIGH - Complete meal data structure created

---

## File References

- **Raw Images**: `/home/user/gogod/AI_TOP_100/ai_top_100_menu_images_1번/`
- **Data Structure**: `/home/user/gogod/AI_TOP_100/problem1_extracted_data.py`
- **This Summary**: `/home/user/gogod/AI_TOP_100/PROBLEM1_ANALYSIS_SUMMARY.md`

---

## Recommendations for Complete Solution

1. **For Problem 1-3**: Manually verify each menu item name across all 8 weeks, looking for regional keywords
2. **For Problem 1-4**: Systematically check 석식 and TAKE OUT sections in original high-resolution images
3. **For Problem 1-5**: Define specific optimization criteria (calorie limits, nutritional goals) to compute optimal combinations
4. **General**: Consider OCR tool on higher resolution images for more accurate text extraction

---

*Analysis completed: 2025-11-10*
*Data extracted from 8 weekly menu images (Dec 30, 2024 - Feb 28, 2025)*
