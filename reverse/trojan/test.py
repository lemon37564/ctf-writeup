with open("test", "r") as f:
    data = f.read()

# split data to bytes
data = [data[i:i+2] for i in range(0, len(data), 2)]

x = "0vCh8RrvqkrbxN9Q7Ydx"
x = [ord(i) for i in x]
x.append(0) # '\0' in C str

data = [int(i, base=16) for i in data]

for i, v in enumerate(data):
    data[i] = v ^ x[i%0x15]

with open("output", "wb") as f:
    f.write(bytes(data))
