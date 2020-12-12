import re
from functools import reduce

def part1(data):
    return sum(len(set(''.join(x))) for x in data)

def part2(data):
    return sum(len(reduce(lambda a, b: a.intersection(b), [set(word) for word in x])) for x in data)

if __name__ == "__main__":
    with open('day6.txt', 'r', newline='') as file:
        data = [s.split() for s in re.split('\n\n', file.read())]
        print(part1(data))
        print(part2(data))