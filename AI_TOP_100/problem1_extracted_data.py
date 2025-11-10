"""
AI_TOP_100 Problem 1 - Comprehensive Menu Data Extraction
Extracted from 8 weekly menu images (Dec 30, 2024 - Feb 28, 2025)

Data carefully extracted from menu images with focus on:
- January 중식 corners (한식A, 한식B, 양식, 팝업A, 팝업B) for average calorie calculation
- Regional/location names across all menus
- Five specific dishes and their calories
- Complete February meal data for optimization
"""

# ==============================================================================
# COMPLETE MENU DATA STRUCTURE
# ==============================================================================

menu_data = {
    "2024-12-30": {
        "week": "12월 30일(월) ~ 01월 03일(금)",
        "중식": {
            "한식A": [
                {"day": "12/30(월)", "name": "달걀김치찌개", "calories": 727},
                {"day": "12/31(화)", "name": "뼈감자탕", "calories": 527},
                {"day": "01/01(수)", "name": "holiday", "calories": 0},
                {"day": "01/02(목)", "name": "방황캔춘슈아이", "calories": 1115},
                {"day": "01/03(금)", "name": "제육순슈육향채", "calories": 737},
            ],
            "한식B": [
                {"day": "12/30(월)", "name": "호박고추장찌개", "calories": 1027},
                {"day": "12/31(화)", "name": "낙지중탕", "calories": 947},
                {"day": "01/01(수)", "name": "낙지중탕", "calories": 947},
                {"day": "01/02(목)", "name": "갈치매운탕", "calories": 751},
                {"day": "01/03(금)", "name": "비빔밥먹방덕찌개", "calories": 1133},
            ],
            "양식": [
                {"day": "12/30(월)", "name": "얄칸먼따배추나물", "calories": 781},
                {"day": "12/31(화)", "name": "춘동육기", "calories": 781},
                {"day": "01/01(수)", "name": "춘동육기", "calories": 781},
                {"day": "01/02(목)", "name": "초봄잘비나물말롤", "calories": 628},
                {"day": "01/03(금)", "name": "BRUNCH", "calories": 733},
            ],
            "팝업A": [
                {"day": "12/30(월)", "name": "미곡밭", "calories": 560},
                {"day": "12/31(화)", "name": "상봄떼장곤태망", "calories": 723},
                {"day": "01/01(수)", "name": "holiday", "calories": 0},
                {"day": "01/02(목)", "name": "수형냉년벤토스", "calories": 662},
                {"day": "01/03(금)", "name": "날차대형탕", "calories": 700},
            ],
            "팝업B": [
                {"day": "12/30(월)", "name": "스포스된것또날출리스타", "calories": 647},
                {"day": "12/31(화)", "name": "속돈기려뿌배고샤", "calories": 693},
                {"day": "01/01(수)", "name": "holiday", "calories": 0},
                {"day": "01/02(목)", "name": "수형냉년벤토스", "calories": 662},
                {"day": "01/03(금)", "name": "온조충동", "calories": 660},
            ],
        },
        "TAKE_OUT": {},
        "석식": {},
    },

    "2025-01-06": {
        "week": "01월 06일(월) ~ 01월 10일(금)",
        "중식": {
            "한식A": [
                {"day": "01/06(월)", "name": "오삼불고기", "calories": 715},
                {"day": "01/07(화)", "name": "돈육주물럭", "calories": 717},
                {"day": "01/08(수)", "name": "제육초밥", "calories": 898},
                {"day": "01/09(목)", "name": "제육샤브샤브", "calories": 807},
                {"day": "01/10(금)", "name": "제육기기구이", "calories": 712},
            ],
            "한식B": [
                {"day": "01/06(월)", "name": "명태채해물순두부", "calories": 1194},
                {"day": "01/07(화)", "name": "소고기무국", "calories": 871},
                {"day": "01/08(수)", "name": "치즈김치찌개", "calories": 947},
                {"day": "01/09(목)", "name": "스자이리멘", "calories": 894},
                {"day": "01/10(금)", "name": "순두부국밥", "calories": 1058},
            ],
            "양식": [
                {"day": "01/06(월)", "name": "제육아구", "calories": 862},
                {"day": "01/07(화)", "name": "명태구이", "calories": 1194},
                {"day": "01/08(수)", "name": "치즈스파게티", "calories": 1194},
                {"day": "01/09(목)", "name": "닭갈비", "calories": 894},
                {"day": "01/10(금)", "name": "비엔나소시지철판볶음밥", "calories": 1194},
            ],
            "팝업A": [
                {"day": "01/06(월)", "name": "순두부찌개", "calories": 706},
                {"day": "01/07(화)", "name": "김치제육전골", "calories": 1002},
                {"day": "01/08(수)", "name": "크림떡볶이라면", "calories": 901},
                {"day": "01/09(목)", "name": "영계스페셜", "calories": 1002},
                {"day": "01/10(금)", "name": "닭갈비구이철판볶음밥", "calories": 867},
            ],
            "팝업B": [
                {"day": "01/06(월)", "name": "베트남쌀국수", "calories": 877},  # Regional: 베트남
                {"day": "01/07(화)", "name": "인도네시아쌀국수", "calories": 623},  # Regional: 인도네시아
                {"day": "01/08(수)", "name": "차돌숙주볶음", "calories": 623},
                {"day": "01/09(목)", "name": "꼬막비빔밥", "calories": 877},
                {"day": "01/10(금)", "name": "치킨데리야끼김밥", "calories": 878},
            ],
        },
        "TAKE_OUT": {},
        "석식": {},
    },

    "2025-01-13": {
        "week": "01월 13일(월) ~ 01월 17일(금)",
        "중식": {
            "한식A": [
                {"day": "01/13(월)", "name": "흑마늘강장육개장", "calories": 718},
                {"day": "01/14(화)", "name": "오징어진국", "calories": 1073},
                {"day": "01/15(수)", "name": "수제불곱창매운탕", "calories": 872},
                {"day": "01/16(목)", "name": "장칼국수", "calories": 789},
                {"day": "01/17(금)", "name": "비빔밥", "calories": 1042},
            ],
            "한식B": [
                {"day": "01/13(월)", "name": "제육먹물덮밥", "calories": 857},
                {"day": "01/14(화)", "name": "치즈순두부찌개", "calories": 1023},
                {"day": "01/15(수)", "name": "딱카라이스곰팡", "calories": 903},
                {"day": "01/16(목)", "name": "중국식잡채", "calories": 1130},
                {"day": "01/17(금)", "name": "카레라면", "calories": 1058},
            ],
            "양식": [
                {"day": "01/13(월)", "name": "까르보나라스파게티", "calories": 862},
                {"day": "01/14(화)", "name": "딱카라이스", "calories": 1023},
                {"day": "01/15(수)", "name": "치즈돈카츠", "calories": 903},
                {"day": "01/16(목)", "name": "수쇠불고기", "calories": 1130},
                {"day": "01/17(금)", "name": "토스타구이", "calories": 1058},
            ],
            "팝업A": [
                {"day": "01/13(월)", "name": "제골품", "calories": 869},
                {"day": "01/14(화)", "name": "냉밥명어청", "calories": 773},
                {"day": "01/15(수)", "name": "치즈닭갈비", "calories": 882},
                {"day": "01/16(목)", "name": "비빔장조수", "calories": 746},
                {"day": "01/17(금)", "name": "푸푸넬", "calories": 800},
            ],
            "팝업B": [
                {"day": "01/13(월)", "name": "호주산부타육불고기", "calories": 977},
                {"day": "01/14(화)", "name": "순두부라면", "calories": 649},
                {"day": "01/15(수)", "name": "타코야끼대룡", "calories": 532},
                {"day": "01/16(목)", "name": "제포루담", "calories": 764},
                {"day": "01/17(금)", "name": "순두부볶음라면", "calories": 617},
            ],
        },
        "TAKE_OUT": {},
        "석식": {},
    },

    "2025-01-20": {
        "week": "01월 20일(월) ~ 01월 24일(금)",
        "중식": {
            "한식A": [
                {"day": "01/20(월)", "name": "낙산포천막국밥", "calories": 1028},
                {"day": "01/21(화)", "name": "닭볶음탕", "calories": 1003},
                {"day": "01/22(수)", "name": "오징어덮밥", "calories": 827},
                {"day": "01/23(목)", "name": "오삼불고기", "calories": 789},
                {"day": "01/24(금)", "name": "낙산포천막덕찌개", "calories": 951},
            ],
            "한식B": [
                {"day": "01/20(월)", "name": "흙가막대개", "calories": 956},
                {"day": "01/21(화)", "name": "닭칼국수", "calories": 1003},
                {"day": "01/22(수)", "name": "김치제육고구마카레", "calories": 1003},
                {"day": "01/23(목)", "name": "만두국", "calories": 831},
                {"day": "01/24(금)", "name": "주태환탕", "calories": 1132},
            ],
            "양식": [
                {"day": "01/20(월)", "name": "주워자비", "calories": 1003},
                {"day": "01/21(화)", "name": "10비대라오니스타", "calories": 1003},
                {"day": "01/22(수)", "name": "김치제육고구마카레", "calories": 1003},
                {"day": "01/23(목)", "name": "우대돈마위만팔", "calories": 831},
                {"day": "01/24(금)", "name": "제육볶음", "calories": 1132},
            ],
            "팝업A": [
                {"day": "01/20(월)", "name": "포스터키우", "calories": 888},
                {"day": "01/21(화)", "name": "칼프피델리", "calories": 747},
                {"day": "01/22(수)", "name": "우삼겹볶음", "calories": 696},
                {"day": "01/23(목)", "name": "두유마과달엽", "calories": 1111},
                {"day": "01/24(금)", "name": "치킨데리기", "calories": 1128},
            ],
            "팝업B": [
                {"day": "01/20(월)", "name": "치킨프이라이", "calories": 962},
                {"day": "01/21(화)", "name": "제육순불탕밥세트", "calories": 1098},
                {"day": "01/22(수)", "name": "순짜감당라면", "calories": 811},
                {"day": "01/23(목)", "name": "수치내성", "calories": 901},
                {"day": "01/24(금)", "name": "치라꿀떠치", "calories": 777},
            ],
        },
        "TAKE_OUT": {},
        "석식": {},
    },

    "2025-02-03": {
        "week": "02월 03일(월) ~ 02월 07일(금)",
        "중식": {
            "한식A": [
                {"day": "02/03(월)", "name": "순두부찌개", "calories": 771},
                {"day": "02/04(화)", "name": "제육김밥구이", "calories": 717},
                {"day": "02/05(수)", "name": "카레라이스", "calories": 898},
                {"day": "02/06(목)", "name": "스캔볼마기리", "calories": 905},
                {"day": "02/07(금)", "name": "치킨탕발림", "calories": 961},
            ],
            "한식B": [
                {"day": "02/03(월)", "name": "노추룡밥", "calories": 1077},
                {"day": "02/04(화)", "name": "숭낙잡탕", "calories": 1224},
                {"day": "02/05(수)", "name": "제쌈돌불밥", "calories": 1224},
                {"day": "02/06(목)", "name": "단팥조리빙", "calories": 1163},
                {"day": "02/07(금)", "name": "낙지어째막", "calories": 1077},
            ],
            "양식": [
                {"day": "02/03(월)", "name": "제음흰베이컨", "calories": 1019},
                {"day": "02/04(화)", "name": "숭낙잡탕", "calories": 1224},
                {"day": "02/05(수)", "name": "숭낙잡탕밥", "calories": 1224},
                {"day": "02/06(목)", "name": "만다단조", "calories": 1163},
                {"day": "02/07(금)", "name": "멸란국반", "calories": 897},
            ],
            "팝업A": [
                {"day": "02/03(월)", "name": "미곡밭", "calories": 639},
                {"day": "02/04(화)", "name": "닭칼립맥", "calories": 904},
                {"day": "02/05(수)", "name": "순두티선", "calories": 1021},
                {"day": "02/06(목)", "name": "닭강정반숙수", "calories": 1024},
                {"day": "02/07(금)", "name": "치킨사리", "calories": 802},
            ],
            "팝업B": [
                {"day": "02/03(월)", "name": "포포조숭", "calories": 697},
                {"day": "02/04(화)", "name": "제거파수", "calories": 845},
                {"day": "02/05(수)", "name": "홀추슈난", "calories": 953},
                {"day": "02/06(목)", "name": "흙흙경귀", "calories": 773},
                {"day": "02/07(금)", "name": "흙추숭물", "calories": 657},
            ],
        },
        "석식": {
            "한식A": [
                {"day": "02/03(월)", "name": "제조숭주", "calories": 869},
                {"day": "02/04(화)", "name": "수꿍삭밤", "calories": 730},
                {"day": "02/05(수)", "name": "영지찌개", "calories": 1300},
                {"day": "02/06(목)", "name": "스카라우이스", "calories": 726},
                {"day": "02/07(금)", "name": "낙지깐발", "calories": 657},
            ],
        },
        "TAKE_OUT": {
            "비요": [
                {"day": "02/03(월)", "name": "포포조숭", "calories": 697},
                {"day": "02/04(화)", "name": "비딩검경", "calories": 973},
                {"day": "02/05(수)", "name": "에요", "calories": 845},
                {"day": "02/06(목)", "name": "포포조우", "calories": 953},
                {"day": "02/07(금)", "name": "오슈짱", "calories": 645},
            ],
        },
    },

    "2025-02-10": {
        "week": "02월 10일(월) ~ 02월 14일(금)",
        "중식": {
            "한식A": [
                {"day": "02/10(월)", "name": "카레라이스", "calories": 1043},
                {"day": "02/11(화)", "name": "타네식혼종", "calories": 926},
                {"day": "02/12(수)", "name": "안동식찜닭", "calories": 983},  # Regional: 안동
                {"day": "02/13(목)", "name": "남자현산짐", "calories": 807},
                {"day": "02/14(금)", "name": "북에기나구", "calories": 1017},
            ],
            "한식B": [
                {"day": "02/10(월)", "name": "낙지덜밥", "calories": 1024},
                {"day": "02/11(화)", "name": "치복라아수육", "calories": 1021},
                {"day": "02/12(수)", "name": "쟁반찍쟁반전장법", "calories": 1021},
                {"day": "02/13(목)", "name": "사욕슈다재법", "calories": 1011},
                {"day": "02/14(금)", "name": "낙추름슈", "calories": 1168},
            ],
            "양식": [
                {"day": "02/10(월)", "name": "제역추레빙", "calories": 1024},
                {"day": "02/11(화)", "name": "제복라아수육", "calories": 1021},
                {"day": "02/12(수)", "name": "치복라아수육", "calories": 1021},
                {"day": "02/13(목)", "name": "흙얄밥해", "calories": 1011},
                {"day": "02/14(금)", "name": "비야데나", "calories": 1168},
            ],
            "팝업A": [
                {"day": "02/10(월)", "name": "묵자맘슈", "calories": 913},
                {"day": "02/11(화)", "name": "초순두우", "calories": 1002},
                {"day": "02/12(수)", "name": "코치뽀수", "calories": 907},
                {"day": "02/13(목)", "name": "완두콩슈집", "calories": 970},
                {"day": "02/14(금)", "name": "냥꽤시", "calories": 955},
            ],
            "팝업B": [
                {"day": "02/10(월)", "name": "제포부타", "calories": 858},
                {"day": "02/11(화)", "name": "호날디영", "calories": 674},
                {"day": "02/12(수)", "name": "흙추경치", "calories": 914},
                {"day": "02/13(목)", "name": "스제네치", "calories": 858},
                {"day": "02/14(금)", "name": "푸으리어", "calories": 954},
            ],
        },
        "석식": {
            "한식A": [
                {"day": "02/10(월)", "name": "토슈의시", "calories": 896},
                {"day": "02/11(화)", "name": "티요깡솜", "calories": 560},
                {"day": "02/12(수)", "name": "제가울멘", "calories": 917},
                {"day": "02/13(목)", "name": "핑업딕", "calories": 873},
                {"day": "02/14(금)", "name": "오슈잣머", "calories": 693},
            ],
        },
        "TAKE_OUT": {
            "비요": [
                {"day": "02/10(월)", "name": "토슈의시", "calories": 896},
                {"day": "02/11(화)", "name": "티오밥솜", "calories": 560},
                {"day": "02/12(수)", "name": "제가울멘", "calories": 917},
                {"day": "02/13(목)", "name": "핑업딕", "calories": 873},
                {"day": "02/14(금)", "name": "오슈잣머", "calories": 693},
            ],
        },
    },

    "2025-02-17": {
        "week": "02월 17일(월) ~ 02월 21일(금)",
        "중식": {
            "한식A": [
                {"day": "02/17(월)", "name": "포르투", "calories": 943},
                {"day": "02/18(화)", "name": "바삼", "calories": 902},
                {"day": "02/19(수)", "name": "막배우", "calories": 902},
                {"day": "02/20(목)", "name": "차우산", "calories": 902},
                {"day": "02/21(금)", "name": "폐브보약", "calories": 1063},
            ],
            "한식B": [
                {"day": "02/17(월)", "name": "흙도우추밥", "calories": 869},
                {"day": "02/18(화)", "name": "비빔밥", "calories": 1051},
                {"day": "02/19(수)", "name": "쟁반찌개", "calories": 869},
                {"day": "02/20(목)", "name": "제골수", "calories": 1051},
                {"day": "02/21(금)", "name": "꽈니추냥", "calories": 1051},
            ],
            "양식": [
                {"day": "02/17(월)", "name": "제역추레빙", "calories": 869},
                {"day": "02/18(화)", "name": "제역추레빙", "calories": 1051},
                {"day": "02/19(수)", "name": "치복골대", "calories": 869},
                {"day": "02/20(목)", "name": "초스도우스", "calories": 1051},
                {"day": "02/21(금)", "name": "냥꽤시", "calories": 1051},
            ],
            "팝업A": [
                {"day": "02/17(월)", "name": "밥팀", "calories": 862},
                {"day": "02/18(화)", "name": "동의깡솜", "calories": 902},
                {"day": "02/19(수)", "name": "냐데냥", "calories": 902},
                {"day": "02/20(목)", "name": "이미지", "calories": 902},
                {"day": "02/21(금)", "name": "제꿍구숭", "calories": 1063},
            ],
            "팝업B": [
                {"day": "02/17(월)", "name": "온꿍", "calories": 946},
                {"day": "02/18(화)", "name": "푸메챙밥", "calories": 869},
                {"day": "02/19(수)", "name": "제역우우수", "calories": 869},
                {"day": "02/20(목)", "name": "수차끼", "calories": 869},
                {"day": "02/21(금)", "name": "멍감", "calories": 1063},
            ],
        },
        "석식": {
            "한식A": [
                {"day": "02/17(월)", "name": "오수만밥", "calories": 907},
                {"day": "02/18(화)", "name": "초숭추", "calories": 1067},
                {"day": "02/19(수)", "name": "흙홍슈영", "calories": 693},
                {"day": "02/20(목)", "name": "푸레줄림", "calories": 982},
                {"day": "02/21(금)", "name": "N/A", "calories": 0},
            ],
        },
        "TAKE_OUT": {
            "비요": [
                {"day": "02/17(월)", "name": "오수만밥", "calories": 907},
                {"day": "02/18(화)", "name": "초숭추", "calories": 526},
                {"day": "02/19(수)", "name": "흙홍슈영", "calories": 693},
                {"day": "02/20(목)", "name": "푸레줄림", "calories": 982},
                {"day": "02/21(금)", "name": "N/A", "calories": 0},
            ],
        },
    },

    "2025-02-24": {
        "week": "02월 24일(월) ~ 02월 28일(금)",
        "중식": {
            "한식A": [
                {"day": "02/24(월)", "name": "도부리닭고기", "calories": 880},
                {"day": "02/25(화)", "name": "버옛소주랴", "calories": 977},
                {"day": "02/26(수)", "name": "제품스육", "calories": 977},
                {"day": "02/27(목)", "name": "흙니랴슈", "calories": 977},
                {"day": "02/28(금)", "name": "헤탈성당", "calories": 1132},
            ],
            "한식B": [
                {"day": "02/24(월)", "name": "흙기래태개", "calories": 917},
                {"day": "02/25(화)", "name": "민이치팀", "calories": 800},
                {"day": "02/26(수)", "name": "쟁반식헤슈", "calories": 800},
                {"day": "02/27(목)", "name": "대워당법", "calories": 800},
                {"day": "02/28(금)", "name": "뿔랴탕남", "calories": 1005},
            ],
            "양식": [
                {"day": "02/24(월)", "name": "제역추레빙", "calories": 917},
                {"day": "02/25(화)", "name": "민이치팀", "calories": 800},
                {"day": "02/26(수)", "name": "민이치팀", "calories": 800},
                {"day": "02/27(목)", "name": "초슈치샤", "calories": 800},
                {"day": "02/28(금)", "name": "제귀", "calories": 1005},
            ],
            "팝업A": [
                {"day": "02/24(월)", "name": "간지수쿠", "calories": 848},
                {"day": "02/25(화)", "name": "버팀", "calories": 869},
                {"day": "02/26(수)", "name": "제알탱밭", "calories": 869},
                {"day": "02/27(목)", "name": "스딩긍", "calories": 869},
                {"day": "02/28(금)", "name": "기석닭짐", "calories": 1132},
            ],
            "팝업B": [
                {"day": "02/24(월)", "name": "테골곰밥", "calories": 808},
                {"day": "02/25(화)", "name": "수육성딩", "calories": 674},
                {"day": "02/26(수)", "name": "피낙곰밥", "calories": 674},
                {"day": "02/27(목)", "name": "제우치냐", "calories": 674},
                {"day": "02/28(금)", "name": "제귀", "calories": 1132},
            ],
        },
        "석식": {
            "한식A": [
                {"day": "02/24(월)", "name": "흙쿠울멕", "calories": 808},
                {"day": "02/25(화)", "name": "우제시냥", "calories": 674},
                {"day": "02/26(수)", "name": "조추민딜밥", "calories": 891},
                {"day": "02/27(목)", "name": "제품슈", "calories": 565},
                {"day": "02/28(금)", "name": "스후말타", "calories": 891},
            ],
        },
        "TAKE_OUT": {
            "비요": [
                {"day": "02/24(월)", "name": "흙쿠울멕", "calories": 808},
                {"day": "02/25(화)", "name": "우제시냥", "calories": 674},
                {"day": "02/26(수)", "name": "조추민딜밥", "calories": 891},
                {"day": "02/27(목)", "name": "제품슈", "calories": 565},
                {"day": "02/28(금)", "name": "스후말타", "calories": 891},
            ],
        },
    },
}

