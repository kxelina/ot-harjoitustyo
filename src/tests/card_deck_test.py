import unittest
import os
from services.game import Game
from entities.card import Card
from entities.card_suit import Suit
from entities.game_level import Level
from database_initialize import initialize_database


class TestCard_deck(unittest.TestCase):

    def test_create_card_deck(self):
        newgame = Game(Level.EASY, None, None)
        self.assertEqual(len(newgame.deck), 20)
        newgame = Game(Level.MEDIUM, None, None)
        self.assertEqual(len(newgame.deck), 40)
        newgame = Game(Level.HARD, None, None)
        self.assertEqual(len(newgame.deck), 40)

    def test_card_deck_right_order(self):
        newgame = Game(Level.EASY, None, None)
        deck = newgame.get_deck()
        self.assertTrue(deck[0].is_same(Card(Suit.SPADE, 1, newgame)))
        self.assertEqual(deck[-1].to_string(),
                         Card(Suit.CLUB, 5, newgame).to_string())

        newgame = Game(Level.HARD, None, None)
        deck = newgame.get_deck()
        self.assertTrue(deck[0].is_same(Card(Suit.SPADE, 1, newgame)))
        self.assertEqual(deck[-1].to_string(),
                         Card(Suit.CLUB, 10, newgame).to_string())

    def test_card_deck_shuffle(self):
        newgame = Game(Level.EASY, None, None)
        newgame.shuffle()
        deck = newgame.get_deck()
        card_value = 1
        test_ok = False
        for card in deck:
            if card_value == card.value:
                continue
            elif card.value == card_value+1:
                card_value += 1
                continue
            test_ok = True

        self.assertTrue(test_ok)

    def test_card_right_place(self):
        newgame = Game(Level.EASY, None, None)
        newgame.shuffle()
        newgame.place_cards()
        deck = newgame.get_deck()

        self.assertEqual(deck[0].column, 0)
        self.assertEqual(deck[0].row, 0)
        self.assertEqual(deck[-1].column, 4)
        self.assertEqual(deck[-1].row, 3)
        self.assertEqual(deck[0].button_place_x(), 300)
        self.assertEqual(deck[0].button_place_y(), 100)
        self.assertEqual(deck[-1].button_place_x(), 285*4+300)
        self.assertEqual(deck[-1].button_place_y(), 200*3+100)

        newgame = Game(Level.HARD, None, None)
        newgame.shuffle()
        newgame.place_cards()
        deck = newgame.get_deck()

        self.assertEqual(deck[0].column, 0)
        self.assertEqual(deck[0].row, 0)
        self.assertEqual(deck[-1].column, 9)
        self.assertEqual(deck[-1].row, 3)
        self.assertEqual(deck[0].button_place_x(), 50)
        self.assertEqual(deck[0].button_place_y(), 100)
        self.assertEqual(deck[-1].button_place_x(), 185*9+50)
        self.assertEqual(deck[-1].button_place_y(), 200*3+100)

    def test_check_win(self):
        db_name = "test"
        initialize_database(db_name)
        newgame = Game(Level.EASY, None, db_name)
        newgame.set_timer()
        card1 = Card(Suit.DIAMOND, 1, newgame)
        card2 = Card(Suit.CLUB, 1, newgame)

        newgame.deck = [card1, card2]
        card1.display = True
        card2.display = True
        newgame.find_pairs()
        win = newgame.check_win()

        self.assertTrue(win)
        os.remove("data/teststatistics.db")

    def test_check_not_win(self):
        db_name = "test"
        initialize_database(db_name)
        newgame = Game(Level.EASY, None, db_name)
        newgame.shuffle()
        newgame.place_cards()
        newgame.get_deck()
        win = newgame.check_win()

        self.assertFalse(win)
        os.remove("data/teststatistics.db")
