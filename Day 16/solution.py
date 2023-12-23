from typing import List, Tuple

def parse_input(filename: str): 
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
    

def traverse_map(lattice: List[str], start_data: Tuple[int, int, str]) -> List[str]:
    x, y, direction = start_data
    visited_map = [[{ el: False for el in ['N', 'S', 'W', 'E']} for _ in line] for line in lattice] 

    ways = []
    while True:
        # match position and in-direction to new position and in-direction
        while y < 0 or y >= len(lattice) or x < 0 or x >= len(lattice[0]) or visited_map[y][x][direction]:
            if len(ways) > 0:
                x, y, direction = ways.pop()
            else:
                return [''.join(['#' if any(el.values()) else '.' for el in line]) for line in visited_map]

        visited_map[y][x][direction] = True

        match (lattice[y][x], direction):
            case ('/', 'S'):
                x += 1
                direction = 'W'
            case ('/', 'W'):
                y -= 1
                direction = 'S'
            case ('/', 'N'):
                x -= 1
                direction = 'E'
            case ('/', 'E'):
                y += 1
                direction = 'N'
            
            case ('\\', 'S'):
                x -= 1
                direction = 'E'
            case ('\\', 'W'):
                y += 1
                direction = 'N'
            case ('\\', 'N'):
                x += 1
                direction = 'W'
            case ('\\', 'E'):
                y -= 1
                direction = 'S'

            case ('|', 'S') | ('.', 'S'):
                y -= 1
            case ('|', 'N') | ('.', 'N'):
                y += 1
            case ('-', 'E') | ('.', 'E'):
                x -= 1
            case ('-', 'W') | ('.', 'W'):
                x += 1

            case ('|', 'E') | ('|', 'W'):
                ways.append((x, y + 1, 'N'))
                y -= 1
                direction = 'S'
            case ('-', 'S') | ('-', 'N'):
                ways.append((x + 1, y, 'W'))
                x -= 1
                direction = 'E'


def count_energized_tiles(visited_map: List[str]) -> int:
    return sum([sum([el == '#' for el in line]) for line in visited_map])


def find_max_energy_level(lattice: List[str]) -> int:
    max_level = 0
    for idx, _ in enumerate(lattice[0]):
        energized_tiles = count_energized_tiles(traverse_map(lattice.copy(), (idx, 0, 'N')))
        if energized_tiles > max_level:
            max_level = energized_tiles
    
    for idx, _ in enumerate(lattice[-1]):
        energized_tiles = count_energized_tiles(traverse_map(lattice.copy(), (idx, len(lattice) - 1, 'S')))
        if energized_tiles > max_level:
            max_level = energized_tiles
    
    for idx in range(len(lattice)):
        energized_tiles = count_energized_tiles(traverse_map(lattice.copy(), (0, idx, 'W')))
        if energized_tiles > max_level:
            max_level = energized_tiles

    for idx in range(len(lattice)):
        energized_tiles = count_energized_tiles(traverse_map(lattice.copy(), (len(lattice[0]) - 1, idx, 'E')))
        if energized_tiles > max_level:
            max_level = energized_tiles
    
    return max_level


lattice = parse_input('input.txt')

# part 1
visited = traverse_map(lattice, (0, 0, 'W'))
print(count_energized_tiles(visited))

# part 2
print(find_max_energy_level(lattice))
