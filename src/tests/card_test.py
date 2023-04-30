import unittest
from services.game import Game
from entities.card import Card
from entities.card_suit import Suit
from entities.game_level import Level


class TestCard(unittest.TestCase):
    def test_find_pairs_are_same(self):
        newgame = Game(Level.EASY)

        card1 = Card(Suit.SPADE, 1, newgame)
        card2 = Card(Suit.DIAMOND, 1, newgame)

        newgame.deck = [card1, card2]
        card1.display = True
        card2.display = True

        newgame.find_pairs()

        self.assertEqual(newgame.deck, [])

        newgame = Game(Level.HARD)

        card1 = Card(Suit.SPADE, 1, newgame)
        card2 = Card(Suit.CLUB, 1, newgame)

        newgame.deck = [card1, card2]
        card1.display = True
        card2.display = True

        newgame.find_pairs()

        self.assertEqual(newgame.deck, [])

    def test_find_pairs_not_same(self):
        newgame = Game(Level.EASY)

        card1 = Card(Suit.SPADE, 2, newgame)
        card2 = Card(Suit.CLUB, 1, newgame)

        newgame.deck = [card1, card2]
        card1.display = True
        card2.display = True

        newgame.find_pairs()

        self.assertEqual(len(newgame.deck), 2)

        newgame = Game(Level.HARD)

        card1 = Card(Suit.DIAMOND, 1, newgame)
        card2 = Card(Suit.CLUB, 1, newgame)

        newgame.deck = [card1, card2]
        card1.display = True
        card2.display = True

        newgame.find_pairs()

        self.assertEqual(len(newgame.deck), 2)

    def test_card_is_same_color(self):
        newgame = Game(Level.EASY)

        card1 = Card(Suit.SPADE, 1, newgame)
        card2 = Card(Suit.CLUB, 1, newgame)

        self.assertEqual(card1.is_same_color(card2), True)

        card1 = Card(Suit.HEART, 1, newgame)
        card2 = Card(Suit.DIAMOND, 1, newgame)

        self.assertEqual(card1.is_same_color(card2), True)

    def test_card_is_not_same_color(self):
        newgame = Game(Level.EASY)

        card1 = Card(Suit.SPADE, 1, newgame)
        card2 = Card(Suit.HEART, 1, newgame)

        self.assertEqual(card1.is_same_color(card2), False)

    def test_check_visible_cards(self):
        newgame = Game(Level.EASY)
        cards = newgame.get_visible_cards()
        self.assertEqual(cards, 0)
        newgame.deck[1].turn_card()
        newgame.deck[5].turn_card()
        cards = newgame.get_visible_cards()
        self.assertEqual(cards, 2)
        newgame.deck[3].turn_card()
        cards = newgame.get_visible_cards()
        self.assertEqual(cards, 3)

    def test_level(self):
        self.assertEqual(Level.EASY.level_to_string(), "Easy")
        self.assertEqual(Level.MEDIUM.level_to_string(), "Medium")
        self.assertEqual(Level.HARD.level_to_string(), "Hard")
