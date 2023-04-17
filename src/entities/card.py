class Card:
    def __init__(self, suit, value, game):
        self.suit = suit
        self.value = value
        self.display = False
        self.game = game
        self.ui_card = None
        self.column = None
        self.row = None

    def set_button(self, ui_card):
        self.ui_card = ui_card

    def suitname(self):
        return self.suit.name

    def to_string(self):
        return f'{self.suitname()}-{self.value}'

    def is_same(self, card):
        if self.suit == card.suit and self.value == card.value:
            return True
        return False

    def button_place_x(self):
        return 185*self.column+50

    def button_place_y(self):
        return 200*self.row+100

    def set_card_on_table(self, column, row):
        self.column = column
        self.row = row