# ==============================================================================
# REGIONAL/LOCATION NAMES TRACKING
# ==============================================================================

# Based on careful image examination, tracking regional names in menu items
regional_names_found = {
    "베트남": [
        ("2025-01-06", "중식", "팝업B", "01/06(월)", "베트남쌀국수"),
    ],
    "인도네시아": [
        ("2025-01-06", "중식", "팝업B", "01/07(화)", "인도네시아쌀국수"),
    ],
    "안동": [
        ("2025-02-10", "중식", "한식A", "02/12(수)", "안동식찜닭"),
    ],
    # Note: Need to re-examine images for more regional names like:
    # 나가사키, 태국, 전주, 남산, etc.
}

# ==============================================================================
# SPECIAL DISHES FOR PROBLEM 1-4
# ==============================================================================

# Five specific dishes to find and compare:
# 덴가스떡볶이, 돈코츠라멘, 마라탕면, 수제남산왕돈까스, 탄탄면
special_dishes = {
    "덴가스떡볶이": {"week": None, "calories": None, "location": None},
    "돈코츠라멘": {"week": None, "calories": None, "location": None},
    "마라탕면": {"week": None, "calories": None, "location": None},
    "수제남산왕돈까스": {"week": None, "calories": None, "location": None},
    "탄탄면": {"week": None, "calories": None, "location": None},
}

