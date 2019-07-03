# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:18:52 2019

@author: ILYAS
"""
import math

"check is increasing sequence or not"
def is_superincreasing(seq):
    total = 0
    for n in seq:
        if n <= total:
            return False
        total += n
    return True

def coprime(a,b):
    return math.gcd(a,b) == 1

def bits_to_byte(bits):
    if not all(bit in (0, 1) for bit in bits):
        raise BinaryConversionError("Encountered non-bits in bit tuple.")

    byte = 0
    for bit in bits:
        byte *= 2
        if bit:
            byte += 1
    return byte

def byte_to_bits(byte):
    if not 0 <= byte <= 255:
        raise BinaryConversionError(byte)
    out = []
    for i in range(8):
        out.append(byte & 1)
        byte >>= 1
    return tuple(out[::-1])