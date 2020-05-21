# all available instructions of game are set here

# the game continues until one of the players collects this number of victories
MAX_ROUNDS = 3

# plater instructions
HEROES_PLAYER_ONE = 5
HEROES_PLAYER_TWO = 5
IS_AI_PLAYER_ONE = True
IS_AI_PLAYER_ONE = True
PLACES_PLAYER_ONE = 3
PLACES_PLAYER_TWO = 3

# [number of cards, index of place in heroes]
PLACES = [
	[3, 0],
	[3, 1],
	[3, 2],
]

# [number of cards, [force of this card on corresponding indexes]]
HEROES = [
	[3, [3, 1, 2]],
	[3, [3, 2, 1]],
	[3, [2, 3, 1]],
	[3, [2, 1, 3]],
	[3, [1, 3, 2]],
	[3, [1, 3, 2]],
]
