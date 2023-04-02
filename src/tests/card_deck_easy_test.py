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

    def test_create_card_deck2(self):
        Card_deck.create_card_deck(self.testdeck, "easy")
        Card_deck.show_deck(self.testdeck)
        Card_deck.print_deck(self.testdeck)
        self.assertEqual(self.testdeck.deck[0],Card(Suit.spade, 1))
        self.assertEqual(len(self.testdeck.deck), 41)