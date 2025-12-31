from dataclasses import dataclass

@dataclass
class Range:
    low: int
    high: int

def rangeSpliter(range: str) -> Range:
    all: list[str] = range.split('-')
    return Range(int(all[0]), int(all[1]))

def readInput() -> list[Range]:
    with open('input.txt', 'r') as file:
        line: str = file.read()

    ranges: list[str] = line.split(',')
    return list(map(rangeSpliter, ranges))


ranges: list[Range] = readInput()

sum: int = 0
for r in ranges:
    for i in range(r.low, r.high + 1):
        num: str = str(i)
        if (len(num) % 2 == 1):
            continue

        midIndex: int = int(len(num) / 2)
        firstHalf: str = num[:midIndex]
        secondHalf: str = num[midIndex:]

        if (firstHalf == secondHalf):
            print(num)
            sum += i

print(sum)