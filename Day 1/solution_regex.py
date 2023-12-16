import re

WORDS_NUMBERS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

DIGITS = '|'.join(WORDS_NUMBERS.keys())
    
def count_numbers(filename):
    with open(filename) as f:
        sum = 0
        for line in f.readlines():
            match = re.findall(r'(\d)\w*(\d)|(\d)', line.strip())
            if len(match) > 0 and (numbers := match[0]):
                sum += int(numbers[0] + numbers[1]) if numbers[0] else int(numbers[2] + numbers[2])
        return sum

def count_numbers_with_word_mapping(filename):
    with open(filename) as f:
        sum = 0
        for line in f.readlines():
            match = re.findall(rf'(\d|{DIGITS})\w*(\d|{DIGITS})|(\d|{DIGITS})', line.strip())
            if len(match) > 0 and (numbers := match[0]):
                numbers =  list(map(lambda x: WORDS_NUMBERS.get(x, x), match[0]))
                sum += int(numbers[0] + numbers[1]) if numbers[0] else int(numbers[2] + numbers[2])
    return sum


# part 1
print(count_numbers('input.txt'))

# part 2
print(count_numbers_with_word_mapping('input.txt'))