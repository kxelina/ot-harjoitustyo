import unittest
from functionality.cards_on_table import Card_deck

class TestCard_deck(unittest.TestCase):
    def setUp(self):
        self.testdeck=Card_deck("easy")

    def test_create_card_deck(self):
        Card_deck.create_card_deck(self.testdeck, "easy")

        self.assertEqual(len(self.testdeck.deck), 40)