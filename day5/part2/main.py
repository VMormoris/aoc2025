from dataclasses import dataclass

@dataclass
class Range:
    low: int
    high: int

def readInput() -> tuple[list[Range], list[int]]:
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()

    ranges: list[Range] = []
    ids: list[int] = []
    flag: bool = False
    for line in lines:
        if line == '\n':
            flag = True
            continue

        if not flag:
            corners: list[str] = line.split('-')
            ranges.append(Range(int(corners[0]), int(corners[1])))
        else:
            ids.append(int(line))

    return (ranges, ids)

(ranges, ids) = readInput()

ranges = sorted(ranges, key=lambda ran: ran.low)
print(ranges)
newRanges: list[Range] = []
i = 0
while i < len(ranges):
    curr: Range = ranges[i]
    if i == len(ranges) - 1:
        newRanges.append(curr)
        break

    next: Range = ranges[i + 1]
    res = curr
    if curr.high >= next.low:
        while curr.high >= next.low:
            curr = Range(min(curr.low, next.low), max(curr.high, next.high))
            i += 1
            if i == len(ranges) - 1:
                break
            next = ranges[i + 1]
    i += 1
    newRanges.append(curr)

sum = 0
for ran in newRanges:
    print(ran)
    sum += (ran.high - ran.low) + 1
print(sum)

# Too low 327303529455702
# ??????? 332067203034711
# Too hig 332067203034729