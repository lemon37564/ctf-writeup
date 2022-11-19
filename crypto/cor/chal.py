import random

from secret import FLAG

class LFSR:
    def __init__(self, tap, state):
        self._tap = tap
        self._state = state

    def getbit(self):
        f = sum([self._state[i] for i in self._tap]) & 1
        x = self._state[0]
        self._state = self._state[1:] + [f]
        return x

class triLFSR:
    def __init__(self, lfsr1, lfsr2, lfsr3):
        self.lfsr1 = lfsr1
        self.lfsr2 = lfsr2
        self.lfsr3 = lfsr3

    def getbit(self):
        x1 = self.lfsr1.getbit()
        x2 = self.lfsr2.getbit()
        x3 = self.lfsr3.getbit()
        return x2 if x1 else x3

lfsr1 = LFSR([0, 13, 16, 26], [random.randrange(2) for _ in range(27)])
lfsr2 = LFSR([0, 5, 7, 22], [random.randrange(2) for _ in range(23)])
lfsr3 = LFSR([0, 17, 19, 24], [random.randrange(2) for _ in range(25)])
cipher = triLFSR(lfsr1, lfsr2, lfsr3)

flag = map(int, ''.join(["{:08b}".format(c) for c in FLAG]))

output = []

for b in flag:
    output.append(cipher.getbit() ^ b)

for _ in range(200):
    output.append(cipher.getbit())

print(output)