#include <cinttypes>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

#define SIZE 432

int result[SIZE] = {
    1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0,
    1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0,
    1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1,
    0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1,
    0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0,
    1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1,
    1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1,
    1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1,
    0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0,
    0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1,
};

class LFSR {
   public:
    uint64_t state, tap, size;
    LFSR(uint64_t state, uint64_t tap, uint64_t size) {
        this->state = state;
        this->tap = tap;
        this->size = size;
    }

    int getbit() {
        uint64_t b = __builtin_popcountl(this->state & this->tap) & 1;
        int bit = this->state & 1;
        this->state >>= 1;
        this->state |= b << (this->size - 1);
        return bit;
    }
};

double cal_cor(int a[], int b[]) {
    int count = 0;
    const int total = 200;
    for (int i = 0; i < total; i++) {
        if (a[i] == b[i])
            count++;
    }
    return (double)count / (double)total;
}

std::vector<uint64_t> get_state(uint64_t tap, uint64_t size) {
    int output[SIZE];
    std::vector<uint64_t> states;
    for (uint64_t state = 0; state < ((uint64_t)1 << size); state++) {
        LFSR lfsr = LFSR(state, tap, size);
        for (int i = 0; i < SIZE; i++) {
            output[i] = lfsr.getbit();
        }

        double accuracy = cal_cor(&output[SIZE - 200], &result[SIZE - 200]);
        if (accuracy > 0.7) {
            states.push_back(state);
        }
    }
    return states;
}

int main() {
    int output[SIZE] = {0};
    std::vector<std::vector<uint64_t>> states;
    uint64_t size[3] = {27, 23, 25};
    uint64_t tap[3] = {
        (1 << 26) | (1 << 16) | (1 << 13) | 1,
        (1 << 22) | (1 << 7) | (1 << 5) | 1,
        (1 << 24) | (1 << 19) | (1 << 17) | 1,
    };

    for (int i = 1; i < 3; i++) {
        states.push_back(get_state(tap[i], size[i]));
    }
    for (uint64_t state1 : states[0]) {
        for (uint64_t state2 : states[1]) {
            for (uint64_t state0 = 0; state0 < ((uint64_t)1 << size[0]);
                 state0++) {
                LFSR lfsr0 = LFSR(state0, tap[0], size[0]);
                LFSR lfsr1 = LFSR(state1, tap[1], size[1]);
                LFSR lfsr2 = LFSR(state2, tap[2], size[2]);
                int x0, x1, x2;
                for (int i = 0; i < SIZE; i++) {
                    x0 = lfsr0.getbit();
                    x1 = lfsr1.getbit();
                    x2 = lfsr2.getbit();
                    output[i] = x0 ? x1 : x2;
                }
                double accuracy =
                    cal_cor(&output[SIZE - 200], &result[SIZE - 200]);
                if (accuracy >= 0.99) {
                    goto answer;
                }
            }
        }
    }

answer:
    std::vector<uint8_t> flag_bit(SIZE - 200);
    for (int i = 0; i < flag_bit.size(); i++) {
        flag_bit[i] = output[i] ^ result[i];
    }
    std::string flag_str;
    for (int i = 0; i < flag_bit.size(); i += 8) {
        int value = 0;
        for (int t = 0; t < 8; t++) {
            value += flag_bit[i + t] << (8 - 1 - t);
        }
        flag_str += char(value);
    }
    std::cout << flag_str << std::endl;
}