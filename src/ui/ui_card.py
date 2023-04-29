import tkinter as tk
import time


class UiCard:
    def __init__(self, view, card, game):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.
        Args:
            view: merkkijonoarvo, kertoo kortille näkymän.
            card: merkkijonoarvo, kertoo kortille kortin tiedot.
            game: merkkijonoarvo, kertoo kortille pelin.
        funktio:
            set_button: luo kortille nappulan ja kertoo sille sen paikan
        """
        self.view = view
        self.card = card
        self.game = game
        self.card.set_button(self)
        image = self.view.backimage
        self.card.button = tk.Button(master=self.view._canvas, image=image,
                                     command=self.handle_cardback, width=100, height=169)
        self.card.button.place(x=self.card.button_place_x(),
                               y=self.card.button_place_y())

        self.card.button.image = image

    def show_card(self, card):
        """ Näyttää kortin. """
        image = self.view.create_image(card)
        self.card.button.image = image
        self.card.button.config(image=image)

    def show_cardback(self):
        """ Näyttää kortin takapuolen."""
        image = self.view.backimage
        self.card.button.config(image=image)

    def handle_cardback(self):
        """ Kääntää kortin, näyttää kortin, lisää kortit listaan, tarkistaa, onko kortit parit ja poistaa kortit, jos on.
        Lopulta katsoo, onko peli suoritettu loppuun.
        """
        self.game.turn_card(self.card)
        self.show_card(self.card)
        card = self.game.get_visible_cards()
        if card != 2:
            return
        self.view._root.update()
        time.sleep(0.7)
        same = self.game.find_pairs()
        if same[0]:
            same[1].button.destroy()
            same[2].button.destroy()
        else:
            self.game.turn_card(same[1])
            self.game.turn_card(same[2])
            same[1].ui_card.show_cardback()
            same[2].ui_card.show_cardback()
        self.view.win()
