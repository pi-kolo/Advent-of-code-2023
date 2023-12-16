import re

def parse_input(filename):
    games_data = {}
    with open(filename) as f:
        for line in f.readlines():
            game_id, winning_numbers, game_numbers = re.search(r"Card ([0-9 ]*): ([0-9 ]*) \| *([0-9 ]*)", line).groups()
            games_data[int(game_id)] = { 
                'winning_numbers': { int(num) for num in winning_numbers.split() },
                'game_numbers': { int(num) for num in game_numbers.split() }
            }

        return games_data

def count_winning_result(games_data):
    result = 0
    for game_data in games_data.values():
        common_numbers = len(game_data['winning_numbers'] & game_data['game_numbers'])
        if common_numbers > 0:
            result += 2 ** (common_numbers - 1)
    
    return result

def count_scratchcards(games_data):
    for idx in games_data:
        games_data[idx]['scratchcard_numbers'] = 1

    for idx, data in games_data.items():
        common_numbers = len(data['winning_numbers'] & data['game_numbers'])
        for i in range(common_numbers):
            games_data[idx + i + 1]['scratchcard_numbers'] += games_data[idx]['scratchcard_numbers']
        
    return sum([game['scratchcard_numbers'] for game in games_data.values()])


# part 1
games_data = parse_input('input.txt')
print(count_winning_result(games_data))

# part 2
print(count_scratchcards(games_data))