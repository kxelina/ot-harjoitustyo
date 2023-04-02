import tkinter as tk
#from src.functionality.card_deck import Card_deck
#from functionality import 
#from functionality.card_deck import Card_deck
from functionality.cards_on_table import Card_deck

class Easy_view:
    def __init__(self, root, handle_welcome):
        self._root = root
        self._root.geometry("1600x950")
        self._window = None
        self._frame = None
        self._handle_welcome= handle_welcome

        self._initialize()

    def _initialize(self):
        self.frame()
        self.window()
        self.button()
        self.create_deck()
       


    def pack(self):
        self._frame.pack(fill=tk.constants.X)
        
    
    def destroy(self):
        self._frame.destroy()

    def frame(self):
        self._frame = tk.Frame(self._root, bg='white',bd=100)
        self._frame.pack(expand=True, fill=tk.BOTH)
        #background=


    def window(self):
        title = tk.Label(master=self._frame, text="Easy mode", font=("Helvetica", 20))
        title.pack()
  

    
    def button(self):
        back= tk.Button(master=self._frame, text="back", bg="pink", fg="white", command=self._handle_welcome)
        back.pack()


    def create_deck(self):
        #card picture=
        new_deck=Card_deck("easy")
        Card_deck.create_card_deck(new_deck, "easy")
        Card_deck.show_deck(new_deck)
        Card_deck.print_deck(new_deck)
        #return deck
        
        