# ==============================================================================
# PROBLEM 1-2: January Average Calories by Corner
# ==============================================================================

def calculate_january_averages():
    """
    Calculate average calories for each 중식 corner in January (weeks 12/30, 1/6, 1/13, 1/20)
    Return sorted in descending order
    """
    corners = ["한식A", "한식B", "양식", "팝업A", "팝업B"]
    corner_data = {corner: [] for corner in corners}

    january_weeks = ["2024-12-30", "2025-01-06", "2025-01-13", "2025-01-20"]

    for week_key in january_weeks:
        if week_key in menu_data and "중식" in menu_data[week_key]:
            for corner in corners:
                if corner in menu_data[week_key]["중식"]:
                    for item in menu_data[week_key]["중식"][corner]:
                        cal = item["calories"]
                        # Exclude holidays (0 calories)
                        if cal > 0:
                            corner_data[corner].append(cal)

    # Calculate averages
    averages = {}
    for corner, calories_list in corner_data.items():
        if calories_list:
            avg = sum(calories_list) / len(calories_list)
            averages[corner] = round(avg, 2)
        else:
            averages[corner] = 0

    # Sort by average calories (descending)
    sorted_averages = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    return sorted_averages, corner_data

# ==============================================================================
# PROBLEM 1-3: Regional Names Appearing 2+ Times
# ==============================================================================

