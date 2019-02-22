import unittest
from .game_funcs import *
from .cards import Card
from .player import Player, Hand


class TestDeckFunctions(unittest.TestCase):

    def test_reload(self):
        """ Test correct number of cards are loaded into deck """
        d1, d2, d12 = [], [], []
        reload(d1)
        reload(d2, 2)
        reload(d12, 12)
        self.assertEqual(len(d1), 52)
        self.assertEqual(len(d2), 104)
        self.assertEqual(len(d12), 624)

    def test_draw(self):
        """ Test that draw removes one card from the deck and returns it, and reloads when deck is empty """
        deck, draw_pile = [], []
        reload(deck)
        draw_pile.append(draw(deck))
        self.assertEqual(len(deck), 51)
        for _ in range(52):
            draw_pile.append(draw(deck))
        self.assertEqual(len(draw_pile), 53)
        self.assertEqual(len(deck), 51)


class TestPlayerFunctions(unittest.TestCase):

    def test_hit(self):
        """ Test that hit removes one card and adds that card to hand """
        deck, hand = [], Hand()
        reload(deck)
        hit(deck, hand)
        self.assertEqual(len(deck), 51)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.cards[0] in deck, False)


class TestGameFunctions(unittest.TestCase):

    def test_hand_detail(self):
        """ Test that hand detail function returns correct string """
        player, hand = Player(name='Joe', chips=500), Hand(wager=50)
        hand.cards = [Card('Ace', 'Diamonds'), Card('Two', 'Clubs')]  # 13 points
        s = hand_detail(player, hand)
        s_test = "Joe's hand: [Ace of Diamonds, Two of Clubs] (point total: 13, bet: 50, remaining chips: 500)\n"
        self.assertEqual(s, s_test)


if __name__ == '__main__':
    unittest.main()
