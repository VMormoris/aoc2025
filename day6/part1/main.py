from dataclasses import dataclass

@dataclass
class Problem:
    numbers: list[list[int]]
    operations: list[str]

    def __init__(self, size: int):
        self.numbers = []
        for _ in range(0, size):
            self.numbers.append([])
        self.operations = []

def parseInput() -> list[list[str]]:
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()

    inputs: list[list[str]] = []
    for line in lines:
        nums: list[str] = line.split(' ')
        
        accumulator: list[str] = []
        for num in nums:
            if num == '' or num == '\n':
                continue
            accumulator.append(num)

        inputs.append(accumulator)
    return inputs


inputs: list[list[str]] = parseInput()
problem: Problem = Problem(len(inputs[0]))
problem.operations = inputs[-1]
for i in range(0 , len(inputs) - 1):
    nums: list[str] = inputs[i]
    for j in range(0, len(nums)):

        problem.numbers[j].append(int(nums[j]))

sum: int = 0
for i in range(0, len(problem.numbers)):
    nums: list[int] = problem.numbers[i]
    op: str = problem.operations[i]

    if op == '*':
        num = 1
        for n in nums:
            num *= n
    else:
        num = 0
        for n in nums:
            num += n
    print(num)
    sum += num

print(sum)
    