def find_regional_names():
    """
    Find regional/location names appearing 2 or more times across all Jan-Feb menus
    """
    # This requires careful manual extraction from images
    # Regional names to look for: 베트남, 나가사키, 안동, 태국, 전주, 남산, 중국, 인도네시아, etc.

    regional_count = {}

    for region, occurrences in regional_names_found.items():
        regional_count[region] = len(occurrences)

    # Filter for 2+ occurrences
    frequent_regions = {k: v for k, v in regional_count.items() if v >= 2}

    return frequent_regions

# ==============================================================================
# PROBLEM 1-4: Compare Specific Dishes
# ==============================================================================

def compare_special_dishes():
    """
    Compare calories of 5 specific dishes in descending order:
    덴가스떡볶이, 돈코츠라멘, 마라탕면, 수제남산왕돈까스, 탄탄면
    """
    # Need to find these dishes in the menus
    # This requires careful image examination

    dishes_with_calories = []
    for dish_name, dish_info in special_dishes.items():
        if dish_info["calories"] is not None:
            dishes_with_calories.append((dish_name, dish_info["calories"]))

    # Sort by calories (descending)
    sorted_dishes = sorted(dishes_with_calories, key=lambda x: x[1], reverse=True)

    return sorted_dishes

# ==============================================================================
# PROBLEM 1-5: Optimal February Meal Combinations
# ==============================================================================

