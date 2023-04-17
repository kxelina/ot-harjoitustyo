import unittest
from services.game import Game
from entities.card import Card
from entities.card_suit import Suit


class TestCard_deck(unittest.TestCase):

    def test_create_card_deck(self):
        newgame = Game("easy", self)

        self.assertEqual(len(newgame.deck), 40)

    def test_card_deck_right_order(self):
        newgame = Game("easy", self)
        Game.show_deck(newgame)
        Game.debug_print_deck(newgame)

        self.assertTrue(newgame.deck[0].is_same(Card(Suit.SPADE, 1, self)))
        self.assertEqual(newgame.deck[-1].to_string(),
                         Card(Suit.CLUB, 10, self).to_string())

    def test_card_deck_shuffle(self):
        newgame = Game("easy", self)
        Game.shuffle(newgame)
        Game.debug_print_deck(newgame)

        self.assertFalse(newgame.deck[0].is_same(Card(Suit.SPADE, 1, self)))
        # self.assertEqual(len(self.newgame.deck), 41)

    def test_card_right_place(self):
        newgame = Game("easy", self)
        Game.shuffle(newgame)
        Game.place_cards(newgame)

        self.assertEqual(newgame.deck[0].column, 0)
        self.assertEqual(newgame.deck[0].row, 0)
        self.assertEqual(newgame.deck[-1].column, 9)
        self.assertEqual(newgame.deck[-1].row, 3)
        self.assertEqual(newgame.deck[0].button_place_x(), 50)
        self.assertEqual(newgame.deck[0].button_place_y(), 100)
        self.assertEqual(newgame.deck[-1].button_place_x(), 185*9+50)
        self.assertEqual(newgame.deck[-1].button_place_y(), 200*3+100)

    # def test_
