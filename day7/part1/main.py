from dataclasses import dataclass

@dataclass
class Vec2:
    x: int
    y: int

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vec2):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash('' + str(self.x) + ', ' + str(self.y))

def can_move_down(point: Vec2, size: Vec2) -> bool:
    return point.y + 1 < size.y

def can_move_left(point: Vec2, size: Vec2) -> bool:
    return point.x -1 >= 0

def can_move_right(point: Vec2, size: Vec2) -> bool:
    return point.x + 1 < size.y

def down(point: Vec2) -> Vec2:
    return Vec2(point.x, point.y + 1)

def left(point: Vec2) -> Vec2:
    return Vec2(point.x - 1, point.y)

def right(point: Vec2) -> Vec2:
    return Vec2(point.x + 1, point.y)

def up(point: Vec2) -> Vec2:
    return Vec2(point.x, point.y - 1)

def count(lines: list[str]) -> int:
    sum = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            char = lines[y][x]
            if char == '^':
                checkPoint = up(Vec2(x, y))
                if lines[checkPoint.y][checkPoint.x] == '|':
                    sum += 1

    return sum

def debug_print(lines: list[str]) -> None:
    for line in lines:
        print(line)
    print()

def replace(lines: list[str], point: Vec2) -> None:
    line: str = lines[point.y]
    lines[point.y] = line[0:point.x] + '|' + line[point.x+1:]

with open('input.txt', 'r') as file:
    lines: list[str] = file.readlines()
    for i in range(0, len(lines)):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        
startIdx: int = lines[0].index('S')
start: Vec2 = Vec2(startIdx, 0)

size: Vec2 = Vec2(len(lines[0]), len(lines))

beams: list[Vec2] = [down(start)]
debug_print(lines)
while (len(beams) > 0):
    new_beams: list[Vec2] = []
    for beam in beams:
        val: str = lines[beam.y][beam.x]
        if val == '.':
            replace(lines, beam)
            if can_move_down(beam, size):
                new_beams.append(down(beam))
        elif val == '^':
            if can_move_left(beam, size):
                new_beams.append(left(beam))
            if can_move_right(beam, size):
                new_beams.append(right(beam))
    beams = set(new_beams)
debug_print(lines)
print(count(lines))