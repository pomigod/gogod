# decoded_code.c의 두 번째 줄 분석
# a="G";i=input;a+="NO";q="TL";b="R";b+="W";a+=b;q+="AH";q=q[::1];a=a[::1];

a = "G"
a += "NO"
q = "TL"
b = "R"
b += "W"
a += b
q += "AH"

# q[::1]은 그대로, q[::-1]이면 역순
# 문제 힌트: "멈추어야 비로소 보이리라" -> 역순으로 읽어야 함
# "스스로를 되돌아보는 주문" -> 역순

print("a =", a)
print("q =", q)
print("a reversed =", a[::-1])
print("q reversed =", q[::-1])

# HALT와 비교해야 함
print("\nExpected input for question 3:", q[::-1])
