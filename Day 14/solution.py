from typing import List, Tuple


def parse_input(filename: str) -> List[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
    

def roll_rocks_to_north(platform: List[str]):
    rolled = [list(row) for row in platform]
    for row, line in enumerate(platform):
        for col, block in enumerate(line):
            if block == 'O':
                swap_idx = row
                while swap_idx > 0 and rolled[swap_idx-1][col] == '.':
                    swap_idx -= 1

                if swap_idx != row:
                    rolled[swap_idx][col], rolled[row][col] = 'O', '.'

    return rolled


def roll_rocks_to_south(platform: List[str]):
    rolled = [list(row) for row in platform][::-1]
    for row, line in enumerate(platform[::-1]):
        for col, block in enumerate(line):
            if block == 'O':
                swap_idx = row
                while swap_idx > 0 and rolled[swap_idx-1][col] == '.':
                    swap_idx -= 1
                
                if swap_idx != row:
                    rolled[swap_idx][col], rolled[row][col] = 'O', '.'
        
    return rolled[::-1]


def roll_rocks_to_west(platform: List[str]):
    rolled = [list(row) for row in platform]
    for row, line in enumerate(platform):
        for col, block in enumerate(line):
            if block == 'O':
                swap_idx = col
                while swap_idx > 0 and rolled[row][swap_idx - 1] == '.':
                    swap_idx -= 1

                if swap_idx != col:
                    rolled[row][swap_idx], rolled[row][col] = 'O', '.'

    return rolled


def roll_rocks_to_east(platform: List[str]):
    rolled = [list(row)[::-1] for row in platform]
    for row, line in enumerate(platform):
        for col, block in enumerate(line[::-1]):
            if block == 'O':
                swap_idx = col
                while swap_idx > 0 and rolled[row][swap_idx - 1] == '.':
                    swap_idx -= 1

                if swap_idx != col:
                    rolled[row][swap_idx], rolled[row][col] = 'O', '.'

    return [row[::-1] for row in rolled]


def count_load_after_cycles(platform: List[str], cycles: int) -> int:
    rolled = platform.copy()
    saved = []
    for i in range(cycles):
        for roll_function in [roll_rocks_to_north, roll_rocks_to_west, roll_rocks_to_south, roll_rocks_to_east]:
            rolled = roll_function(rolled)
    
        if rolled in saved:
            idx = saved.index(rolled)
            cycle = i - idx
            return count_load(saved[idx + (cycles - idx) % cycle - 1 ])
        else:
            saved.append(rolled.copy())

    return count_load(rolled)


def count_load(platform: List[str]) -> int:
    load = 0
    for idx, line in enumerate(platform[::-1], 1):
        load += sum(idx for block in line if block == 'O')

    return load


platform = parse_input('input.txt')

#part 1
rolled = roll_rocks_to_north(platform)
print(count_load(rolled))

#part 2
count = count_load_after_cycles(platform, 1000000000)
print(count)