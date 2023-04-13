import unittest
from services.game import Game
from entities.card import Card
from entities.card_suit import Suit


class TestCard_deck(unittest.TestCase):
    def setUp(self):
        self.testdeck = Game("easy", self)

    def test_create_card_deck(self):
        Game.create_game(self.testdeck, "easy", self)

        self.assertEqual(len(self.testdeck.deck), 40)

    def test_card_deck_right_order(self):
        Game.create_game(self.testdeck, "easy", self)
        Game.show_deck(self.testdeck)
        Game.debug_print_deck(self.testdeck)

        self.assertTrue(self.testdeck.deck[0].is_same(Card(Suit.SPADE, 1, "easy", self)))
        self.assertEqual(self.testdeck.deck[-1].to_string(), Card(Suit.CLUB, 10, "easy", self).to_string())

    def test_card_deck_shuffle(self):
        Game.create_game(self.testdeck, "easy", self)
        Game.shuffle(self.testdeck)
        Game.debug_print_deck(self.testdeck)

        self.assertFalse(self.testdeck.deck[0].is_same(Card(Suit.SPADE, 1, "easy", self)))
        # self.assertEqual(len(self.testdeck.deck), 41)

    def test_card_right_place(self):
        Game.create_game(self.testdeck, "easy", self)
        Game.shuffle(self.testdeck)
        Game.place_cards(self.testdeck)

        self.assertEqual(self.testdeck.deck[0], Card.card_button_place(self, 50, 100))
