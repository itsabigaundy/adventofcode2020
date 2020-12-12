import re
from collections import defaultdict
from queue import Queue

def part1(data):
    tree = defaultdict(list)
    for rule in data:
        for bag in rule[1:]:
            if bag == 'no other':
                continue
            tree[bag[2:]].append((rule[0], int(bag[0])))

    visited = set()
    q = Queue()
    q.put('shiny gold')
    while not q.empty():
        node = q.get()
        for bag, _ in tree[node]:
            if bag in visited:
                continue
            visited.add(bag)
            q.put(bag)

    return len(visited)

def part2(data):
    tree = defaultdict(list)
    for rule in data:
        tree[rule[0]].extend([(bag[2:], int(bag[0])) for bag in rule[1:] if bag != 'no other'])

    total = 0
    q = Queue()
    q.put(('shiny gold', 1))
    while not q.empty():
        parent, scale = q.get()
        for child, count in tree[parent]:
            subtotal = count * scale
            total += subtotal
            q.put((child, subtotal))

    return total

if __name__ == "__main__":
    with open('day7.txt', 'r', newline='') as file:
        data = [re.split(' bags contain | bags, | bag, | bag.| bags.', s.rstrip())[:-1] for s in file.readlines()]
        print(part1(data))
        print(part2(data))