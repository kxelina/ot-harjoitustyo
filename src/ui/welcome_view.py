import tkinter as tk

class Welcome_view:
    "Kun peli avataan, niin siitä aukeava näkymä"

    def __init__(self, root, handle_easy):
        self._root = root
        self._root.geometry("1600x950")
        self._window = None
        self._frame = None
        self._handle_easy= handle_easy

        self._initialize()

    def _initialize(self):
        self.frame()
        self.window()
        self.button()
        self.how_to_play()


    def pack(self):
        self._frame.pack(fill=tk.constants.X)
        
    
    def destroy(self):
        self._frame.destroy()

    def frame(self):
        self._frame = tk.Frame(self._root, bg='pink', bd=100)
        self._frame.pack(expand=True, fill=tk.BOTH)
        #background= 

    def window(self):
        welcome = tk.Label(master=self._frame, text="Welcome to memory game", font=("Helvetica", 20))
        welcome.pack()
        

    def button(self):
        easy= tk.Button(master=self._frame, text="easy", bg="pink", fg="white", command=self._handle_easy)
        easy.pack()

    def how_to_play(self):
        instructions_label = tk.Button(self._frame, text="How to Play: Match the pairs of cards in as few moves as possible.", font=("Helvetica", 12))
        instructions_label.pack()

