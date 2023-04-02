from enum import Enum

class Card_deck:
    def __init__(self, level):
        self.level=level
        self.deck=[]

    def create_card_deck(self, level):
        self.level=level
        for i in range(1, 11):
            self.deck.append(Card(Suit.spade, i))
            self.deck.append(Card(Suit.diamond, i))
            self.deck.append(Card(Suit.heart, i))
            self.deck.append(Card(Suit.club, i))
    
    def show_deck(self):
        return self.deck

    def print_deck(self):
        for i in self.deck:
    
            print(f'{i.suitname()}-{i.value()} ')

    def shuffle(self):
        shuffled_deck=self.deck.shuffle()
        return shuffled_deck

class Card:
    def __init__(self, suit, value):
        self._suit=suit
        self._value=value
   
    def suit(self):
        return self._suit
    
    def suitname(self):
        return self._suit.name
    
    def value(self):
        return self._value

class Suit(Enum):
    spade=1
    diamond=2
    heart=3
    club=4

   