import numpy as np
from functools import reduce

def part1(data):
    data = [int(x) for x in data if x.isdigit()]
    target = data[0]
    remainders = [x - target % x for x in data[1:]]
    best = min(remainders)
    return data[1:][remainders.index(best)] * best

def part2(data):
    constraints = []
    offset = 1
    for x in data[1:]:
        if x.isdigit():
            constraints.append([int(x), offset])
            offset = 1
        else:
            offset += 1
    constraints = np.array(constraints)
    constraints[0, 1] = 0
    n = len(constraints)

    x = constraints[:, 0]
    y = np.cumsum(constraints[:, 1])

    ret = 0
    step = 1

    for i in range(1, n):
        step *= x[i - 1]
        while (ret + y[i]) % x[i] != 0:
            ret += step

    return ret

def gcd(array):
    return reduce(gcdBase, array)

def gcdBase(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


if __name__ == "__main__":
    with open('day13.txt', 'r', newline='') as file:
        data = [file.readline().rstrip()]
        data.extend(file.readline().rstrip().split(','))
        print(part1(data))
        print(part2(data))