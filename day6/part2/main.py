from dataclasses import dataclass

@dataclass
class Problem:
    numbers: list[list[str]]
    operations: list[str]

def parseInput() -> Problem:
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()

    rawInputs: list[list[str]] = []
    for line in lines[:-1]:
        nums: list[str] = line.split(' ')
        
        accumulator: list[str] = []
        for num in nums:
            if num == '' or num == '\n':
                continue
            accumulator.append(str(int(num)))

        rawInputs.append(accumulator)
    
    colLengths: list[int] = []
    for x in range(0, len(rawInputs[0])):
        maxLen: int = 0
        for y in range(0, len(rawInputs)):
            length: int = len(rawInputs[y][x])
            if maxLen < length:
                maxLen = length

        colLengths.append(maxLen)

    interInputs: list[list[str]] = []
    for line in lines[:-1]:
        idx: int = 0
        accumulator: list[str] = []
        for colLength in colLengths:
            slice: str = line[idx:idx+colLength]
            idx += colLength + 1
            accumulator.append(slice)
        interInputs.append(accumulator)

    inputs: list[list[str]] = []
    for x in range(0, len(interInputs[0])):
        nums: list[str] = []
        for y in range(0, len(interInputs)):
            nums.append(interInputs[y][x])
        inputs.append(nums)

    rawOperations: list[str] = lines[-1].split(' ')
    operations: list[str] = []
    for op in rawOperations:
        if op == '' or op == '\n':
            continue
        operations.append(op)
    
    return Problem(inputs, operations)


problem: Problem = parseInput()
sum = 0
for i in range(0, len(problem.operations)):
    operation: str = problem.operations[i]
    nums: list[str] = problem.numbers[i]
    digits: int = len(nums[0])

    accs: list[int] = []
    for j in range(0, digits):
        acc = ''
        for num in nums:
            acc += num[j]
        accs.append(int(acc))

    if operation == '*':
        base: int = 1
        for acc in accs:
            base *= acc
    else:
        base: int = 0
        for acc in accs:
            base += acc
    sum += base
    print(accs, operation, base)

print(sum)

