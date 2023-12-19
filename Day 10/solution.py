from typing import List, Tuple, Union

SOUTH = 'S'
WEST = 'W'
NORTH = 'N'
EAST = 'E'


PIPES = {
    '|': {
        SOUTH: NORTH,
        NORTH: SOUTH
    },
    '-': {
        EAST: WEST,
        WEST: EAST
    },
    'L': {
        NORTH: EAST,
        EAST: NORTH
    },
    'J': {
        WEST: NORTH,
        NORTH: WEST
    },
    '7': {
        WEST: SOUTH,
        SOUTH: WEST
    },
    'F': {
        SOUTH: EAST,
        EAST: SOUTH
    }
}

DIRECTIONS = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    EAST: (0, 1),
    WEST: (0, -1)
}

def parse_input(filename: str) -> List[str]:
    with open(filename) as f:
        data = [f'.{line.strip()}.' for line in f.readlines()]
        data.insert(0, '.' * len(data[0]))
        data.append('.' * len(data[0]))
        return data


def find_start(lattice: List[str]) -> Tuple[int, int]:
    for row, line in enumerate(lattice):
        for column, char in enumerate(line):
            if char == 'S':
                return (row, column)


def opposite(direction: Union[EAST, WEST, SOUTH, NORTH]) -> Union[EAST, WEST, SOUTH, NORTH]:
    if direction == NORTH:
        return SOUTH
    if direction == SOUTH:
        return NORTH
    if direction == EAST:
        return WEST
    if direction == WEST:
        return EAST

def find_loop(lattice: List[str]):
    start_row, start_col = find_start(lattice)

    ways = []
    if lattice[start_row-1][start_col] in ['F', '|', '7']:
        ways.append([(start_row, start_col, NORTH, 0)])

    if lattice[start_row][start_col+1] in ['-', 'J', '7']:
        ways.append([(start_row, start_col, EAST, 0)])

    if lattice[start_row+1][start_col] in ['|', 'L', 'J']:
        ways.append([(start_row, start_col, SOUTH, 0)])

    if lattice[start_row][start_col-1] in ['-', 'L', 'F']:
        ways.append([(start_row, start_col, WEST, 0)])

    while (ways[0][-1][0] != ways[1][-1][0] or ways[0][-1][1] != ways[1][-1][1]) or ways[0][-1][3] == 0:
        for idx, nodes in enumerate(ways):
            last_row, last_col, last_dir, step = nodes[-1]
            next_row = last_row + DIRECTIONS[last_dir][0]
            next_col = last_col + DIRECTIONS[last_dir][1]
            next_dir = PIPES[lattice[next_row][next_col]][opposite(last_dir)]
            next_node = (next_row, next_col, next_dir, step + 1)
            ways[idx].append(next_node)
    
    return ways
    

lattice = parse_input('input.txt')

# part 1
print(find_loop(lattice)[0][-1][3])