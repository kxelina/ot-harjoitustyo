import unittest
from functionality.cards_on_table import Card_deck
from functionality.cards_on_table import Card
from functionality.cards_on_table import Suit

class TestCard_deck(unittest.TestCase):
    def setUp(self):
        self.testdeck=Card_deck("easy")

    def test_create_card_deck(self):
        Card_deck.create_card_deck(self.testdeck, "easy")

        self.assertEqual(len(self.testdeck.deck), 40)

    def test_card_deck_right_order(self):
        Card_deck.create_card_deck(self.testdeck, "easy")
        Card_deck.show_deck(self.testdeck)
        Card_deck.debug_print_deck(self.testdeck)

        self.assertTrue(self.testdeck.deck[0].is_same(Card(Suit.spade, 1)))
        self.assertEqual(self.testdeck.deck[-1].to_string(),Card(Suit.club, 10).to_string())
        

    def test_card_deck_shuffle(self):
        Card_deck.create_card_deck(self.testdeck, "easy")
        Card_deck.shuffle(self.testdeck)
        Card_deck.debug_print_deck(self.testdeck)

        self.assertFalse(self.testdeck.deck[0].is_same(Card(Suit.spade, 1)))
        #self.assertEqual(len(self.testdeck.deck), 41)