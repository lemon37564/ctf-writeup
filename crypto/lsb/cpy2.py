import pwn
from Crypto.Util.number import inverse, long_to_bytes

r = pwn.remote("edu-ctf.zoolab.org", "10102")
n = int(r.recvline().strip().decode())
e = int(r.recvline().strip().decode())
enc = int(r.recvline().strip().decode())

prev = 0 # previous sum
pt = 0 # plain text
xi = 0 # ith bit
while True:
    inv = inverse(3, n)
    c1 = (enc * pow(inv, e*xi, n)) % n
    r.sendline(str(c1).encode())
    lsb = int(r.recvline().strip().decode())
    curr = (lsb - (prev*inv) % n) % 3
    prev = prev*inv + curr
    pt = pow(3, xi)*curr + pt
    
    # break when flag was found
    if b"FLAG" in long_to_bytes(pt):
        break
    xi += 1

print(long_to_bytes(pt))
