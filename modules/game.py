from .player import Player
from .game_funcs import *


class Game:
    num_decks_for_reload = 1
    max_num_players = 10

    def __init__(self, quick_game=True):
        self.quick_game = quick_game
        self.dealer = Player(name='Dealer')
        self.player_list = []
