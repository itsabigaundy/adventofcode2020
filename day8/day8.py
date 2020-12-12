from queue import Queue

lib = {
    'nop' : lambda i, acc, x: (i + 1, acc),
    'acc' : lambda i, acc, x: (i + 1, acc + x),
    'jmp' : lambda i, acc, x: (i + x, acc), 
}

def part1(data, i, acc, visited):
    while i not in visited and i < len(data):
        visited.add(i)
        code, x = data[i]
        i, acc = lib[code](i, acc, x)

    return i, acc, visited

def part2(data):
    q = Queue()
    q.put((0, 0, set(), True))
    while not q.empty():
        i, acc, visited, isMain = q.get()
        if isMain:
            while i < len(data):
                visited.add(i)
                code, x = data[i]
                if code == 'nop' or code == 'jmp':
                    other_i, other_acc = lib['jmp' if code == 'nop' else 'nop'](i, acc, x)
                    q.put((other_i, other_acc, visited, False))

                    i, acc = lib[code](i, acc, x)
                    q.put((i, acc, visited, True))
                    break
                else:
                    i, acc = lib[code](i, acc, x)
        else:
            i, acc, visited = part1(data, i, acc, visited)
            if i not in visited:
                return acc

    return None

if __name__ == "__main__":
    with open('day8.txt', 'r', newline='') as file:
        data = [s.split() for s in file.readlines()]
        data = [(code, int(val)) for code, val in data]
        print(part1(data, 0, 0, set())[1])
        print(part2(data))