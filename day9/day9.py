import numpy as np

def part1(data):
    for i in range(25, len(data)):
        if not np.any(np.add.outer(data[i - 25:i], data[i - 25:i]) == data[i]):
            return i
    return None

def part2(data):
    idx = part1(data)
    prefixsum = np.cumsum(data[:idx])
    outer = np.subtract.outer(prefixsum, prefixsum)
    loc = np.argwhere(outer == data[idx])[0]
    window = data[min(loc) + 1:max(loc)]
    return min(window) + max(window)

if __name__ == "__main__":
    data = np.genfromtxt('day9.txt', dtype=int)
    print(data[part1(data)])
    print(part2(data))