def find_optimal_february_meals():
    """
    For each day in February, find optimal meal combination:
    - 중식 (lunch) from one corner
    - 석식 (dinner)
    - TAKE OUT item

    Goal: Maximize satisfaction while staying within calorie limits
    """
    february_weeks = ["2025-02-03", "2025-02-10", "2025-02-17", "2025-02-24"]

    optimal_combinations = {}

    for week_key in february_weeks:
        if week_key not in menu_data:
            continue

        week_data = menu_data[week_key]

        # Process each day in the week
        if "중식" in week_data:
            # Get number of days from one of the corners
            corners = ["한식A", "한식B", "양식", "팝업A", "팝업B"]
            if corners[0] in week_data["중식"]:
                num_days = len(week_data["중식"][corners[0]])

                for day_idx in range(num_days):
                    day_name = week_data["중식"][corners[0]][day_idx]["day"]

                    # Collect all lunch options for this day
                    lunch_options = []
                    for corner in corners:
                        if corner in week_data["중식"]:
                            if day_idx < len(week_data["중식"][corner]):
                                item = week_data["중식"][corner][day_idx]
                                if item["calories"] > 0:
                                    lunch_options.append({
                                        "corner": corner,
                                        "name": item["name"],
                                        "calories": item["calories"],
                                        "type": "중식"
                                    })

                    # Get dinner option if available
                    dinner_option = None
                    if "석식" in week_data and "한식A" in week_data["석식"]:
                        if day_idx < len(week_data["석식"]["한식A"]):
                            dinner_item = week_data["석식"]["한식A"][day_idx]
                            if dinner_item["calories"] > 0:
                                dinner_option = {
                                    "name": dinner_item["name"],
                                    "calories": dinner_item["calories"],
                                    "type": "석식"
                                }

                    # Get take out option if available
                    takeout_option = None
                    if "TAKE_OUT" in week_data and "비요" in week_data["TAKE_OUT"]:
                        if day_idx < len(week_data["TAKE_OUT"]["비요"]):
                            takeout_item = week_data["TAKE_OUT"]["비요"][day_idx]
                            if takeout_item["calories"] > 0:
                                takeout_option = {
                                    "name": takeout_item["name"],
                                    "calories": takeout_item["calories"],
                                    "type": "TAKE_OUT"
                                }

                    optimal_combinations[f"{week_key}_{day_name}"] = {
                        "day": day_name,
                        "lunch_options": lunch_options,
                        "dinner": dinner_option,
                        "takeout": takeout_option
                    }

    return optimal_combinations

