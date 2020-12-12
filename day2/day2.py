import re

def part1(data):
    return sum([1 if int(lo) <= pw.count(ch) <= int(hi) else 0 for lo, hi, ch, pw in data])

def part2(data):
    return sum([(pw[int(lo) - 1] == ch) ^ (pw[int(hi) - 1] == ch) for lo, hi, ch, pw in data])

if __name__ == "__main__":
    with open('day2.txt', 'r', newline='') as file:
        data = [re.split('-|: | ', s.rstrip()) for s in file.readlines()]
        print(part1(data))
        print(part2(data))