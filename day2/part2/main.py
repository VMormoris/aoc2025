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

def tokenize(string: str, size: int) -> list[str]:
    tokens: list[str] = []
    for i in range(0, len(string), size):
        tokens.append(string[i:i+size])
    return tokens

ranges: list[Range] = readInput()

sum: int = 0
for r in ranges:
    for i in range(r.low, r.high + 1):
        num: str = str(i)

        mid: int = int(len(num) / 2)
        for j in range(1, mid + 1):
            query: str = num[:j]
            tokens: list[str] = tokenize(num[j:], len(query))
            if all(token == query for token in tokens):
                print ("With query: '", query, "' and tokens: ", tokens, " from num: '", num,  "' " , sep='')
                sum += int(num)
                break
    
print ('Result:', sum)
