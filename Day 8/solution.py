import re
import math
from typing import Dict, Tuple, List

START = 'AAA'
END = 'ZZZ'

def parse_input(filename: str) -> Tuple[str, Dict[str, Dict[str, str]]]:
    with open(filename) as f:
        direction = f.readline().strip()
        f.readline()
        network = {}
        for line in f.readlines():
            start, left, right = re.findall(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line.strip())[0]
            network[start] = { 'L': left, 'R': right }
        return direction, network
    
def follow_directions_network(directions: str, network: Dict[str, Dict[str, str]]) -> int:
    node = START
    step = 0
    while node != END:
        next_direction = directions[step % len(directions)]
        node = network[node][next_direction]
        step += 1
    return step


def simultaneously_follow_directions(directions: str, network: Dict[str, Dict[str, str]]) -> int:
    nodes = [key for key in network.keys() if key[2] == 'A']
    step = 0
    while not all(map(lambda node: node[2] == 'Z', nodes)):
        next_direction = directions[step % len(directions)]
        for idx, node in enumerate(nodes):
            nodes[idx] = network[node][next_direction]
        step += 1
        if step % 10000 == 0:
            print(step, nodes)
    return step

def find_node_sequence(directions: str, network: Dict[str, Dict[str, str]], start_node: str) -> List[Tuple[str, int, int]]:
    node = start_node
    step = 0
    zs = []
    while True:
        next_direction = directions[step % len(directions)]
        node = network[node][next_direction]
        step += 1
        if node[2] == 'Z':
            if (node, step % len(directions)) in [(el[0], el[1]) for el in zs]:
                return zs
            else:
                zs.append((node, step % len(directions), step))
        

directions, network = parse_input('input.txt')

# part 1
# print(follow_directions_network(directions, network))

# part 2
# print(simultaneously_follow_directions(directions, network)) <---  too slow

start_nodes = [node for node in network.keys() if node[2] == 'A']
steps = []
for node in start_nodes:
    steps.append(find_node_sequence(directions, network, node)[0][2])

print(math.lcm(*steps))