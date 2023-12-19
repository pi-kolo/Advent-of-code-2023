from typing import List, Tuple, Union
from itertools import combinations

# if expand == False attach information abour empty rows and cols
def parse_input(filename: str, expand=True) -> Union[List[List[str]], Tuple[List[List[str]], List[int], List[int]]]:
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
    
    expanded = data.copy()
    
    rows_to_extend = [idx for idx, line in enumerate(expanded) if all(el == '.' for el in line)]
    for count, row in enumerate(rows_to_extend):
        expanded.insert(row + count, '.' * len(expanded[0]))
    
    cols_to_extend = [i for i in range(len(expanded[0])) if all(row[i] == '.' for row in expanded)]
    for count, col in enumerate(cols_to_extend):
        for i, line in enumerate(expanded):
            expanded[i] = line[:count+col] + '.' + line[count+col:]

    return expanded if expand else data, rows_to_extend, cols_to_extend


def find_galaxies(lattice: List[List[str]]) -> List[Tuple[int, int]]:
    galaxies = []
    for row, line in enumerate(lattice):
        for col, char in enumerate(line):
            if char == '#':
                galaxies.append((row, col))
    
    return galaxies


def distance(start: Tuple[int, int], end: Tuple[int, int]) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def calculate_distances(lattice: List[List[str]]) -> int:
    galaxies = find_galaxies(lattice)
    pairs = list(combinations(galaxies, 2))
    return sum([distance(x, y) for x, y in pairs])


def calculate_distances_v2(lattice: List[List[str]], rows_without_galaxies: List[int], cols_without_galaxies: List[int], galaxies_speed: int) -> int:
    galaxies = find_galaxies(lattice)
    distances = 0
    for p1, p2 in combinations(galaxies, 2):
        distances += distance(p1, p2)
        r1, r2 = sorted([p1[0], p2[0]])
        c1, c2 = sorted([p1[1], p2[1]])

        for row in rows_without_galaxies:
            if r1 < row and r2 > row:
                distances += galaxies_speed

        for col in  cols_without_galaxies:
            if c1 < col and c2 > col:
                distances += galaxies_speed
    
    return distances


# part 1
lattice_expanded = parse_input('input.txt', True)[0]
print(calculate_distances(lattice_expanded))

# part 2
lattice, rows_without_galaxies, cols_without_galaxies = parse_input('input.txt', False)
print(calculate_distances_v2(lattice, rows_without_galaxies, cols_without_galaxies, 10**6 - 1))