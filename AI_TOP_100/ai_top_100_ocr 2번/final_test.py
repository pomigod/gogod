#!/usr/bin/env python3
# Final test for both inputs

# Variable initialization
a = "G"
a += "NO"
q = "TL"
b = "R"
b += "W"
a += b
q += "AH"
q = q[::-1]  # "HALT"
a = a[::-1]  # "WRONG"

# Build r string
r = "A"
r = "H"
r = "L"
r = "T"
r += "Q"
r = r + "C"
r = r + "T"
r = r + "O"
r = r + "Z"
r += "S"
r = r + "B"
r += "E"
r = r + "S"
r = r + "X"
r = r + "T"
r = r + "V"
r += "R"
r = r + "C"
r = "A"      # RESET
r = r + "I"
r = r + "T"
r = r + "Q"
r = r + "P"
r += "1"
r += "0"
r += "0"

print(f"Expected q (HALT input): {q}")
print(f"Expected a (WRONG output): {a}")
print(f"Final r value: {r}")
print()

# Test 1: input "1q2w3e4r"
test_input_1 = "1q2w3e4r"
print(f"Test 1: Input = '{test_input_1}'")
if test_input_1 != q:
    print(f"Output: {a}")
else:
    print(f"Output: {r}")
print()

# Test 2: input "HALT"
test_input_2 = "HALT"
print(f"Test 2: Input = '{test_input_2}'")
if test_input_2 != q:
    print(f"Output: {a}")
else:
    print(f"Output: {r}")
