import numpy as np
import itertools as it

data = np.genfromtxt('day1.csv')

def part1():
    lower = data[data < 1010]
    mid = data[data == 1010]
    upper = data[data > 1010]
    if len(mid) >= 2:
        return 1010 * 1010
    adds = np.add.outer(lower, upper)
    loc = np.argwhere(adds == 2020)[0]
    return lower[loc[0]] * upper[loc[1]]

def part2():
    combos = it.combinations(range(len(data)), 3)
    for combo in combos:
        if np.sum(data[list(combo)]) == 2020:
            return np.prod(data[list(combo)])
    return -1

if __name__ == "__main__":
    print(part1())
    print(part2())