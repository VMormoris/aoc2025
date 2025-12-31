with open('input.txt', 'r') as file:
    lines: list[str] = file.readlines()

start = 50
count = 0
for line in lines:
    if (line == ''):
        continue
    diff: int =  -int(line[1:]) if line[0] == 'L' else int(line[1:])
    
    start += diff
    while (start < 0):
        start += 100
    
    start = start % 100
    if start == 0:
        count += 1

print('Result:', count)