import random
import time
from entities.card import Card
from entities.card_suit import Suit


class Game:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, level, root):
        """ Luokan konstruktori, joka antaa kortille nämä tiedot.
        Args:
            level: merkkijonoarvo, 
            joka kertoo pelin tason (kertoo, kuinka paljon kortteja menee mille tasolle)
            deck: tyhjä lista, luo korttipakalle tyhjän listan
            start_time: oletusarvoltaan None.
            aloittaa pelisuorituksen ajan
            root: merkkijonoarvo, kertoo pelille käyttöliittymän (ikkuna)
        Funktio:
            create_game: luo pelin
        """
        self.level = level
        self.deck = []
        self.start_time = None
        self._root = root
        if level == "easy":
            self.cards_per_suit = 10  # 10

        self.create_game()

    def create_game(self):
        """ Luo pelille kortit eli lisää kortit korttipakkaan. """
        for i in range(1, self.cards_per_suit+1):
            self.deck.append(Card(Suit.SPADE, i, self))
            self.deck.append(Card(Suit.DIAMOND, i, self))
            self.deck.append(Card(Suit.HEART, i, self))
            self.deck.append(Card(Suit.CLUB, i, self))

    def show_deck(self):
        """ Palauttaa korttipakan. """
        return self.deck

    def debug_print_deck(self):
        for i in self.deck:
            print(i.to_string())

    def shuffle(self):
        """ Sekoittaa korttien järjestystä. """
        random.shuffle(self.deck)

    def place_cards(self):
        """ Laittaa kortit käyttöliittymässä oikeisiin paikkoihin. """
        counter = 1
        column = 0
        row = 0
        for card in self.deck:
            card.set_card_on_table(column, row)
            column += 1
            if counter == self.cards_per_suit:
                counter = 0
                column = 0
                row += 1
            counter += 1

    def find_pairs(self):
        """ Etsii valituista korteista parit. 
        Returns:
            Palauttaa same: Boolea-arvon (oletusarvona False), 
            joka kertoo, onko kortit samat, jos on samat (True).
            Palauttaa myös niiden korttien tiedot.
        """
        print("finpairs")
        visable_list = []
        card_counter = 0
        index_list = []
        same = False
        for card in self.deck:
            if card.display is True:
                visable_list.append(card)
                index_list.append(card_counter)
                print(f"hello:{card.to_string()}, {card_counter}")
                if len(visable_list) == 2:
                    break
            card_counter += 1

        if visable_list[0].value == visable_list[1].value:
            same = True
            self.turn_card(visable_list[0])
            self.turn_card(visable_list[1])
            card = self.deck.pop(index_list[1])
            card = self.deck.pop(index_list[0])

       # if self.level == "medium":

        return (same, visable_list[0], visable_list[1])

    def check_card(self):
        """ Päivittää käyttöliittymän näkymän ja kutsuu find_pairs funktiota. 
        Returns:
            Palauttaa find_pairs funktion arvon.
        """
        self._root.update()
        time.sleep(0.7)
        print("onko sama")
        same = self.find_pairs()

        return same

    def get_visable_cards(self):
        """ Lisää valitut kortit listaan. 
        Returns:
            Palauttaa listan pituuden.
        """
        visable_list = []
        for card in self.deck:
            if card.display is True:
                visable_list.append(card)
        return len(visable_list)

    def turn_card(self, card):
        """ Kääntää kortin. """
        print(f"card is turned{card.display}")
        card.display = not card.display
