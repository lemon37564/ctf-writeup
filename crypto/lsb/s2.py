#! /usr/bin/python3
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
import os

FLAG = b"FLAG{abcdefghijklmnopqrstuvwxyz}"

p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi)

m = bytes_to_long(FLAG + os.urandom(256 - len(FLAG)))
assert m < n
enc = pow(m, e, n)
# print(n)
# print(e)
# print(enc)

res = []
inp = enc

while inp > 0:
    pt = pow(inp, d, n)
    res.append(pt % 2)
    inp >>= e

print(res)