import re

required = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
eclset = set(('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))
valid = {
    'byr' : lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
    'iyr' : lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
    'eyr' : lambda x: x.isdigit() and 2020 <= int(x) <= 2030,
    'hgt' : lambda x: len(x) > 2 and x[:-2].isdigit() and ((x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76)),
    'hcl' : lambda x: len(x) == 7 and x[0] == '#' and not re.search(r'[^a-f0-9]', x[1:]),
    'ecl' : lambda x: x in eclset,
    'pid' : lambda x: len(x) == 9 and x.isdigit(),
    'cid' : lambda x: True
}

def part1(data):
    return sum([1 if required.issubset(set(x)) else 0 for x in data])

def meetscritieria(x):
    if not required.issubset(set(x)):
        return 0
    fn = None
    for val in x:
        if val in required or val == 'cid':
            fn = valid[val]
        elif not fn(val):
            return 0
    return 1

def part2(data):
    return sum([meetscritieria(x) for x in data])

if __name__ == "__main__":
    with open('day4.txt', 'r', newline='') as file:
        data = [re.split(':| |\n', s) for s in re.split('\n\n', file.read())]
        print(part1(data))
        print(part2(data))