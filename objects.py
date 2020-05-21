# here are objects that are used in game
import instructions
from random import sample

class Game:
    def __init__(self):
        test_input_instructions()

        self.max_rounds = MAX_ROUNDS
        self.places = PLACES
        self.heroes = HEROES

        player_one_heroes, player_one_places = sample_cards(HEROES_PLAYER_ONE, PLACES_PLAYER_ONE)
        player_two_heroes, player_two_places = sample_cards(HEROES_PLAYER_TWO, PLACES_PLAYER_TWO)
        self.player_one = Player(player_one_heroes, player_one_places, IS_AI_PLAYER_ONE)
        self.player_two = Player(player_two_heroes, player_two_places, IS_AI_PLAYER_TWO)

        self.wins = [0, 0]
        self.rounds = 0

    def sample_cards(self, heroes_number, places_number):
        assert heroes_number >= len(self.heroes)
        assert places_number >= len(self.places)

        random.shuffle(self.heroes)
        player_heroes = self.heroes[:heroes_number]
        self.heroes = self.heroes[heroes_number:]

        random.shuffle(self.places)
        player_places = self.places[:places_number]
        self.places = self.places[places_number:]

        return player_heroes, player_places

    def start(self):
        next_is_first = True
        for game_round in range(self.max_rounds):
            if next_is_first:
                first_hero, place = self.player_one.turn(/*game_state*/)
                second_hero = self.player_two.answer(/*game_state*/, place)
            else:
                second_hero, place = self.player_two.turn(/*game_state*/)
                first_hero = self.player_one.answer(/*game_state*/, place)

            result = self.compare_heroes_on_place(first_hero, second_hero, place)

            if result == "WinFirst":
                self.wins[0] += 1
            else if result == "WinSecond":
                self.wins[1] += 1:
            else:
                pass

            if not all(self.wins < 2):
                break

            next_is_first = !next_is_first
        self.write_game_statistics()

class Player:
    def __init__(self):
        return None

class 
