from dataclasses import dataclass

@dataclass
class Node:
    source: str
    targets: list[str]

def parse_input() -> list[Node]: 
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()
    
    nodes: list[Node] = []
    for line in lines:
        parts: list[str] = line.replace('\n','').split(': ')
        nodes.append(Node(parts[0], parts[1].split(' ')))
    
    return nodes

def find_by_source(nodes: list[Node], source: str = 'you') -> Node:
    for node in nodes:
        if node.source == source:
            return node
        
    return None

def find_exits(node: Node, registry: list[Node]) -> int:
    exits: int = 0
    for target in node.targets:
        if target == 'out':
            exits += 1
            continue
        next = find_by_source(registry, target)
        exits += find_exits(next, registry)
    return exits

registry: list[Node] = parse_input()
start: Node = find_by_source(registry)
print(find_exits(start, registry))