import unittest
from services.cards_on_table import Carddeck
from services.cards_on_table import Card
from services.cards_on_table import Suit


class TestCard_deck(unittest.TestCase):
    def setUp(self):
        self.testdeck = Carddeck("easy")

    def test_create_card_deck(self):
        Carddeck.create_card_deck(self.testdeck, "easy")

        self.assertEqual(len(self.testdeck.deck), 40)

    def test_card_deck_right_order(self):
        Carddeck.create_card_deck(self.testdeck, "easy")
        Carddeck.show_deck(self.testdeck)
        Carddeck.debug_print_deck(self.testdeck)

        self.assertTrue(self.testdeck.deck[0].is_same(Card(Suit.spade, 1)))
        self.assertEqual(
            self.testdeck.deck[-1].to_string(), Card(Suit.club, 10).to_string())

    def test_card_deck_shuffle(self):
        Carddeck.create_card_deck(self.testdeck, "easy")
        Carddeck.shuffle(self.testdeck)
        Carddeck.debug_print_deck(self.testdeck)

        self.assertFalse(self.testdeck.deck[0].is_same(Card(Suit.spade, 1)))
        # self.assertEqual(len(self.testdeck.deck), 41)
