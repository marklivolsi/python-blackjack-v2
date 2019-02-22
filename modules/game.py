from .player import Player
from .game_funcs import *


class Game:
    num_decks_for_reload = 1
    max_num_players = 10

    def __init__(self, quick_game=True):
        self.quick_game = quick_game
        self.dealer = Player(name='Dealer')
        self.player_list = []

    def set_game_type(self):
        print("Would you like to play a quick game? Quick games are one player versus the dealer,\n"
              "and the player starts off with $1,000 in chips. Normal games allow you to set the number of players,\n"
              "player names, chip amounts for each player, and number of decks in the dealer's shoe.\n")
        quick_game = yes_no_input("Type 'yes' for a quick game, or 'no' for a normal game: \n")
        if not quick_game:
            self.quick_game = False

    def print_table(self, show_dealer=False):
        if show_dealer:
            print("Dealer's hand: {} ({} points)".format(self.dealer.hands[0], self.dealer.hands[0].points))
        else:
            print("Dealer's hand: [{}, ???]".format(self.dealer.hands[0][0]))
        for player in self.player_list:
            for hand in player.hands:
                print(hand_detail(player, hand))
