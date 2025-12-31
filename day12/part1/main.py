from dataclasses import dataclass

@dataclass
class Shape:
    id: int
    form: list[str]
    space: int = 0

    def update(self) -> None:
        self.space = 0
        for string in self.form:
            for char in string:
                if char == '#':
                    self.space += 1

def rotate(shape: Shape) -> Shape:
    rotated_shape: Shape = Shape(shape.id, []) 
    for x in range(0, 3):
        col: str = ''
        for y in range(2, -1, -1):
            col += shape.form[y][x]
        rotated_shape.form.append(col)
    return rotated_shape

def all_rotations(shape: Shape) -> list[Shape]:
    shapes: list[Shape] = [shape]
    for _ in range(0, 3):
        curr: Shape = shapes[-1]
        shapes.append(rotate(curr))
    return shapes

def debug_print_shape(shape: Shape) -> None:
    for line in shape.form:
        print(line)
    print()

@dataclass
class Vec2:
    x: int = 0
    y: int = 0

@dataclass
class Query:
    size: Vec2
    indexes: list[int]

@dataclass
class Board:
    size: Vec2
    free_space: int = 0
    buffer: str = ''
    def __init__(self, size: Vec2):
        for _ in range(0, size.y):
            for _ in range(0, size.x):
                self.buffer += '.'
        self.size = size
        self.free_space = size.x * size.y

    def debug_print(self):
        for y in range(0, self.size.y):
            for x in range(0, self.size.x):
                print(self.buffer[y*x+x], sep='', end='')
            print()

def apply(board: Board, shape: Shape) -> list[Board]:
    pass

def parseInput() -> tuple[list[Shape], list[Query]]:
    with open('input.txt') as file:
        lines = file.readlines()
    
    for i in range(0, len(lines)):
        line = lines[i]
        if line[-1] == '\n':
            lines[i] = line[:-1]

    shapes: list[Shape] = []
    shape: Shape = None
    for i in range(1, 31):
        line: str = lines[i]
        if i % 5 == 0:
            shape.update()
            shapes.append(shape)
        elif i % 5 == 1:  
            shape = Shape(int(line.split(':')[0]), [])
        else:
            shape.form.append(line)

    queries: list[Query] = []
    for i in range(31, len(lines)):
        line = lines[i]
        parts: list[str] = line.split(': ')
        
        query: Query = Query(Vec2(), [])
        for counter in parts[1].split(' '):
            query.indexes.append(int(counter))

        axis = parts[0].split('x')
        query.size = Vec2(int(axis[0]), int(axis[1]))
        queries.append(query)

    return (shapes, queries)


(shapes, queries) = parseInput()

countNots = 0
countMaybes = 0
for query in queries:
    wanted_area: int = query.size.x * query.size.y
    best_area: int = 0
    for idx in range(0, len(query.indexes)):
        count: int = query.indexes[idx]
        shape: Shape = shapes[idx]
        best_area += shape.space * count
    
    if wanted_area >= best_area:
        countMaybes += 1
    else:
        countNots += 1

print('Nots:', countNots, 'Maybes:', countMaybes)
