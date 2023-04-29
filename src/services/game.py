import random
from entities.card import Card
from entities.card_suit import Suit


class Game:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, level, root):
        """ Luokan konstruktori, joka antaa kortille nämä tiedot.
        Args:
            level: pelin vaikeustaso
            (kertoo, kuinka paljon kortteja menee mille tasolle)
            root: Ohjelman käyttöliitymän juuri-ikkuna-elementti
        Funktio:
            create_game: luo pelin
        """
        self.level = level
        self.deck = []
        self.start_time = None
        self._root = root
        self.cards_per_suit = level.cards_per_suit()

        self.create_game()

    def create_game(self):
        """ Luo pelille kortit eli lisää kortit korttipakkaan. """
        for i in range(1, self.cards_per_suit+1):
            self.deck.append(Card(Suit.SPADE, i, self))
            self.deck.append(Card(Suit.DIAMOND, i, self))
            self.deck.append(Card(Suit.HEART, i, self))
            self.deck.append(Card(Suit.CLUB, i, self))

    def get_deck(self):
        """ Palauttaa korttipakan. """
        return self.deck

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
        visible_list = []
        card_counter = 0
        index_list = []
        for card in self.deck:
            if card.display is True:
                visible_list.append(card)
                index_list.append(card_counter)
                if len(visible_list) == 2:
                    break
            card_counter += 1

        same = visible_list[0].is_same(visible_list[1])
        if same:
            self.turn_card(visible_list[0])
            self.turn_card(visible_list[1])
            card = self.deck.pop(index_list[1])
            card = self.deck.pop(index_list[0])

        return (same, visible_list[0], visible_list[1])

    def get_visible_cards(self):
        """ Lisää valitut kortit listaan. 
        Returns:
            Palauttaa listan pituuden.
        """
        visible_list = []
        for card in self.deck:
            if card.display is True:
                visible_list.append(card)
        return len(visible_list)

    def turn_card(self, card):
        """ Kääntää kortin. """
        card.display = not card.display
