import pwn
from Crypto.Util.number import long_to_bytes

p = pwn.remote("edu-ctf.zoolab.org", "10102")

n = int(p.recvline().strip())
e = int(p.recvline().strip())
enc = int(p.recvline().strip())

test = ""

print(n)
print(e)
print(enc)

while enc > 0:
    # print(str(enc))
    p.sendline(bytes(str(enc), "ascii"))
    test = str(p.recvline().strip(), encoding="ascii") + test
    enc //= 3
    # print(test)

print(test)