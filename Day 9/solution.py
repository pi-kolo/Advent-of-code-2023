from typing import List

def parse_input(filename: str) -> List[List[int]]:
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(list(map(int, line.strip().split())))
        return data
    
def extrapolate(sequence: List[int], backwards=False) -> List[int]:
    differences = [sequence]
    row = sequence
    while not all([el == 0 for el in row]):
        new_row = [row[i+1] - row[i] for i in range(len(row) - 1)]
        differences.append(new_row)
        row = new_row

    for idx, diff_seq in enumerate(differences[:0:-1], 1):
        if backwards:
            differences[-1-idx].insert(0, differences[-1-idx][0] - diff_seq[0])
        else:
            differences[-1-idx].append(differences[-1-idx][-1] + diff_seq[-1])

    return differences[0][0] if backwards else differences[0][-1]


sequences = parse_input('input.txt')

# part 1: find next values
print(sum(extrapolate(sequence) for sequence in sequences))

# part 2: find previous values
print(sum(extrapolate(sequence, backwards=True) for sequence in sequences))
    