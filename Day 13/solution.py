from typing import List, Union


def parse_input(filename: str) -> List[List[str]]:
    data = []
    lattice = []
    with open(filename) as f:
        for line in f.readlines():
            if line == '\n':
                data.append(lattice)
                lattice = []
            else:
                lattice.append(line.strip())
        else:
            if lattice != []:
                data.append(lattice)
        return data
    

def find_reflection_row(lattice: List[str]) -> Union[int, None]:
    rows = len(lattice)
    
    for i in range(rows - 1):
        for j in range(min(i + 1, rows - i - 1)):
            if lattice[i-j] != lattice[i+j+1]:
                break
        else:
            return i + 1

    return None


def find_reflection_row_with_smudge(lattice: List[str]) -> Union[int, None]:
    reflection_row = None
    rows = len(lattice)
    cols = len(lattice[0])

    for i in range(rows - 1):
        counter = 0
        for j in range(min(i + 1, rows - i - 1)):
            if lattice[i-j] != lattice[i+j+1]:
                counter += sum(lattice[i-j][k] != lattice[i+j+1][k] for k in range(cols))

        if counter == 1:
            reflection_row = i + 1

    return reflection_row


def find_reflection_col(lattice: List[str]) -> Union[int, None]:
    cols = len(lattice[0])

    for i in range(cols - 1):
        if [row[max(0, i+1-(cols-i-1)):i+1][::-1] for row in lattice] == [row[i+1:min(cols, 2*(i+1))] for row in lattice]:
            return i + 1
    
    return None
        

def find_reflection_col_with_smudge(lattice: List[str]) -> int:
    reflection_col = None
    cols = len(lattice[0])

    for i in range(cols - 1):
        before_line = [row[max(0, i+1-(cols-i-1)):i+1][::-1] for row in lattice]
        after_line = [row[i+1:min(cols, 2*(i+1))] for row in lattice]
        length = len(before_line) * len(before_line[0])
        if after_line != before_line:
            if sum(''.join(before_line)[k] != ''.join(after_line)[k] for k in range(length)) == 1:
                return i + 1
    
    return reflection_col


def count_patterns(lattices: List[List[str]], with_smudge=False) -> int:
    find_row = find_reflection_row_with_smudge if with_smudge else find_reflection_row
    find_col = find_reflection_col_with_smudge if with_smudge else find_reflection_col
    result = 0
    
    for lattice in lattices:
        if (x := find_row(lattice)) and x is not None:
            result += 100 * x
        
        if (x := find_col(lattice)) and x is not None:
            result += x

    return result


lattices = parse_input('input.txt')

# part 1
print(count_patterns(lattices))

#part 2
print(count_patterns(lattices, True))