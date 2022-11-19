from Crypto.Util.number import long_to_bytes

long_arr = [0x8D909984B8BEBAB3, 0x8D9A929E98D18B92,
            0xD0888BD19290D29C, 0x8C9DC08F978FBDD1,
            0xD9C7C7CCCDCB92C2, 0xC8CFC7CEC2BE8D91,
            0xFFFFFFFFFFFFCF82]

flag = b""
for rax in long_arr:
    # xchg al, ah
    al = rax & 0xFF   # extract al (7-0 bit)
    ah = (rax & 0xFF00) >> 8  # extract ah (15-8 bit)

    rax &= 0xFFFFFFFFFFFF0000  # clear al and ah

    al, ah = ah, al  # xchg
    rax |= al  # set al
    rax |= (ah << 8)  # set ah

    # neg rax
    rax = rax ^ 0xFFFFFFFFFFFFFFFF

    flag += long_to_bytes(rax)[::-1]  # little endian

print(flag)
