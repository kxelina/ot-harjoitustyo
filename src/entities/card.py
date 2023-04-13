import tkinter as tk
from PIL import Image, ImageTk


class Card:
    def __init__(self, suit, value, view, game):
        self.suit = suit
        self.value = value
        self.display = False
        self.view = view
        self.game = game

    def suitname(self):
        return self.suit.name

    def to_string(self):
        return f'{self.suitname()}-{self.value}'

    def is_same(self, card):
        if self.suit == card.suit and self.value == card.value:
            return True
        return False

    def handle_cardback(self):
        self.turn_card()
        self.game.check_card()
        self.game.win()

    def card_filename(self):
        if self.display is False:
            return "back.png"
        else:
            return f'{self.suitname().lower()}-{self.value}.png'

    def card_button_place(self, x, y):
        self.button_place_x = x
        self.button_place_y = y

    def create_button(self):
        x = self.to_string()
        image = self.create_image()
        self.button = tk.Button(master=self.view._canvas, image=image,
                                command=self.handle_cardback, width=100, height=169)
        self.button.place(x=self.button_place_x, y=self.button_place_y)

        self.button.image = image
        print(
            f"create card button {x}-{self.display},  {self.button_place_x}-{self.button_place_y}")

    def show_card(self):
        image = self.create_image()
        self.button.image = image
        self.button.config(image=image)

    def create_image(self):
        image = Image.open(f"./src/images/cards/{self.card_filename()}")
        print(f'filename {self.card_filename()}')
        image = image.resize((100, 169))  # 667, 1024
        image = ImageTk.PhotoImage(image)

        return image

    # UI

    def turn_card(self):
        print(f"card is turned{self.display}")
        if self.display is False:
            self.display = True
            print(f"käänty{self.display}")
            self.game.counter += 1
            self.game.show_counter()

        else:
            self.display = False
            print(f"käänty2{self.display}")
            self.game.show_counter()

        self.show_card()
