import tkinter as tk
import time
from PIL import Image, ImageTk
from services.game import Game
from ui.ui_card import UiCard


class Game_view:
    def __init__(self, root, handle_welcome, mode):
        self._root = root
        self._root.geometry("1600x950")
        self._canvas = None
        self._handle_welcome = handle_welcome
        self._mode = mode
        self.backimage = self.create_back_image()

        self._initialize()

    def _initialize(self):
        self.canvas()
        self.label()
        self.button()
        self.create_deck()

    def destroy(self):
        self._canvas.destroy()

    def canvas(self):
        self._canvas = tk.Canvas(
            master=self._root, bg='white', width=1600, height=950)
        self._canvas.pack(expand=True, fill=tk.BOTH)

    def label(self):
        title = tk.Label(master=self._canvas, text="Easy mode",
                         font=("Helvetica", 20))
        title.pack()

    def button(self):
        back = tk.Button(master=self._canvas, text="back",
                         bg="pink", fg="white", command=self._handle_welcome)
        back.place(x=100, y=100)
        back.pack()

    def create_image(self, card):
        image = Image.open(f"./src/images/cards/{self.card_filename(card)}")
        print(f'filename {self.card_filename(card)}')
        image = image.resize((100, 169))  # 667, 1024
        image = ImageTk.PhotoImage(image)

        return image

    def create_back_image(self):
        image = Image.open(f"./src/images/cards/back.png")
        image = image.resize((100, 169))  # 667, 1024
        image = ImageTk.PhotoImage(image)

        return image

    def card_filename(self, card):
        return f'{card.suitname().lower()}-{card.value}.png'

    def create_deck(self):
        game = Game("easy", self._root)

        Game.debug_print_deck(game)
        Game.shuffle(game)
        Game.place_cards(game)
        for card in game.deck:
            UiCard(self, card, game)

        game.start_time = time.time()
        # self.show_time()

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
