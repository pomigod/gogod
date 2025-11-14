#!/usr/bin/env python3
# Cleaned up version of decoded_code.c - extracting only meaningful Python code

# Line 2 - Variable initialization
a = "G"
a += "NO"
q = "TL"
b = "R"
b += "W"
a += b
q += "AH"
q = q[::-1]  # Reverse: "HALT"
a = a[::-1]  # Reverse: "WRONG"
i = input

# Lines 7-19 - Building string r (extracting only r assignments)
# Following the execution order:
r = "A"      # Line 7
r = "H"      # Line 8
r = "L"      # Line 8
r = "T"      # Line 8
r += "Q"     # Line 8
r = r + "C"  # Line 9
r = r + "T"  # Line 10
r = r + "O"  # Line 11
r = r + "Z"  # Line 11
r += "S"     # Line 12
r = r + "B"  # Line 12
r += "E"     # Line 13
r = r + "S"  # Line 13
r = r + "X"  # Line 14
r = r + "T"  # Line 14
r = r + "V"  # Line 15
r += "R"     # Line 15
r = r + "C"  # Line 16
r = "A"      # Line 16 - RESET!
r = r + "I"  # Line 17
r = r + "T"  # Line 17
r = r + "Q"  # Line 18
r = r + "P"  # Line 18
r += "1"     # Line 18
r += "0"     # Line 19 (first)
r += "0"     # Line 19 (second)

print(f"a = {a}")
print(f"q = {q}")
print(f"r = {r}")

# Main logic: read input and compare with q
user_input = i()
if user_input != q:
    print(a)  # Print "WRONG"
else:
    print(r)  # Print the r string
