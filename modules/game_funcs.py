from random import shuffle
from .cards import Card, point_dict, suits
from .game import Game


""" Deck functions """


def reload(deck, num_decks=Game.num_decks_for_reload):
    for _ in range(0, num_decks):
        for card in point_dict.keys():
            for suit in suits:
                deck.append(Card(card, suit))
    shuffle(deck)


def draw(deck):
    if len(deck) == 0:
        reload(deck, Game.num_decks_for_reload)
    return deck.pop()


""" Player functions """


def hit(deck, hand):
    hand.cards.append(draw(deck))


""" Game functions """


def check_wager(wager, player):
    if wager <= player.chips:
        return True
    return False


def set_num_players(max_num=Game.max_num_players):
    num_players = None
    while num_players not in range(1, max_num+1):
        num_players = int_input("Please enter the desired number of players (max 10):\n")
    return num_players


def hand_detail(player, hand):  # For printing
    string = "{}'s hand: {} (point total: {}, bet: {}, remaining chips: {})\n".format(player, hand, hand.points,
                                                                                      hand.wager, player.chips)
    return string


""" Helper functions """


def int_input(text):
    while True:
        try:
            value = int(input(text))
            break
        except ValueError:
            print('Please enter an integer value.\n')
            continue
    return value


def yes_no_input(text):
    choice = None
    while choice not in ('yes', 'no'):
        choice = input(text).lower()
    return choice
