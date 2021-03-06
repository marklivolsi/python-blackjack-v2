import unittest
from unittest.mock import patch
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

    @patch('modules.game_funcs.int_input', return_value=100)
    def test_get_wager(self, mock_input):
        """ Test get_wager function returns wager only if not exceeding remaining chips """
        player = Player(chips=200)
        wager = get_wager(player)
        self.assertEqual(wager, 100)

    def test_set_wager(self):
        """ Test set_wager correctly deducts from player chips and adds to hand wager """
        player, hand = Player(chips=200), Hand()
        wager = 50
        set_wager(wager, player, hand)
        self.assertEqual(hand.wager, 50)
        self.assertEqual(player.chips, 150)

    def test_double_down(self):
        """ Test double_down doubles wager and removes chips """
        player, hand, deck = Player(chips=200), Hand(wager=50), []
        double_down(player, hand, deck)
        self.assertEqual(player.chips, 150)
        self.assertEqual(hand.wager, 100)

    def test_surrender(self):
        """ Test surrender returns half of wager and clears hand """
        player, hand = Player(chips=200), Hand(wager=100)
        surrender(player, hand)
        self.assertEqual(len(hand.cards), 0)
        self.assertEqual(hand.wager, 0)
        self.assertEqual(player.chips, 250)

    def test_split_hand(self):
        """ Test split_hand removes card from hand, creates new hand, and adds to players hands list """
        player, hand1 = Player(), Hand()
        card = Card('Ace', 'Spades')
        for _ in range(2):
            hand1.cards.append(card)
        player.hands.append(hand1)
        self.assertEqual(len(player.hands), 1)
        self.assertEqual(len(player.hands[0].cards), 2)

        split_hand(player, player.hands[0])
        self.assertEqual(len(player.hands), 2)
        self.assertEqual(player.hands[0].cards, player.hands[1].cards)

    def test_split_hand_wager(self):
        """ Test split hand sets equal wager on new hand """
        player, hand1 = Player(chips=200), Hand(wager=50)
        card = Card('Ace', 'Spades')
        for _ in range(2):
            hand1.cards.append(card)
        player.hands.append(hand1)
        split_hand(player, player.hands[0])
        self.assertEqual(player.hands[0].wager, 50)
        self.assertEqual(player.hands[1].wager, 50)
        self.assertEqual(player.chips, 150)


class TestGameFunctions(unittest.TestCase):

    def test_hand_detail(self):
        """ Test that hand detail function returns correct string """
        player, hand = Player(name='Joe', chips=500), Hand(wager=50)
        hand.cards = [Card('Ace', 'Diamonds'), Card('Two', 'Clubs')]  # 13 points
        s = hand_detail(player, hand)
        s_test = "Joe's hand: [Ace of Diamonds, Two of Clubs] (point total: 13, bet: 50, remaining chips: 500)\n"
        self.assertEqual(s, s_test)

    def test_check_wager(self):
        """ Test that check wager function returns false if wager exceeds remaining chips """
        player, hand = Player(chips=200), Hand(wager=300)
        self.assertEqual(check_wager(hand.wager, player), False)


if __name__ == '__main__':
    unittest.main()