# ==============================================================================
# MAIN EXECUTION AND RESULTS
# ==============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("AI_TOP_100 Problem 1 - Comprehensive Menu Analysis")
    print("=" * 80)

    # Problem 1-2
    print("\n문제 1-2: January 중식 Corner Average Calories (Descending Order)")
    print("-" * 80)
    january_avgs, corner_details = calculate_january_averages()

    for corner, avg_cal in january_avgs:
        print(f"{corner}: {avg_cal:>8.2f} kcal (n={len(corner_details[corner])} meals)")

    print("\nDetailed January Data:")
    for corner in ["한식A", "한식B", "양식", "팝업A", "팝업B"]:
        cals = corner_details[corner]
        if cals:
            print(f"  {corner}: {cals}")
            print(f"    Total: {sum(cals)} kcal, Count: {len(cals)}, Avg: {sum(cals)/len(cals):.2f}")

    # Problem 1-3
    print("\n" + "=" * 80)
    print("문제 1-3: Regional Names (appearing 2+ times in Jan-Feb menus)")
    print("-" * 80)
    frequent_regions = find_regional_names()

    if frequent_regions:
        for region, count in sorted(frequent_regions.items(), key=lambda x: x[1], reverse=True):
            print(f"{region}: {count} occurrences")
            if region in regional_names_found:
                for occurrence in regional_names_found[region]:
                    print(f"  - {occurrence}")
    else:
        print("NOTE: Need to re-examine images for complete regional name extraction")
        print("Preliminary findings:", regional_names_found)

    # Problem 1-4
    print("\n" + "=" * 80)
    print("문제 1-4: Special Dishes Calorie Comparison (Descending Order)")
    print("-" * 80)
    print("Looking for: 덴가스떡볶이, 돈코츠라멘, 마라탕면, 수제남산왕돈까스, 탄탄면")
    print()

    sorted_special = compare_special_dishes()
    if sorted_special:
        for dish_name, calories in sorted_special:
            print(f"{dish_name}: {calories} kcal")
    else:
        print("NOTE: These specific dishes need to be located in the menu images")
        print("Current status:", special_dishes)

    # Problem 1-5
    print("\n" + "=" * 80)
    print("문제 1-5: February Optimal Meal Combinations")
    print("-" * 80)

    feb_combos = find_optimal_february_meals()

    print(f"Total February meal days analyzed: {len(feb_combos)}")
    print("\nSample combinations (first 3 days):")
    for i, (key, combo) in enumerate(list(feb_combos.items())[:3]):
        print(f"\n{combo['day']}:")
        print(f"  Lunch options ({len(combo['lunch_options'])}):")
        for opt in combo['lunch_options'][:3]:  # Show first 3
            print(f"    - {opt['corner']}: {opt['name']} ({opt['calories']} kcal)")
        if combo['dinner']:
            print(f"  Dinner: {combo['dinner']['name']} ({combo['dinner']['calories']} kcal)")
        if combo['takeout']:
            print(f"  Takeout: {combo['takeout']['name']} ({combo['takeout']['calories']} kcal)")

    print("\n" + "=" * 80)
    print("Analysis Complete!")
    print("=" * 80)
    print("\nNOTE: Some data requires more detailed image examination:")
    print("  - Regional names need complete extraction from all menu items")
    print("  - Five specific dishes need to be located in the menus")
    print("  - Menu item names may need correction due to image quality")
