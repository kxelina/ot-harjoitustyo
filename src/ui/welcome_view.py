import tkinter as tk
from PIL import Image, ImageTk
from entities.game_level import Level


class Welcome_view:
    "Kun peli avataan, niin siitä aukeava näkymä"

    def __init__(self, root, handle_game_instruction, ui):
        """ Luokan kontruktori. Luo pelinäkymän.
        Args:
            root: Tkinter-elementti, joka alustaa pelinäkymän.
            frame: Tkinter-elementti, jonka oletusarvo on None.
            handle_easy: kutsuttava arvo, jota kutsutaan kun halutaan pelinäkymälle easy tasolle.
            handle_game_instruction: kutsuttava arvo, jota kutsutaan kun halutaan peliohjeen näkymälle.
            ui: merkkijonoarvo, joka kertoo ui luokan.
        """
        self._root = root
        self._root.geometry("1600x950")
        self._frame = None
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

    def _handle_game_easy(self):
        self.ui._show_game_view(Level.EASY)

    def _handle_game_medium(self):
        self.ui._show_game_view(Level.MEDIUM)

    def _handle_game_hard(self):
        self.ui._show_game_view(Level.HARD)

    def pack(self):
        """ Näyttää näkymän. """
        self._frame.pack()

    def destroy(self):
        """ Poistaa näkymän."""
        self._frame.destroy()

    def background(self):
        """ Luo taustakuvan pelin etusivulle.
        Returns:
            Palauttaa taustakuvan.
        """
        bg = Image.open(f"./src/images/background.png")
        bg = bg.resize((1900, 1020))
        bg = ImageTk.PhotoImage(bg)
        label = tk.Label(self._root, image=bg)
        label.place(x=0, y=0)
        return bg

    def frame(self):
        """ Luo laatikon."""
        self._frame = tk.Frame(self._root, bg='light goldenrod yellow', bd=20)
        self._frame.pack(padx=30, pady=40, anchor="ne")

    def title(self):
        """ Luo otsikon."""
        welcome = tk.Label(
            master=self._frame, text="Welcome to memory game", font=("Times New Roman", 55), bg="light goldenrod yellow", fg="steelblue")
        welcome.pack()

    def game_button(self):
        """ Luo nappulan, jolla pääsee pelamaan peliä easy modessa."""
        button_border = tk.Frame(self._frame, highlightbackground="steelblue",
                                 highlightthickness=3, bd=0)
        easy = tk.Button(button_border, text="Play Easy",
                         bg="pink", fg="steelblue", command=self._handle_game_easy, font=("Times New Roman", 30))
        m_button_border = tk.Frame(self._frame, highlightbackground="steelblue",
                                   highlightthickness=3, bd=0)
        medium = tk.Button(m_button_border, text="Play Medium",
                           bg="pink", fg="steelblue", command=self._handle_game_medium, font=("Times New Roman", 30))
        h_button_border = tk.Frame(self._frame, highlightbackground="steelblue",
                                   highlightthickness=3, bd=0)
        hard = tk.Button(h_button_border, text="Play Hard",
                         bg="pink", fg="steelblue", command=self._handle_game_hard, font=("Times New Roman", 30))
        easy.pack()
        button_border.pack(pady=10)
        medium.pack()
        m_button_border.pack(pady=10)
        hard.pack()
        h_button_border.pack(pady=10)

    def game_instruction_button(self):
        """Luo nappulan, jolla pääsee peliohjenäkymään."""
        button_border = tk.Frame(self._frame, highlightbackground="steelblue",
                                 highlightthickness=3, bd=0)
        instructions_label = tk.Button(
            button_border, text="Game Instructions", font=("Times New Roman", 25), command=self._handle_game_instruction, bg="pink", fg="steelblue")
        instructions_label.pack()
        button_border.pack(pady=10)

    def show_top_five_score(self):
        """ Näyttää 5 parasta pelin suoritusaikaa."""
        list = self.ui.gamestatitics.get_best_score()
        top5 = [
            f"score: {round(i[0],2)}, {Level(i[1]).level_to_string()}" for i in list]
        str = "\n".join(top5)
        score = tk.Label(
            master=self._frame, text=f"Here are top five score:\n{str}", font=("Times New Roman", 25), bg="light goldenrod yellow", fg="steelblue")
        score.pack(pady=10)
