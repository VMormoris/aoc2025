from dataclasses import dataclass

@dataclass
class Vec2:
    x: int
    y: int

@dataclass
class StraightSection:
    start: Vec2
    end: Vec2

def doIntersect(A: Vec2, B: Vec2, C: Vec2, D: Vec2) -> bool:
    (x1, y1) = (A.x, A.y)
    (x2, y2) = (B.x, B.y)
    (x3, y3) = (C.x, C.y)
    (x4, y4) = (D.x, D.y)

    try:
        alpha = ((x4 - x3) * (y3 - y1) - (y4 - y3) * (x3 - x1)) /\
            ((x4 - x3) * (y2 - y1) - (y4 - y3) * (x2 - x1))
    except:
        return False
    
    beta = ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) /\
        ((x4 - x3) * (y2 - y1) - (y4 - y3) * (x2 - x1))
    
    if beta == 0:
        return False

    return 0 < alpha < 1 and 0 < beta < 1
    
def parseInput() -> list[Vec2]:    
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()

    vectors: list[Vec2] = []
    for line in lines:
        axis: list[str] = line.split(',')
        vectors.append(Vec2(int(axis[0]), int(axis[1])))
    return vectors

def area(one: Vec2, two: Vec2) -> int:
    diff: Vec2 = Vec2(abs(one.x-two.x) + 1, abs(one.y - two.y) + 1)
    return diff.x * diff.y

def sortRects(tiles: list[Vec2]) -> list[tuple[Vec2, Vec2, int]]:
    combinations: list[tuple[Vec2, Vec2, int]] = []

    for i in range(0, len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            one: Vec2 = tiles[i]
            two: Vec2 = tiles[j]
            t: tuple[Vec2, Vec2, int] = (one, two, area(one, two))
            combinations.append(t)

    return sorted(combinations, key= lambda candidate: candidate[2], reverse=True)

tiles: list[Vec2] = parseInput()
perimeter: list[StraightSection] = []
for i in range(-1, len(tiles) - 1):
    curr = tiles[i]
    next = tiles[i + 1]

    perimeter.append(StraightSection(curr, next))

top = [tile for tile in tiles if tile.y >= 50191]
bottom = [tile for tile in tiles if tile.y < 48573]

top_perimeter = [line for line in perimeter if line.start.y >= 50191 and line.end.y >= 50191]
bottom_perimeter = [line for line in perimeter if line.start.y < 48573 and line.end.y < 48573]
sortedRects = sortRects(top)
res: list[tuple[Vec2, Vec2, int]] = []
for rect in sortedRects:
    valid = True

    otherRect = (Vec2(rect[0].x, rect[1].y), Vec2(rect[1].x, rect[0].y))
    for section in top_perimeter:
        if section.start == rect[0] or section.end == rect[0] or\
            section.start == rect[1] or section.end == rect[1]:
            continue

        if section.start == otherRect[0] or section.end == otherRect[0] or\
            section.start == otherRect[1] or section.end == otherRect[1]:
            continue
        
        if doIntersect(rect[0], rect[1], section.start, section.end) or\
            doIntersect(otherRect[0], otherRect[1], section.start, section.end):
            valid = False
            break

    if valid:
        res.append(rect)

print(res[0])

sortedRects = sortRects(bottom)
res: list[tuple[Vec2, Vec2, int]] = []
for rect in sortedRects:
    valid = True

    otherRect = (Vec2(rect[0].x, rect[1].y), Vec2(rect[1].x, rect[0].y))
    for section in bottom_perimeter:
        if section.start == rect[0] or section.end == rect[0] or\
            section.start == rect[1] or section.end == rect[1]:
            continue

        if section.start == otherRect[0] or section.end == otherRect[0] or\
            section.start == otherRect[1] or section.end == otherRect[1]:
            continue
        
        if doIntersect(rect[0], rect[1], section.start, section.end) or\
            doIntersect(otherRect[0], otherRect[1], section.start, section.end):
            valid = False
            break

    if valid:
        res.append(rect)

print(res[0])

# for rect in sortedRects:


# print(findMax(top))
# print(findMax(bottom))

## Too high 3154250619
## Too high 3035483075
## Too high 2878637370

## Top solution 1652344888 correct!!! <3