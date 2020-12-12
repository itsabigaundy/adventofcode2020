import numpy as np

units = {
    'N' : np.array([0, 1]),
    'E' : np.array([1, 0]),
    'S' : np.array([0, -1]),
    'W' : np.array([-1, 0])
}

rotate = {
    'R' : {
        90 : lambda loc : np.flip(loc) * np.array([1, -1]),
        180 : lambda loc : -1 * loc,
        270 : lambda loc : np.flip(loc) * np.array([-1, 1])
    },
    'L' : {
        90 : lambda loc : np.flip(loc) * np.array([-1, 1]),
        180 : lambda loc : -1 * loc,
        270 : lambda loc : np.flip(loc) * np.array([1, -1])
    }
}

def part1(data):
    loc = np.zeros(2, dtype=int)
    face = np.array([1, 0], dtype=int)
    for i in range(len(data)):
        char = data[i][0]
        x = int(data[i][1:])
        if char == 'R' or char == 'L':
            face = rotate[char][x](face)
        elif char == 'F':
            loc += x * face
        else:
            loc += x * units[char]
    
    return np.sum(np.abs(loc))

def part2(data):
    loc = np.zeros(2, dtype=int)
    wpt = np.array([10, 1], dtype=int)
    for i in range(len(data)):
        char = data[i][0]
        x = int(data[i][1:])
        if char == 'R' or char == 'L':
            wpt = rotate[char][x](wpt)
        elif char == 'F':
            loc += x * wpt
        else:
            wpt += x * units[char]

    return np.sum(np.abs(loc))

if __name__ == "__main__":
    with open('day12.txt', 'r', newline='') as file:
        data = [s.rstrip() for s in file.readlines()]
        print(part1(data))
        print(part2(data))