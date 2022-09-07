# Bitwise AND operator: Returns 1 if both the bits are 1 else 0.

a = 10 #= 1010 (Binary)
b = 4 #= 0100 (Binary)

print("And ::",a & b)
"""
= 1010
    &
  0100
= 0000

= 0 (Decimal)
"""

# Bitwise or operator: Returns 1 if either of the bit is 1 else 0.

print("Or ::",a | b)
"""
= 1010
    &
  0100
= 1110

= 14 (Decimal)
"""

# Bitwise not operator: Returns one’s complement of the number.

print("Not ::",~a)
"""
= ~1010
= -(1010 + 1)
= -(1011)
= -11 (Decimal)
"""

# Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.

print("xor ::",a ^ b)
"""
= 1010
   ^
  0100
= 1110
= 14 (Decimal)
"""
