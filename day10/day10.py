import numpy as np
from collections import Counter
from queue import Queue

def part1(data):
    data = np.sort(data)
    data[1:] -= data[:-1]
    ctr = Counter(data)
    ctr[3] += 1
    return ctr[1] * ctr[3]

def part2(data):
    data = np.sort(data)
    graph = {x : data[(data > x) & (data <= x + 3)] for x in data}
    graph[0] = data[data <= 3]

    ctr = Counter({x : 1 for x in graph[0]})
    for x in data:
        for y in graph[x]:
            ctr[y] += ctr[x]
    return ctr[data[-1]]

if __name__ == "__main__":
    data = np.sort(np.genfromtxt('day10.txt', dtype=int))
    print(part1(data))
    print(part2(data))