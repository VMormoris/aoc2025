from dataclasses import dataclass

@dataclass
class Vec2:
    x: int
    y: int    

with open('input.txt', 'r') as file:
    lines: list[str] = file.readlines()
    lines = list(map(lambda line: line[:-1] if line[-1] == '\n' else line, lines)) 

gridSize: Vec2 = Vec2(len(lines[0]), len(lines))

def is_valid(tile: Vec2):
    return tile.x >= 0 and tile.y >= 0 and\
        tile.x < gridSize.x and tile.y < gridSize.y

def find_adjacent(tile: Vec2):
    up: Vec2 = Vec2(tile.x, tile.y - 1)
    upRight: Vec2 = Vec2(tile.x + 1, tile.y -1)
    right: Vec2 = Vec2(tile.x + 1, tile.y)
    bottomRight: Vec2 = Vec2(tile.x + 1, tile.y + 1)
    bottom: Vec2 = Vec2(tile.x, tile.y + 1)
    bottomLeft: Vec2 = Vec2(tile.x - 1, tile.y + 1)
    left: Vec2 = Vec2(tile.x - 1, tile.y)
    upLeft: Vec2 = Vec2(tile.x - 1, tile.y - 1)

    adjacent: list[Vec2] = []
    if is_valid(up):
        adjacent.append(up)
    if is_valid(upRight):
        adjacent.append(upRight)
    if is_valid(right):
        adjacent.append(right)
    if is_valid(bottomRight):
        adjacent.append(bottomRight)
    if is_valid(bottom):
        adjacent.append(bottom)
    if is_valid(bottomLeft):
        adjacent.append(bottomLeft)
    if is_valid(left):
        adjacent.append(left)
    if is_valid(upLeft):
        adjacent.append(upLeft)

    return adjacent

sum = 0
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        if lines[y][x] != '@':
            continue
        adjacents: list[Vec2] = find_adjacent(Vec2(x, y))
        rolls: int = 0
        for tile in adjacents:
            if lines[tile.y][tile.x] == '@':
                rolls += 1
        
        if rolls < 4:
            sum += 1

print(sum)