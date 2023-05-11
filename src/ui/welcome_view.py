import tkinter as tk
from PIL import Image, ImageTk
from entities.game_level import Level
from repositories.game_statitics_repository import GameStatitics
from services.game import Game


class Welcome_view:
    "Kun peli avataan, niin siitä aukeava näkymä"

    def __init__(self, root, handle_game_instruction, ui):
        """ Luokan kontruktori. Luo pelinäkymän.
        Args:
            root: Tkinter-elementti, joka alustaa pelinäkymän.
            handle_game_instruction: kutsuttava arvo, jota kutsutaan kun halutaan peliohjeen näkymälle.
            ui: merkkijonoarvo, joka kertoo ui luokan.
        """
        self._root = root
        self._root.attributes("-fullscreen", True)
        self._handle_game_instruction = handle_game_instruction
        self.ui = ui

        self._initialize()

    def _initialize(self):
        self.background = self._background()
        self._frame()
        self._title()
        self._game_button()
        self._game_instruction_button()
        self._show_top_five_score()
        self._quit_frame()
        self._quit_button()

    def _handle_game_easy(self):
        """ Näyttää pelin easy tason näkymän. """
        self.ui._show_game_view(Level.EASY)

    def _handle_game_medium(self):
        """ Näyttää pelin medium tason näkymän. """
        self.ui._show_game_view(Level.MEDIUM)

    def _handle_game_hard(self):
        """ Näyttää pelin hard tason näkymän. """
        self.ui._show_game_view(Level.HARD)

    def handle_quit(self):
        """ Poistaa ui näkymän. """
        self.ui.quit()

    def pack(self):
        """ Näyttää näkymän taustan. """
        self._frame.pack()
        self._quit_frame.pack()

    def destroy(self):
        """ Poistaa näkymän taustan."""
        self._frame.destroy()
        self._quit_frame.destroy()

    def _background(self):
        """ Luo taustakuvan pelin etusivulle.
        Returns:
            Palauttaa taustakuvan.
        """
        bg = Image.open(f"./src/images/background.png")
        self._root.update()
        geometry_width = self._root.winfo_width()
        geometry_height = self._root.winfo_height()
        bg = bg.resize((geometry_width, geometry_height))
        bg = ImageTk.PhotoImage(bg)
        label = tk.Label(self._root, image=bg)
        label.place(x=0, y=0)
        return bg

    def _frame(self):
        """ Luo taustalaatikon."""
        self._frame = tk.Frame(self._root, bg='light goldenrod yellow', bd=20)
        self._frame.pack(padx=30, pady=40, anchor="ne")

    def _quit_frame(self):
        """ Luo taustalaatikon quit nappulalle."""
        self._quit_frame = tk.Frame(self._root, bg='steelblue', bd=1)
        self._quit_frame.pack(padx=10, pady=100, anchor="sw")

    def _title(self):
        """ Luo otsikon."""
        welcome = tk.Label(
            master=self._frame, text="Welcome to memory game", font=("Times New Roman", 55), bg="light goldenrod yellow", fg="steelblue")
        welcome.pack()

    def _game_button(self):
        """ Luo nappulan, jolla pääsee pelamaan peliä easy, medium ja hard modessa."""
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

    def _game_instruction_button(self):
        """Luo nappulan, jolla pääsee peliohjenäkymään."""
        button_border = tk.Frame(self._frame, highlightbackground="steelblue",
                                 highlightthickness=3, bd=0)
        instructions_label = tk.Button(
            button_border, text="Game Instructions", font=("Times New Roman", 25), command=self._handle_game_instruction, bg="pink", fg="steelblue")
        instructions_label.pack()
        button_border.pack(pady=10)

    def _quit_button(self):
        """Luo nappulan, joka lopettaa pelin."""
        button_border = tk.Frame(self._quit_frame, highlightbackground="steelblue",
                                 highlightthickness=3, bd=0)
        quit_label = tk.Button(
            button_border, text="Quit Game", font=("Times New Roman", 40), command=self.handle_quit, bg="pink", fg="steelblue", pady=10)
        quit_label.pack()
        button_border.pack(padx=10, pady=5, anchor="se")

    def _show_top_five_score(self):
        """ Näyttää 5 parasta pelin suoritusaikaa."""
        gamestatitics = GameStatitics(Game.get_db_name())
        list = gamestatitics.get_best_score()
        top5 = [
            f"score: {round(i[0],2)} s, {Level(i[1]).level_to_string()}" for i in list]
        str = "\n".join(top5)
        score = tk.Label(
            master=self._frame, text=f"Here are top five score:\n{str}", font=("Times New Roman", 25), bg="light goldenrod yellow", fg="steelblue")
        score.pack(pady=10)
