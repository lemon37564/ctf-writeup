FLAG = b"12345abcde"

flag = list(map(int, ''.join(["{:08b}".format(c) for c in FLAG])))

res = ""
for i in range(0, len(flag), 8):
    tmp = 0
    for j in range(8):
        tmp += flag[i + j] << (8-1-j)
    res += chr(tmp)

print(res)