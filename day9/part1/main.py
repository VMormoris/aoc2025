from dataclasses import dataclass

@dataclass
class Vec2:
    x: int
    y: int

def parseInput() -> list[Vec2]:    
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()

    vectors: list[Vec2] = []
    for line in lines:
        axis: list[str] = line.split(',')
        vectors.append(Vec2(int(axis[0]), int(axis[1])))
    return vectors

def debug_print(lines: list[str]) -> None:
    for line in lines:
        print(line)

def area(one: Vec2, two: Vec2) -> int:
    diff: Vec2 = Vec2(abs(one.x-two.x) + 1, abs(one.y - two.y) + 1)
    return diff.x * diff.y

tiles: list[Vec2] = parseInput()
combinations: list[tuple[Vec2, Vec2, int]] = []

for i in range(0, len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        one: Vec2 = tiles[i]
        two: Vec2 = tiles[j]
        t: tuple[Vec2, Vec2, int] = (one, two, area(one, two))
        combinations.append(t)

res = max(combinations, key= lambda candidate: candidate[2])
print(res[2])

# 4764078684 Correct