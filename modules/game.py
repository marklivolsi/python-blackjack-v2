from .player import Player
from .game_funcs import *


class Game:
    num_decks_for_reload = 1
    max_num_players = 10

    def __init__(self, quick_game=True):
        self.quick_game = quick_game
        self.dealer = Player(name='Dealer')
        self.player_list = []

    def print_table(self, show_dealer=False):
        if show_dealer:
            print("Dealer's hand: {} ({} points)".format(self.dealer.hands[0], self.dealer.hands[0].points))
        else:
            print("Dealer's hand: [{}, ???]".format(self.dealer.hands[0][0]))
        for player in self.player_list:
            for hand in player.hands:
                print(hand_detail(player, hand))
