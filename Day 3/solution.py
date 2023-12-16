# load input data with additional empty border (to deal with edge cases)
def parse_input(filename):
    with open(filename) as f:
        data = []
        for line in f.readlines():
            data.append('.' + line.strip() + '.')
        data.insert(0, '.' * len(data[0]))
        data.append('.' * len(data[0]))
    return data

def is_adjacent_to_symbol(board, row, col, excluded=['.', *[str(x) for x in range(10)]]):
    neighbours = [
        board[row - 1][col],
        board[row - 1][col + 1],
        board[row][col + 1],
        board[row + 1][col + 1],
        board[row + 1][col],
        board[row + 1][col - 1],
        board[row][col - 1],
        board[row - 1][col - 1]
    ]

    return any([x not in excluded for x in neighbours])


def count_numbers_neighbours(board, row, col):
    neighbours = [
        board[row - 1][col],
        board[row - 1][col + 1],
        board[row][col + 1],
        board[row + 1][col + 1],
        board[row + 1][col],
        board[row + 1][col - 1],
        board[row][col - 1],
        board[row - 1][col - 1]
    ]

    return sum([x.isdigit() for x in neighbours])

def find_part_numbers(board):
    valid_numbers = []
    for row, line in enumerate(board[1:-1], 1):
        current_number = ''
        is_valid = False
        for col, symbol in enumerate(line[1:-1], 1):
            if symbol.isdigit():
                current_number += symbol
                if not is_valid:
                    is_valid = is_adjacent_to_symbol(board, row, col)
            else:
                if current_number != '' and is_valid:
                    valid_numbers.append(int(current_number))
                
                current_number = ''
                is_valid = False

        if current_number != '' and is_valid:
            valid_numbers.append(int(current_number))

        current_number = ''
        is_valid = False

    return valid_numbers

def find_gear_ratio(board):
    gear_ratio = 0
    for row, line in enumerate(board[1:-1], 1):
        for col, symbol in enumerate(line[1:-1], 1):
            if symbol == '*' and count_numbers_neighbours(board, row, col) == 2:
                gear_ratio
            

board = parse_input('input.txt')
print(sum(find_part_numbers(board)))