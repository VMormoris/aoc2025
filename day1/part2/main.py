with open('input.txt', 'r') as file:
    lines: list[str] = file.readlines()

start: int = 50
count: int = 0
for line in lines:
    if (line == ''):
        continue
    diff: int = -int(line[1:]) if line[0] == 'L' else int(line[1:])
    
    # print('[', start, '] (', line[:-1], ') => [', sep='', end='')

    counter: int = -1 if (start == 0 and diff < 0) else 0

    start += diff
    while (start <= 0):
        counter += 1
        if (start != 0):
            start += 100
        else:
            break
    
    while (start > 99):
        start -= 100
        counter += 1

    count += counter

    # print(start, ']: ', counter, sep='')
    


print('\nResult:', count)

# 1180 (Previous test) - Too low obviously 
# 6911 too high
# 6892 correct