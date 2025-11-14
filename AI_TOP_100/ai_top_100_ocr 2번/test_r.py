#!/usr/bin/env python3
# Test to see what r becomes

# Following the execution order exactly as in decoded_code.c:
r = "A"      # Line 7
r = "H"      # Line 8: r="H"
r = "L"      # Line 8: r="L"
r = "T"      # Line 8: r="T"
r += "Q"     # Line 8: r+="Q" => r="TQ"
r = r + "C"  # Line 9: r=r+"C" => r="TQC"
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
r = "A"      # Line 16: r="A" - RESET!
r = r + "I"  # Line 17
r = r + "T"  # Line 17
r = r + "Q"  # Line 18
r = r + "P"  # Line 18
r += "1"     # Line 18
r += "0"     # Line 19
r += "0"     # Line 19

print(f"r = {r}")
print(f"r reversed = {r[::-1]}")
