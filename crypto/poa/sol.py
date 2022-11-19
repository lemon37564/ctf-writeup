import pwn

BLOCK_SIZE = 16

p = pwn.remote("edu-ctf.zoolab.org", "10101")

data = p.recvline().strip().decode("ascii")
data = bytearray.fromhex(data)
test = data.copy()

pos = 0
# 找0x80
for i in range(1, 16):
    count = 0
    test = data.copy()
    for j in range(256):
        test[-i-BLOCK_SIZE] = j

        p.sendline(bytes(test.hex(), encoding="ascii"))
        if p.recvline() == b"Well received :)\n":
            count += 1
    # 找到0x80位置
    if count == 1:
        pos = i
        break


print(f"0x80 found at {pos}")
ans = ""
last_byte = 0
test = data.copy()

# 最後一個block
for j in range(pos, 16):
    test[-j-BLOCK_SIZE] ^= 0x80
    for i in range(256):
        test[-j-1-BLOCK_SIZE] = i

        p.sendline(bytes(test.hex(), encoding="ascii"))
        if p.recvline() == b"Well received :)\n":
            last_byte = i
            ans += chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80)
            print("crack byte:", chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80))
            break


# 剩下的block (扣掉iv)
while len(data) > 32:
    data = data[:-BLOCK_SIZE]
    test = data.copy()

    # block的最後一個byte
    for i in range(256):
        test[-1-BLOCK_SIZE] = i
        p.sendline(bytes(test.hex(), encoding="ascii"))
        if p.recvline() == b"Well received :)\n":
            last_byte = i
            ans += chr(i ^ data[-1-BLOCK_SIZE] ^ 0x80)
            print("crack byte:", chr(i ^ data[-1-BLOCK_SIZE] ^ 0x80))
            break
    
    # block剩下的15個byte
    for j in range(1, 16):
        test[-j-BLOCK_SIZE] ^= 0x80
        for i in range(256):
            test[-j-1-BLOCK_SIZE] = i

            p.sendline(bytes(test.hex(), encoding="ascii"))
            if p.recvline() == b"Well received :)\n":
                last_byte = i
                ans += chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80)
                print("crack byte:", chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80))
                break


print(ans[::-1])
