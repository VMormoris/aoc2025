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

class Beam:
    pos: Vec2 = Vec2(0, 0)
    size: Vec2 = Vec2(0, 0)
    power: int = 1

    def __init__(self):
        return

    def __init__(self, lines: list[str]):
        self.size = Vec2(len(lines[0]), len(lines))
        for y in range(0, len(lines)):
            for x in range(0, len(lines[y])):
                if lines[y][x] == 'S':
                    self.pos = Vec2(x, y)
                    break

    def can_move_down(self) -> bool:
        return self.pos.y + 1 < self.size.y

    def can_move_left(self) -> bool:
        return self.pos.x -1 >= 0

    def can_move_right(self) -> bool:
        return self.pos.x + 1 < self.size.x

    def down(self):
        newBeam = Beam([''])
        newBeam.pos = Vec2(self.pos.x, self.pos.y + 1)
        newBeam.size = self.size
        newBeam.power = self.power
        return newBeam

    def left(self):
        newBeam = Beam([''])
        newBeam.pos = Vec2(self.pos.x - 1, self.pos.y)
        newBeam.size = self.size
        newBeam.power = self.power
        return newBeam

    def right(self):
        newBeam = Beam([''])
        newBeam.pos = Vec2(self.pos.x + 1, self.pos.y)
        newBeam.size = self.size
        newBeam.power = self.power
        return newBeam

    def powerUp(self, power: int):
        self.power += power

def readInput() -> list[str]:
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()
        for i in range(0, len(lines)):
            if lines[i][-1] == '\n':
                lines[i] = lines[i][:-1]
    return lines

def replace(lines: list[str], point: Vec2, char: str = '|') -> None:
    line: str = lines[point.y]
    lines[point.y] = line[0:point.x] + char + line[point.x+1:]

def debug_print(lines: list[str]) -> None:
    for line in lines:
        print(line)
    print(flush=True)

def print_weights(weight_map: list[list[int]]) -> None:
    for weights in weight_map:
        print(weights)

board: list[str] = readInput()
beams: list[Beam] = [Beam(board).down()]

weight_map: list[list[int]] = []
for row in board:
    weights: list[int] = []
    for col in row:
        weights.append(0)
    weight_map.append(weights)

while len(beams) > 0:
    newBeams: list[Beam] = []
    for beam in  beams:
        val: str = board[beam.pos.y][beam.pos.x]
        if val == '.' or val == '|':
            replace(board, beam.pos)
            if beam.can_move_down():
                newBeams.append(beam.down())
        elif val == '^':
            if beam.can_move_left():
                newBeams.append(beam.left())
            if beam.can_move_right():
                newBeams.append(beam.right())

    beams = []
    for query in newBeams:
        found: bool = False
        for beam in beams:
            if query.pos == beam.pos:
                found = True
                beam.powerUp(query.power)
                break
        if not found:
            beams.append(query)
    
    for beam in beams:
        weight_map[beam.pos.y][beam.pos.x] += beam.power
    debug_print(board)
    print_weights(weight_map)

sum: int = 0
for weight in weight_map[-1]:
    sum += weight

print(sum)