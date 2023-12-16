word_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def map_words_to_numbers(string):
    transformed = string
    while (occurrences := { i: index for i, el in enumerate(word_number) if (index := transformed.find(el)) > -1 })  \
            and len(occurrences) > 0:
        first_number = min(occurrences, key=occurrences.get)
        transformed = transformed.replace(word_number[first_number], str(first_number), 1)

    return transformed


def count_numbers(filename, map_words=False):
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            word = map_words_to_numbers(line.strip()) if map_words else line.strip() 
            digits = list(filter(str.isdigit, word))
            sum += int(digits[0] + digits[-1])
    return sum

# part 1
print(count_numbers('input.txt', False))

# part 2: map words to numbers
print(count_numbers('input.txt', True))