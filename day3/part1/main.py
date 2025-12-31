with open('input.txt', 'r') as file:
    batteryPacks: list[str] = file.readlines()
    batteryPacks = list(map(lambda pack: str(int(pack)), batteryPacks))

sum: int = 0
for pack in batteryPacks:
    maxValue: int = max(pack[:-1])
    maxIdx: int = pack.index(maxValue)
    secMaxValue = max(pack[maxIdx+1:])

    num: int = int(str(maxValue) + str(secMaxValue))
    print(num)
    sum += num

print(sum)