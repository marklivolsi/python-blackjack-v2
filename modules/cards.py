point_dict = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.point_value = point_dict[self.value]

    def __repr__(self):
        return self.value + ' of ' + self.suit

    # def __eq__(self, other):
    #     if isinstance(other, Card):
    #         return self.point_value == other.point_value
    #     return NotImplemented


# Deck can just be an array of cards this way.
