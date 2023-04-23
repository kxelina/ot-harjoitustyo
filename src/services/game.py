import random
import time
from entities.card import Card
from entities.card_suit import Suit


class Game:
    def __init__(self, level, root):
        self.level = level
        self.deck = []
        self.start_time = None
        self._root = root
        if level == "easy":
            self.cards_per_suit = 10  # 10

        self.create_game()

    def create_game(self):
        for i in range(1, self.cards_per_suit+1):
            self.deck.append(Card(Suit.SPADE, i, self))
            self.deck.append(Card(Suit.DIAMOND, i, self))
            self.deck.append(Card(Suit.HEART, i, self))
            self.deck.append(Card(Suit.CLUB, i, self))

    def show_deck(self):
        return self.deck

    def debug_print_deck(self):
        for i in self.deck:
            print(i.to_string())

    def shuffle(self):
        random.shuffle(self.deck)

    def place_cards(self):
        counter = 1
        column = 0
        row = 0
        for card in self.deck:
            card.set_card_on_table(column, row)
            column += 1
            if counter == self.cards_per_suit:
                counter = 0
                column = 0
                row += 1
            counter += 1

    def find_pairs(self):
        print("finpairs")
        visable_list = []
        card_counter = 0
        index_list = []
        same = False
        for card in self.deck:
            if card.display is True:
                visable_list.append(card)
                index_list.append(card_counter)
                print(f"hello:{card.to_string()}, {card_counter}")
                if len(visable_list) == 2:
                    break
            card_counter += 1

        if visable_list[0].value == visable_list[1].value:
            same = True
            self.turn_card(visable_list[0])
            self.turn_card(visable_list[1])
            card = self.deck.pop(index_list[1])
            card = self.deck.pop(index_list[0])

        return (same, visable_list[0], visable_list[1])

    def check_card(self):
        self._root.update()
        time.sleep(0.7)
        print("onko sama")
        same = self.find_pairs()

        return same

    def get_visable_cards(self):
        visable_list = []
        for card in self.deck:
            if card.display is True:
                visable_list.append(card)
        return len(visable_list)

    def turn_card(self, card):
        print(f"card is turned{card.display}")
        card.display = not card.display
