from typing import List, Tuple
import re

def parse_input(filename: str) -> List[str]:
    with open(filename) as f:
        return f.read().split(',')

def hash_word(word: str) -> int:
    code = 0
    for letter in word:
        code = (code + ord(letter)) * 17 % 256

    return code

def place_in_hash_boxes(instructions: List[str]):
    boxes = [[] for _ in range(256)]
    for instruction in instructions:
        word1, word2, val = re.search(r'([a-z]*)-|([a-z]*)=(\d)', instruction).groups()

        word = word1 if word1 else word2
        hash_value = hash_word(word)
        idxs = [idx for idx, el in enumerate(boxes[hash_value]) if el[0] == word]

        if word1:
            if len(idxs) > 0:
                boxes[hash_value].pop(idxs[0])
        else:
            if len(idxs) > 0:
                boxes[hash_value][idxs[0]] = (word2, int(val))
            else:
                boxes[hash_value].append((word2, int(val)))
    
    return boxes


def calculate_boxes_power(boxes: List[List[Tuple[str, int]]]) -> int:
    power = 0
    for i, box in enumerate(boxes, 1):
        for j, lens in enumerate(box, 1):
            power += i * j * lens[1]

    return power


instructions = parse_input('input.txt')

# part 1
print(sum(hash_word(instruction) for instruction in instructions))

# part 2
boxes = place_in_hash_boxes(instructions)
print(calculate_boxes_power(boxes))