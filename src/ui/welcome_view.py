import tkinter as tk
from PIL import Image, ImageTk


class Welcome_view:
    "Kun peli avataan, niin siitä aukeava näkymä"

    def __init__(self, root, handle_easy, handle_game_instruction, ui):
        self._root = root
        self._root.geometry("1600x950")
        # self._root.attributes('-fullscreen')
        self._window = None
        self._frame = None
        self._handle_easy = handle_easy
        self._handle_game_instruction = handle_game_instruction
        self.ui = ui

        self._initialize()

    def _initialize(self):
        self.background = self.background()
        self.frame()
        self.title()
        self.game_button()
        self.game_instruction_button()
        self.show_top_five_score()

    def pack(self):
        self._frame.pack()  # fill=tk.constants.X)

    def destroy(self):
        self._frame.destroy()

    def background(self):
        bg = Image.open(f"./src/images/background.png")
        bg = bg.resize((1900, 1020))
        bg = ImageTk.PhotoImage(bg)
        label = tk.Label(self._root, image=bg)
        label.place(x=0, y=0)
        return bg

    def frame(self):
        self._frame = tk.Frame(self._root, bg='light goldenrod yellow', bd=20)
        # height=600, width= 150)#expand=True) #fill=tk.BOTH)
        self._frame.pack(padx=30, pady=40, anchor="ne")

    def title(self):
        welcome = tk.Label(
            master=self._frame, text="Welcome to memory game", font=("Times New Roman", 55), bg="light goldenrod yellow", fg="steelblue")
        welcome.pack()

    def game_button(self):
        button_border = tk.Frame(self._frame, highlightbackground="steelblue",
                                 highlightthickness=3, bd=0)
        easy = tk.Button(button_border, text="Play Easy",
                         bg="pink", fg="steelblue", command=self._handle_easy, font=("Times New Roman", 30))
        easy.pack()
        button_border.pack(pady=10)

    def game_instruction_button(self):
        button_border = tk.Frame(self._frame, highlightbackground="steelblue",
                                 highlightthickness=3, bd=0)
        instructions_label = tk.Button(
            button_border, text="Game Instructions", font=("Times New Roman", 30), command=self._handle_game_instruction, bg="pink", fg="steelblue")
        instructions_label.pack()
        button_border.pack(pady=10)

    def show_top_five_score(self):
        list = self.ui.gamestatitics.get_best_score()
        print(len(list))
        top5 = [f"score: {round(i[0],2)}, {i[1]}" for i in list]
        str = "\n".join(top5)
        score = tk.Label(
            master=self._frame, text=f"Here are top five score:\n{str}", font=("Times New Roman", 25), bg="light goldenrod yellow", fg="steelblue")
        score.pack(pady=10)
