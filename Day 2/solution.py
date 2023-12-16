import re

RED, RED_MAX = 'red', 12
GREEN, GREEN_MAX = 'green', 13
BLUE, BLUE_MAX = 'blue', 14

def sum_possible_games(filename):
    with open(filename) as f:
        possible_games = []
        for line in f.readlines():
            game_id, rounds = re.search(r"Game ([0-9]*): ([0-9a-z,; ]*)", line).groups()
            is_possible = True
            for round in rounds.split(';'):                
                for colors_tosses in map(lambda s: s.strip(), round.split(',')):
                    if not is_possible:
                        break

                    number, color = colors_tosses.split(' ')
                    number = int(number)
                    if color == RED and number > RED_MAX:
                        is_possible = False
                    elif color == GREEN and number > GREEN_MAX:
                        is_possible = False
                    elif color == BLUE and number > BLUE_MAX:
                        is_possible = False

            if is_possible:
                possible_games.append(game_id)

        return sum(map(int, possible_games))


def find_fewest_cubes_possible(filename):
    with open(filename) as f:
        powers = []
        for line in f.readlines():
            game_id, rounds = re.search(r"Game ([0-9]*): ([0-9a-z,; ]*)", line).groups()
            min_red, min_blue, min_green = 0, 0, 0
            for round in rounds.split(';'):                
                for colors_tosses in map(lambda s: s.strip(), round.split(',')):
                    number, color = colors_tosses.split(' ')
                    number = int(number)
                    if color == RED and number > min_red:
                        min_red = number
                    elif color == GREEN and number > min_green:
                        min_green = number
                    elif color == BLUE and number > min_blue:
                        min_blue = number
            powers.append(min_blue * min_green * min_red)
            
        return sum(powers)

print(sum_possible_games('input.txt'))
print(find_fewest_cubes_possible('input.txt'))

