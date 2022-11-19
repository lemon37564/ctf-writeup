from Crypto.Util.number import isPrime
import random

while True:
    k = 1
    while k.bit_length() < 1024:
        r = random.randint(2, 1024)
        if not isPrime(r):
            continue
        k *= r

    k += 1
    if k.bit_length() != 1024:
        continue
    if isPrime(k):
        break
    else:
        print("failed")

print(k)