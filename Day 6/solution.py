from functools import reduce

def parse_input_1(filename):
    with open(filename) as f:
        times = map(int, f.readline().strip().split()[1:])
        distances = map(int, f.readline().strip().split()[1:])
        return list(zip(times, distances))
    
def parse_input_2(filename):
    with open(filename) as f:
        time = int(''.join(f.readline().strip().split()[1:]))
        distance = int(''.join(f.readline().strip().split()[1:]))
        return time, distance

def find_solutions_numbers(time, distance):
    return sum([i * (time - i) > distance for i in range(time)])


# part 1: multiply numbers of all ways in all races
scores = parse_input_1('input.txt')
print(reduce(lambda x, y: x * y, [find_solutions_numbers(*score) for score in scores]))

# part 2: parse as one long race
score = parse_input_2('input.txt')
print(find_solutions_numbers(*score))

