with open('input.txt', 'r') as file:
    batteryPacks: list[str] = file.readlines()
    batteryPacks = list(map(lambda pack: str(int(pack)), batteryPacks))

sum: int = 0
for pack in batteryPacks:
    
    previousIdx: int = 0
    accumulator: str = ''

    for i in range(11, -1, -1):
        workingSlice: int = pack[previousIdx:-i] if i != 0 else pack[previousIdx:]

        maxValue: int = max(workingSlice)
        previousIdx += workingSlice.index(maxValue) + 1

        accumulator += str(maxValue)

    num: int = int(accumulator)
    print(num)
    sum += num


print(sum)