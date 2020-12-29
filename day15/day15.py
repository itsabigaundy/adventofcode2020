from collections import deque, defaultdict

def part1(data):
    record = defaultdict(lambda : deque(maxlen=2))
    for i, x in enumerate(data):
        record[x].append(i)

    x = data[-1]
    for i in range(len(data), 30000000):
        if len(record[x]) == 1:
            x = 0
        else:
            x = record[x][1] - record[x][0]
        record[x].append(i)
    return x

if __name__ == "__main__":
    data = [2, 15, 0, 9, 1, 20]
    print(part1(data))