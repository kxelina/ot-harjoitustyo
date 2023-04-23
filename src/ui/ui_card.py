import tkinter as tk


class UiCard:
    def __init__(self, view, card, game):
        self.view = view
        self.card = card
        self.game = game
        self.card.set_button(self)
       # x = self.to_string()
        image = self.view.backimage
        self.card.button = tk.Button(master=self.view._canvas, image=image,
                                     command=self.handle_cardback, width=100, height=169)
        self.card.button.place(x=self.card.button_place_x(),
                               y=self.card.button_place_y())

        self.card.button.image = image
        # print(f"create card button {x}-{self.display},  {self.button_place_x}-{self.button_place_y}")

    def show_card(self, card):
        image = self.view.create_image(card)
        self.card.button.image = image
        self.card.button.config(image=image)

    def show_cardback(self):
        image = self.view.backimage
        self.card.button.config(image=image)
        print(f"käänän tätä {self.card.to_string()}")

    def handle_cardback(self):
        self.game.turn_card(self.card)
        print("hello, 1-2 käänty")
        self.show_card(self.card)
        print("bye, 1-2 ohi")
        card = self.game.get_visable_cards()
        print(f"kortti näkyuvä:{card}")
        if card != 2:
            return
        same = self.game.check_card()
        if same[0]:
            same[1].button.destroy()
            same[2].button.destroy()
        else:
            print("ei sama, 2, käänä 2 ")
            self.game.turn_card(same[1])
            self.game.turn_card(same[2])
            same[1].ui_card.show_cardback()
            same[2].ui_card.show_cardback()
            # print("bye11")
        self.view.win()
