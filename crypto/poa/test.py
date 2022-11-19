import chal

BLOCK_SIZE = 16

data = bytearray.fromhex(chal.data)
# data = data[:-2]
length = len(data)
test = data.copy()


ans = ""

last_byte = 0


for j in range(2, 16):
    test[-j-BLOCK_SIZE] ^= 0x80
    for i in range(256):
        test[-j-1-BLOCK_SIZE] = i

        res = chal.crack(test.hex())
        if res == "Well received :)":
            last_byte = i
            ans += chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80)
            # print("last byte:", chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80), "({})".format(last_byte))
            break

# print(ans[::-1])
data = data[:-BLOCK_SIZE]
print(len(list(data)))
test = data.copy()

for i in range(256):
    test[-1-BLOCK_SIZE] = i
    res = chal.crack(test.hex())
    if res == "Well received :)":
        last_byte = i
        ans += chr(i ^ data[-1-BLOCK_SIZE] ^ 0x80)
        print("last byte:", chr(i ^ data[-1-BLOCK_SIZE] ^ 0x80), i, data[-1-BLOCK_SIZE])
        break

for j in range(1, 16):
    test[-j-BLOCK_SIZE] ^= 0x80
    for i in range(256):
        test[-j-1-BLOCK_SIZE] = i

        res = chal.crack(test.hex())
        if res == "Well received :)":
            last_byte = i
            ans += chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80)
            # print("last byte:", chr(i ^ data[-j-1-BLOCK_SIZE] ^ 0x80), "({})".format(last_byte))
            break

print(ans[::-1])
