from dataclasses import dataclass

@dataclass
class Vec3:
    x: int
    y: int
    z: int

@dataclass
class Pair:
    first: Vec3
    second: Vec3
    distance: int

    def __init__(self, one: Vec3, two: Vec3):
        self.first = one
        self.second = two
        self.__squareDist()

    def __squareDist(self):
        dx: int = self.first.x - self.second.x
        dy: int = self.first.y - self.second.y
        dz: int = self.first.z - self.second.z
        
        self.distance = dx * dx + dy * dy + dz * dz
        
def parseInput() -> list[Vec3]:
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()

    vectors: list[Vec3] = []
    for line in lines:
        parts: list[str] = line.split(',')
        vectors.append(Vec3(int(parts[0]), int(parts[1]), int(parts[2])))
    
    return vectors

def debug_circuits(circuits: list[list[Vec3]]) -> None:
    for circuit in circuits:
        print(len(circuit), ': ', circuit, sep='')

def find_max(circuits: list[list[Vec3]]) -> tuple[int, int]:
    max = 0
    idx = 0

    for i in range(0, len(circuits)):
        circuit = circuits[i]
        if max < len(circuit):
            max = len(circuit)
            idx = i
    return (max, idx)

vectors: list[Vec3] = parseInput()

allPairs: list[Pair] = []
for i in range(0, len(vectors[:-1])):
    for j in range(i + 1, len(vectors)):
        allPairs.append(Pair(vectors[i], vectors[j]))

allPairs.sort(key=lambda pair: pair.distance)

circuits: list[list[Vec3]] = []
for vec in vectors:
    circuits.append([vec])

for pair in allPairs:
    fIdx = -1
    sIdx = -1

    for j in range(0, len(circuits)):
        circuit: list[Vec3] = circuits[j]
        if pair.first in circuit:
            fIdx = j
        if pair.second in circuit:
            sIdx = j

    if fIdx != sIdx:
        newCircuit = circuits[fIdx] + circuits[sIdx]
        circuits.pop(max(fIdx, sIdx))
        circuits.pop(min(fIdx, sIdx))
        circuits.append(newCircuit)

    if len(circuits) == 1:
        print(pair.first.x * pair.second.x)
        break

# 9259958565 correct