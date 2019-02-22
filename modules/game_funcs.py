from random import shuffle
from .player import Player, Hand
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


def get_wager(player):
    while True:
        wager = int_input('{}, please enter your wager:\n'.format(player))
        if check_wager(wager, player):
            return wager
        else:
            print("Sorry, you don't have enough chips. Please try again. (remaining chips: {})\n".format(player.chips))
            continue


def set_wager(wager, player, hand):
    player.chips -= wager
    hand.wager += wager


def hit(deck, hand):
    hand.cards.append(draw(deck))


def double_down(player, hand, deck):  # handle logic for overdrawing chips before function call
    player.chips -= hand.wager
    hand.wager *= 2
    hit(deck, hand)


def surrender(player, hand):
    player.chips += hand.wager / 2
    hand.wager = 0
    hand.cards = []


def split_hand(player, hand):  # handle logic for overdrawing chips before function call
    card = hand.cards.pop()
    new_hand = Hand(wager=hand.wager)
    new_hand.cards.append(card)
    player.hands.append(new_hand)
    player.chips -= hand.wager


""" Game functions """


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


def check_wager(wager, player):
    return wager <= player.chips


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
