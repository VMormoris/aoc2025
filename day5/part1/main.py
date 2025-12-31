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

print("Ranges:", ranges)
print("ids:", ids)


sum: int = 0
for id in ids:
    for ran in ranges:
        if id >= ran.low and id <= ran.high:
            sum += 1
            break

print('Result:', sum)

