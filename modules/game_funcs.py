from random import shuffle
from .cards import Card, point_dict, suits


""" Deck functions """


def reload(deck, num_decks):
    for _ in range(0, num_decks):
        for card in point_dict.keys():
            for suit in suits:
                deck.append(Card(card, suit))
    shuffle(deck)


def draw(deck):
    if len(deck) == 0:
        reload(deck, 1)
    return deck.pop()


""" Player functions """


def hit(deck, hand):
    hand.cards.append(draw(deck))


""" Game functions """


def print_hand_detail(player, hand):
    print("{}'s hand: {} (point total: {}, bet: {}, remaining chips: {})".format(player, hand, hand.points,
                                                                                 hand.wager, player.chips))
    print()


""" Helper functions """


def get_int_input(text):
    while True:
        try:
            value = int(input(text))
            break
        except ValueError:
            print('Please enter an integer value.')
            continue
    return value


def yes_no_choice(text):
    choice = None
    while choice not in ('yes', 'no'):
        choice = input(text).lower()
