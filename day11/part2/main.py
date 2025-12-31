from dataclasses import dataclass, field

@dataclass
class Node:
    source: str
    targets: list[str] = field(default_factory=list)

def parse_input() -> list[Node]: 
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()
    
    nodes: list[Node] = []
    for line in lines:
        parts: list[str] = line.replace('\n','').split(': ')
        nodes.append(Node(parts[0], parts[1].split(' ')))
    
    return nodes

def find_by_source(nodes: list[Node], source: str = 'svr') -> Node:
    for node in nodes:
        if node.source == source:
            return node
        
    return Node(source)

def find_paths_between(
    node: Node,
    target_id: str,
    registry: list[Node],
    limiters: list[str] = [],
    memory: dict = {}    
) -> int:
    paths = 0
    memory[node.source] = 0
    for target in node.targets:
        if target == target_id:
            paths += 1
            continue
        if target in limiters:
            continue
        
        if target in memory.keys():
            paths += memory[target]
            continue
        next = find_by_source(registry, target)
        paths += find_paths_between(next, target_id, registry, limiters, memory)

    memory[node.source] = paths
    return paths


registry: list[Node] = parse_input()
svr: Node = find_by_source(registry)
fft: Node = find_by_source(registry, 'fft')
dac: Node = find_by_source(registry, 'dac')

exits_from_dac = find_paths_between(dac, 'out', registry, {})
print('Exits from dac:', exits_from_dac)
svr_to_fft = find_paths_between(svr, 'fft', registry, ['dyb', 'jeu', 'wwr'], {})
print('svr to fft:', svr_to_fft)
fft_to_dac = find_paths_between(fft, 'dac', registry, ['you', 'dpv', 'svi'], {})
print('fft to dac:', fft_to_dac)
print(exits_from_dac * svr_to_fft * fft_to_dac)

# 0 wrong
# 4 wrong
# 23 wrong
# 1206 wrong

# 5050222270334986 Wrong
# 7620354186017232 Wrong
# 145988202564646979 - Not enter probably wrong
# 393474305030400




#                               370500293582760
# Solution for day11.txt Input: 370500293582760
#                                   
# Useful input: https://www.reddit.com/r/adventofcode/comments/1pnsbql/2025_day_11_part_2_pretty_sure_my_approach_is/