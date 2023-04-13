import tkinter as tk
import random
import time
from entities.card import Card
from entities.card_suit import Suit


class Game:
    def __init__(self, level, root):
        self.level = level
        self.deck = []
        self.counter = 0
        self._root = root
        self.start_time = None

    def create_game(self, level, view):
        self.level = level
        if level == "easy":
            self.cards_per_suit = 10  # 10
        for i in range(1, self.cards_per_suit+1):
            self.deck.append(Card(Suit.SPADE, i, view, self))
            self.deck.append(Card(Suit.DIAMOND, i, view, self))
            self.deck.append(Card(Suit.HEART, i, view, self))
            self.deck.append(Card(Suit.CLUB, i, view, self))

    def show_deck(self):
        return self.deck

    def debug_print_deck(self):
        for i in self.deck:

            print(i.to_string())

    def shuffle(self):
        random.shuffle(self.deck)

    def place_cards(self):
        counter = 1
        x = 50
        y = 100
        for card in self.deck:
            card.card_button_place(x, y)
            print(f"button2:{x}- {y}-  {card.to_string()}")
            x += 185
            if counter == self.cards_per_suit:
                counter = 0
                x = 50
                y += 200
                print(f"button3:{x}- {y}")
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
                    print(visable_list[0], visable_list[1])
                    if visable_list[0].value == visable_list[1].value:
                        same = True
                        print("same")
                        break

                    print("ei ole sama")
                    visable_list[0].turn_card()
                    visable_list[1].turn_card()
                    break

            card_counter += 1
            print(f"{card_counter}-{card.to_string()}")

        if same is True:
            card = self.deck.pop(index_list[1])
            print(f"posito:{index_list[1]}-{card.to_string()}")
            card.button.destroy()
            card = self.deck.pop(index_list[0])
            card.button.destroy()
            print(f"posito:{index_list[0]}-{card.to_string()}")
        print(f"finpairs{len(visable_list)}, {index_list[:]}, {card_counter}")

    def check_card(self):
        if self.counter == 2:
            self._root.update()
            time.sleep(0.7)
            print("onko sama")
            self.find_pairs()
            self.counter = 0

    def show_counter(self):
        print(f"laskuri={self.counter}")

    def win(self):
        print("check win")
        if len(self.deck) == 0:
            label = tk.Label(master=self._root, text="WIN")
            label.pack()
            print("win")

            stop_time = time.time()
            start_time = self.start_time
            print(f"aika:{stop_time-start_time} s")
            # win is not on root

    def show_time(self):
        self.label = tk.Label(master=self._root, text="time:")
        self.label.pack()
        self.update_time()

    def update_time(self):
        curr_time = time.time()
        start_time = self.start_time
        time_label = f"{curr_time-start_time} s"
        self.label.config(text=f"time:{time_label}")
        self.label.after(200, self.update_time)

        # if win: stop timer
        # timer is not on root
