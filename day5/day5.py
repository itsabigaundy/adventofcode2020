def binarysearch(seq, lo_char):
    k = len(seq)
    n = 2 ** k
    lo = 0
    hi = n - 1
    for i in range(k):
        mid = (lo + hi) // 2
        if seq[i] == lo_char:
            hi = mid
        else:
            lo = mid + 1
    return lo

def part1(data):
    return max([binarysearch(x[:7], 'F') * 8 + binarysearch(x[7:], 'L') for x in data])

def part2(data):
    ids = sorted([binarysearch(x[:7], 'F') * 8 + binarysearch(x[7:], 'L') for x in data])
    for i in range(len(ids) - 1):
        if ids[i] + 1 != ids[i + 1]:
            return ids[i] + 1

if __name__ == "__main__":
    with open('day5.txt', 'r', newline='') as file:
        data = [s.rstrip() for s in file.readlines()]
        print(part1(data))
        print(part2(data))