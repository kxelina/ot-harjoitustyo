import tkinter as tk


class UiCard:
    def __init__(self, view, card, game):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.
        Args:
            view: merkkijonoarvo, kertoo kortille näkymän.
            card: merkkijonoarvo, kertoo kortille kortin tiedot.
            game: merkkijonoarvo, kertoo kortille pelin.
        """
        self.view = view
        self.card = card
        self.game = game
        self.card.set_button(self)
        image = self.view.backimage
        self.card.button = tk.Button(master=self.view._canvas, image=image,
                                     command=self.click_card, width=100, height=169)
        self.card.button.place(x=self.card.button_place_x(),
                               y=self.card.button_place_y())

        self.card.button.image = image

    def show_card(self):
        """ Näyttää kortin. """
        image = self.view.create_image(self.card)
        self.card.button.image = image
        self.card.button.config(image=image)

    def show_cardback(self):
        """ Näyttää kortin takapuolen."""
        image = self.view.backimage
        self.card.button.config(image=image)

    def click_card(self):
        """ Kun pelaaja painaa korttia, niin menee sovelluslogikkaan."""
        self.game.handle_cardback(self)
