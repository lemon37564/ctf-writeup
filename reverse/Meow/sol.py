data = [0x24, 0x1d, 0x1b, 0x31, 0x21, 0x0b, 0x4f, 0x0f, 0xe8, 0x50,
        0x37, 0x5b, 0x08, 0x40, 0x4a, 0x08, 0x1d, 0x11, 0x4a, 0xb8,
        0x11, 0x67, 0x3f, 0x67, 0x38, 0x14, 0x3f, 0x19, 0x0b, 0x54,
        0xb4, 0x09, 0x63, 0x12, 0x68, 0x2a, 0x45, 0x53, 0x0e, 0x01, 0x00]

key = [0x62, 0x57, 0x56, 0x76, 0x64, 0x77,
       0x3D, 0x3D, 0x87, 0x63, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]

for i in range(39):
    data[i] = data[i] - 2 * (i % 3)
    if data[i] < 0:
        data[i] += 0xff
    data[i] ^= key[i % 0xb]

flag = [chr(i) for i in data]
print("".join(flag))
