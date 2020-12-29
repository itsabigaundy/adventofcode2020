import itertools
import numpy as np
import re
from collections import Counter

def part1(data):
    mem = Counter()
    mask = ''
    for task in data:
        if task[0] == 'mask':
            mask = task[1]
        else:
            idx, val = task[1:]
            bit = 1
            temp = 0
            for i in range(36):
                if mask[35 - i] == 'X':
                    temp += val & bit
                else:
                    temp += int(mask[35 - i]) * bit
                bit <<= 1
            mem[idx] = temp

    return sum(mem.values())

def part2(data):
    mem = Counter()
    mask = ''
    for task in data:
        if task[0] == 'mask':
            mask = task[1]
        else:
            idx, val = task[1:]
            bit = 1
            base = 0
            floats = []
            for i in range(36):
                if mask[35 - i] == 'X':
                    floats.append(bit)
                else:
                    base += (idx & bit) | (int(mask[35 - i]) * bit)
                bit <<= 1

            floats = np.array(floats, dtype=int)
            cartesian = np.array([list(item) for item in itertools.product([0, 1], repeat=len(floats))])
            addrs = np.array([np.sum(floats * group) + base for group in cartesian])
            for addr in addrs:
                mem[addr] = val
    
    return sum(mem.values())



if __name__ == "__main__":
    with open('day14.txt', 'r', newline='') as file:
        data = [[string if not string.isdigit() else int(string) for string in re.split(' = |\\[|\\] = ', s.rstrip())] for s in file.readlines()]
        print(part1(data))
        print(part2(data))