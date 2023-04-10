import tkinter as tk
import time

from services.cards_on_table import Game, Card


class Easy_view:
    def __init__(self, root, handle_welcome):
        self._root = root
        self._root.geometry("1600x950")
        self._canvas = None
        self._handle_welcome = handle_welcome
        

        self._initialize()

    def _initialize(self):
        self.canvas()
        self.label()
        self.button()
        self.create_deck()

    # def pack(self):
    #      self._canvas.pack(fill=tk.constants.X)

    def destroy(self):
        self._canvas.destroy()

    # def frame(self):
    #     self._frame = tk.Frame(self._root, bg='white', width=1600, height=950)
    #     self._frame.pack(expand=True, fill=tk.BOTH)
    #     # background=
    def canvas(self):
        self._canvas = tk.Canvas(master=self._root, bg='white', width=1600, height=950)
        self._canvas.pack(expand=True, fill=tk.BOTH)
    #     # background=

    def label(self):
        title = tk.Label(master=self._canvas, text="Easy mode",
                         font=("Helvetica", 20))
        title.pack()

    def button(self):
        back = tk.Button(master=self._canvas, text="back",
                         bg="pink", fg="white", command=self._handle_welcome)
        back.place(x=100, y=100)
        back.pack()


    def create_deck(self):
        game = Game("easy", self._root)
        Game.create_game(game, "easy", self)
    
        Game.debug_print_deck(game)
        Game.shuffle(game)
        Game.place_cards(game)
        for card in game.deck:
            Card.create_button(card)
   
        game.start_time=time.time()
        game.show_time()


        
       

