from enum import Enum
import random

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

    def debug_print_deck(self):
        for i in self.deck:
            
            print(i.to_string())

    def shuffle(self):
        random.shuffle(self.deck)
        

class Card:
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value
   
    
    def suitname(self):
        return self.suit.name
    
    
    def to_string(self):
        return f'{self.suitname()}-{self.value}'
    
    def is_same(self, card):
        if self.suit == card.suit and self.value == card.value:
            return True
        return False

class Suit(Enum):
    spade=1
    diamond=2
    heart=3
    club=4

   