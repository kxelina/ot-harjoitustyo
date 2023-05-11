import tkinter as tk
import time
from PIL import Image, ImageTk
from services.game import Game
from entities.game_level import Level


class Game_view:
    """ Pelinäkymä."""

    def __init__(self, root, handle_welcome, level, ui):
        """ Luokan kontruktori. Luo pelinäkymän.
        Args:
            root: Tkinter-elementti, joka alustaa pelinäkymän.
            handle_welcome: kutsuttava arvo, jota kutsutaan kun palataan takaisin etusivulle.
            level: Enum level, joka kertoo pelin tason.
            ui: merkkijonoarvo, joka kertoo ui luokan.
        """
        self._root = root
        self._handle_welcome = handle_welcome
        self._backimage = self._create_back_image()
        self.game = Game(level, self, None)
        self.ui = ui

        self._initialize()

    def _initialize(self):
        self._canvas()
        self._label()
        self._create_quit_game_button()
        self._create_deck()
        self._create_timer()

    def destroy(self):
        """Poistaa näkymän. """
        self._canvas.destroy()

    def _canvas(self):
        """Luo näkymän taustan."""
        self._canvas = tk.Canvas(
            master=self._root, bg='white', width=1600, height=950)
        self._canvas.pack(expand=True, fill=tk.BOTH)

    def _label(self):
        """Luo näkymän otsikon."""
        if self.game.level == Level.EASY:
            text = "Easy Level"
        elif self.game.level == Level.MEDIUM:
            text = "Medium Level"
        else:
            text = "Hard Level"
        title = tk.Label(master=self._canvas, text=text,
                         font=("Times New Roman", 40), bg="white", fg="light sea green")
        title.pack(pady=10)

    def _create_quit_game_button(self):
        """Luo nappulan, jotta voi palata pelin etusivulle."""
        self.back = tk.Button(master=self._canvas, text="Quit Game",
                              bg="light sea green", fg="white", command=self._handle_welcome, font=("Times New Roman", 30))
        self.back.pack(side="bottom", pady=30)

    def _create_card_button(self, card):
        """Luo kortille nappulan. """
        image = self._backimage
        card_button = tk.Button(master=self._canvas, image=image,
                                command=card.click_card, width=100, height=169)
        card_button.place(x=card.button_place_x(),
                          y=card.button_place_y())

        card_button.image = image
        card.set_button(card_button)

    def show_card(self, card):
        """Näyttää kortin. """
        image = self._create_image(card)
        card.card_button.image = image
        card.card_button.config(image=image)

    def show_cardback(self, card):
        """ Näyttää kortin takapuolen."""
        image = self._backimage
        card.card_button.config(image=image)

    def _create_image(self, card):
        """ Luo kortille kuvan. 
        Returns:
            Palauttaa kuvan.
        """
        image = Image.open(f"./src/images/cards/{self._card_filename(card)}")
        image = image.resize((100, 169))
        image = ImageTk.PhotoImage(image)

        return image

    def _create_back_image(self):
        """ Luo kortille takapuolikuvan. 
        Returns:
            Palauttaa takapuolikuvan.
        """
        image = Image.open(f"./src/images/cards/back.png")
        image = image.resize((100, 169))
        image = ImageTk.PhotoImage(image)

        return image

    def _card_filename(self, card):
        """
        Returns:
            Palauttaa kortin suit nimen ja kortin arvon eli tiedoston nimen striginä.
        """
        return f'{card.suitname().lower()}-{card.value}.png'

    def _create_deck(self):
        """Luo pelille kortit, sekoittaa niitä, laittaa paikoilleen, aloittaa ajastimen ja näyttää ajastimen."""
        self.game.shuffle()
        self.game.place_cards()
        for card in self.game.get_deck():
            self._create_card_button(card)

        self.game.set_timer()

    def _create_timer(self):
        """Luo ajastimen pelille näkyviin ja kutsuu funktion update_time eli päivittä aikaa."""
        self.label = tk.Label(master=self._canvas, text="time:", font=(
            "Times New Roman", 35), bg="white", fg="light sea green",)
        self.label.place(x=1600-30, y=950-30)

        self._update_time()

    def _time_render(self, desimals):
        """Renderöi ajastinta."""
        if self.game.stop_time == None:
            curr_time = time.time()
        else:
            curr_time = self.game.stop_time
        start_time = self.game.start_time
        time_render = round(curr_time-start_time, desimals)
        time_label = f"{time_render} s"
        self.label.config(text=f"Timer: {time_label}")

    def _update_time(self):
        """Päivittä aikaa ajastimelle."""
        self._time_render(1)
        if self.game.stop_time == None:
            self.update = self.label.after(200, self._update_time)

    def update_screen(self):
        """Päivittä näytön."""
        self._root.update()

    def win(self):
        """Luo onnittelu teksin ja vaihtaa nappulassa olevan tekstin voiton jälkeen."""
        label = tk.Label(master=self._canvas, text="CONGRATULATIONS<3", font=(
            "Times New Roman", 80), bg="white", fg="light sea green")
        label.pack(pady=350)
        self.back.config(text="Back to menu")
        self._time_render(2)
        self.label.after_cancel(self._update_time)
