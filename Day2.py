# State 1: Imports and Variable Definitions
def is_possible(cube_counts, game):
    counts = cube_counts.copy()
    
    for subset in game:
        for cube in subset:
            color, num = cube.split()
            counts[color] -= int(num)
            if counts[color] < 0:
                return False
    
    return True

def possible_games(cube_counts, games):
    possible_ids = []

# Given cube counts
cube_counts = {'red': 12, 'green': 13, 'blue': 14}

# Your puzzle input (list of games)
games = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]
