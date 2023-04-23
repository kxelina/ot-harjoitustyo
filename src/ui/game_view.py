import tkinter as tk
import time
from PIL import Image, ImageTk
from services.game import Game
from ui.ui_card import UiCard


class Game_view:
    def __init__(self, root, handle_welcome, mode, ui):
        self._root = root
        self._root.geometry("1600x950")
        self._canvas = None
        self._handle_welcome = handle_welcome
        self._mode = mode
        self.stop_time = None
        self.backimage = self.create_back_image()
        self.game = Game(mode, self._root)
        self.ui = ui

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
                         font=("Times New Roman", 40), bg="white", fg="light sea green")
        title.pack(pady=10)

    def button(self):
        self.back = tk.Button(master=self._canvas, text="Quit Game",
                              bg="light sea green", fg="white", command=self._handle_welcome, font=("Times New Roman", 30))
        self.back.pack(side="bottom", pady=30)

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
        Game.debug_print_deck(self.game)
        Game.shuffle(self.game)
        Game.place_cards(self.game)
        for card in self.game.deck:
            UiCard(self, card, self.game)

        self.game.start_time = time.time()
        self.show_time()

    def show_time(self):
        self.label = tk.Label(master=self._canvas, text="time:", font=(
            "Times New Roman", 35), bg="white", fg="light sea green",)
        self.label.place(x=1600-30, y=950-30)

        self.update_time()

    def update_time(self):
        if self.stop_time == None:
            curr_time = time.time()
        else:
            curr_time = self.stop_time
        start_time = self.game.start_time
        time_render = round(curr_time-start_time, 1)
        time_label = f"{time_render} s"
        self.label.config(text=f"Timer: {time_label}")
        if self.stop_time == None:
            self.update = self.label.after(200, self.update_time)

    def win(self):
        print("check win")
        if len(self.game.deck) == 0:
            label = tk.Label(master=self._canvas, text="CONGRATULATIONS<3", font=(
                "Times New Roman", 80), bg="white", fg="light sea green")
            label.pack(pady=350)
            print("win")
            self.back.config(text="Back to menu")

            self.stop_time = time.time()
            start_time = self.game.start_time
            self.label.after_cancel(self.update)
           # print(f"aika:{self.stop_time-start_time} s")
            self.ui.gamestatitics.add_game_score(
                self._mode, self.stop_time-start_time)
