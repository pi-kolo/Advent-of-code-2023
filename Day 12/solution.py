from typing import List, Tuple
from itertools import combinations

def parse_input(filename: str, unfold=False):
    with open(filename) as f:
        data = []
        for line in f.readlines():
            sequence, numbers = line.strip().split()
            numbers = [int(num) for num in numbers.split(',')]
            if unfold:
                data.append(((sequence + '?') * 5, numbers * 5))
            else:
                data.append((sequence, numbers))

    return data

def find_arrangements(sequence: str, conditions):
    possible_arrangments = [list(sequence)]
    counter, max_occ = 0, sum(conditions)
    for i, c in enumerate(sequence):
        if c == '?' and counter <= max_occ:
            new_sequences = []
            for j, seq in enumerate(possible_arrangments):
                possible_arrangments[j][i] = '#'
                alternative = seq.copy()
                alternative[i] = '.'
                new_sequences.append(alternative)
            possible_arrangments.extend(new_sequences)
            new_sequences = []
        elif c == '#':
            counter += 1
    return [''.join(seq) for seq in possible_arrangments]


def check_if_arrangement_correct(sequence: str, conditions: List[int]) -> bool:
    occurences = [len(el) for el in sequence.split('.') if el != '']
    return occurences == conditions


def find_total_arrangements_number(data: List[Tuple[str, List[int]]]) -> int:
    total = 0
    for line in data:
        possible_arrangments = find_arrangements(line[0], line[1])
        total += sum(check_if_arrangement_correct(arrangement, line[1]) for arrangement in possible_arrangments)
    return total


def find_arrangements2(sequence: str, conditions: List[int]):
    possible_arrangments = []
    length = len(sequence)
    indices_list = combinations(range(length), len(conditions))
    for indices in indices_list:
        s = ''
        for i, idx in enumerate(indices):
            s = s + (idx - len(s) + i) * '.' + '#' * conditions[i]
        if len(s) == len(sequence):
            for i, c in enumerate(sequence):
                if (c == '#' or c == '.') and c != s[i]:
                    break
            else:
                possible_arrangments.append(s)
    return possible_arrangments


# part 1
data = parse_input('input.txt')
print(find_total_arrangements_number(data))
