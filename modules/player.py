class Player:
    def __init__(self, number=1, name='Player 1', chips=1000):
        self.number = number
        self.name = name
        self.chips = chips
        self.hands = []

    def __repr__(self):
        return self.name


class Hand:
    def __init__(self, cards=[], wager=0):
        self.cards = cards
        self.wager = wager

    def __repr__(self):
        return str(self.cards)

    @property
    def points(self):
        return self.sum_hand_points()

    def sum_hand_points(self):
        total = sum(card.point_value for card in self.cards)
        if total > 21 and any(card.value == 'Ace' for card in self.cards):
            total -= 10
        return total


