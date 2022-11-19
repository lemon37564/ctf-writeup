import pwn
import decimal
from Crypto.Util.number import *


def lsbOracle(c):
    r.sendline(str(c))
    m = r.recvline().strip().decode()
    print("m: "+m)
    m = int(m)
    return m


def revealFlag(c, n):
    k = n.bit_length()  # 二进制长度数，这里是1024
    decimal.getcontext().prec = k  # 设定小数点精度
    low = decimal.Decimal(0)
    high = decimal.Decimal(n)
    for i in range(k):
        plaintext = (low + high) / 2
        state = lsbOracle(c)
        if not state:  # state = 0
            high = plaintext  # 0<high<n/2
        else:
            low = plaintext
        c = (c * pow(2, e, n)) % n
        print(i, state, int(high-low))
    return int(high)


if __name__ == '__main__':
    r = pwn.remote("edu-ctf.zoolab.org", "10102")
    n = r.recvline().strip().decode()
    e = int(r.recvline().strip().decode())
    c = r.recvline().strip().decode()
    print("c: "+c)
    c = int(c)
    print("n: "+n)
    n = int(n)
    res = revealFlag((c * pow(2, e, n)) % n, n)
    print(res)
    res_hex = hex(res)
    print(long_to_bytes(res))
