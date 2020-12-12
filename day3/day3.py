import numpy as np

def part1(data):
    n = len(data)
    m = len(data[0])

    return sum([1 if data[i][(3 * i) % m] == '#' else 0 for i in range(1, n)])

def part2(data):
    n = len(data)
    m = len(data[0])

    slopes = {
        (1, 1) : 0,
        (3, 1) : 0,
        (5, 1) : 0,
        (7, 1) : 0,
        (1, 2) : 0
    }

    for i in range(1, n):
        for slope in slopes:
            right, down = slope
            if i % down == 0 and data[i][(right * i // down) % m] == '#':
                slopes[slope] += 1
    
    return np.prod(list(slopes.values()))

if __name__ == "__main__":
    with open('day3.txt', 'r', newline='') as file:
        data = [s.rstrip() for s in file.readlines()]
        print(part1(data))
        print(part2(data))