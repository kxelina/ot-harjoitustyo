import random
import time
from entities.card import Card
from entities.card_suit import Suit


class Game:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, level):
        """ Luokan konstruktori, joka antaa kortille nämä tiedot.
        Args:
            level: pelin vaikeustaso
            (kertoo, kuinka paljon kortteja menee mille tasolle)
        """
        self.level = level
        self.deck = []
        self.start_time = None
        self.stop_time = None
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
            visible_list[0].turn_card()
            visible_list[1].turn_card()
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

    def handle_cardback(self, card):
        """ Kääntää kortin, näyttää kortin, lisää kortit listaan,
        tarkistaa, onko kortit parit ja poistaa kortit, jos on.
        Lopulta katsoo, onko peli suoritettu loppuun.
        """
        if card.card.display is True:
            return
        card.card.turn_card()
        card.show_card()
        cards = self.get_visible_cards()
        if cards != 2:
            return
        card.view.update_screen()
        time.sleep(0.7)
        same = self.find_pairs()
        if same[0]:
            same[1].button.destroy()
            same[2].button.destroy()
        else:
            same[1].turn_card()
            same[2].turn_card()
            same[1].ui_card.show_cardback()
            same[2].ui_card.show_cardback()

        self.win(card.view)

    def win(self, view):
        """ Tarkistaa, että onko peli voitettu eli korttipakka lista on tyhjä. 
        Lopettaa ajastimen, jos peli on loppunut. 
        Lisää repositorioon pelisuoritusajan.
        """
        if len(self.get_deck()) == 0:
            self.stop_time = time.time()
            start_time = self.start_time
            view.ui.gamestatitics.add_game_score(
                self.level, self.stop_time-start_time)

            view.win()
