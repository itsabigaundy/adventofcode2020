import re
import numpy as np

def updateRanges(ranges, newRange):
    converted = [int(x) for x in newRange.split('-')]
    new_lo, new_hi = converted
    endLoop = False
    for i in range(len(ranges)):
        lo, hi = ranges[i]
        if new_lo < lo and new_hi >= lo:
            ranges[i][0] = new_lo
            endLoop = True
        if new_hi > hi and new_lo <= hi:
            ranges[i][1] = new_hi
            endLoop = True
        if endLoop:
            return ranges

    ranges.append(converted)
    return ranges

def compareToRanges(ranges, array):
    return [int(x) for x in array if not any(lo <= int(x) <= hi for lo, hi in ranges)]

def part1(data):
    errs = []
    ranges = []
    section = ''
    for array in data:
        if len(array) == 3:
            ranges = updateRanges(ranges, array[1])
            ranges = updateRanges(ranges, array[2])
        elif len(array) == 1:
            section = array[0]
        elif section == 'nearby tickets':
            errs.extend(compareToRanges(ranges, array))
    return sum(errs)

def isValidTicket(ranges, array):
    return all(any(any(lo <= x <= hi for lo, hi in range_list) for range_list in ranges.values()) for x in array)

def part2(data):
    ranges = {}
    section = ''
    mine = []
    tickets = []
    for array in data:
        if len(array) == 3:
            ranges[array[0]] = [[int(x) for x in rnge.split('-')] for rnge in array[1:]] 
        elif len(array) == 1:
            section = array[0]
        elif section == 'nearby tickets':
            temp = [int(x) for x in array]
            if isValidTicket(ranges, temp):
                tickets.append(temp)
        elif section == 'your ticket':
            mine = [int(x) for x in array]

    tickets = np.array(tickets)
    sus = [set(ranges.keys()) for i in range(len(mine))]
    for i in range(len(sus)):
        for j in range(tickets.shape[0]):
            sus[i] = set(field for field in sus[i] if any(lo <= tickets[j, i] <= hi for lo, hi in ranges[field]))

    while not all(len(x) == 1 for x in sus):
        for i in range(len(sus)):
            if len(sus[i]) == 1:
                item = list(sus[i])[0]
                for fields in sus:
                    if len(fields) > 1:
                        fields.discard(item)

    sus = [fields.pop() for fields in sus]

    return np.prod([val for field, val in zip(sus, mine) if 'departure' in field])


if __name__ == "__main__":
    with open('day16.txt', 'r', newline='') as file:
        data = [[item for item in re.split(': |:| or |,', s.rstrip()) if item != ''] for s in file.readlines() if len(s) > 2]
        print(part1(data))
        print(part2(data))