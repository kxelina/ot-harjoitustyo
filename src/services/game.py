import random
import time
from entities.card import Card
from entities.card_suit import Suit
from repositories.game_statitics_repository import GameStatitics


class Game:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, level, view, db_name):
        """ Luokan konstruktori, joka antaa kortille nämä tiedot.
        Args:
            level: pelin vaikeustaso
            (kertoo, kuinka paljon kortteja menee mille tasolle)
            view : antaa pelinäkymän
            db_name: kertoo pelille tietokannan nimen
        """
        self.level = level
        self.view = view
        self.deck = []
        self.start_time = None
        self.stop_time = None
        self.cards_per_suit = level.cards_per_suit()
        self.db_name = Game.get_db_name()
        if db_name is not None:
            self.db_name = db_name

        self.create_game()

    def get_db_name():
        return "game"

    def set_timer(self):
        self.start_time = time.time()

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
        column = 0
        row = 0
        for card in self.deck:
            card.set_card_on_table(column, row)
            column += 1
            if column == self.cards_per_suit:
                column = 0
                row += 1

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

    def handle_card_turn(self, card):
        """ Kääntää kortin, näyttää kortin, lisää kortit listaan,
        tarkistaa, onko kortit parit ja poistaa kortit, jos on.
        Lopulta katsoo, onko peli suoritettu loppuun.
        """
        if card.display is True:
            return
        card.turn_card()
        self.view.show_card(card)
        cards = self.get_visible_cards()
        if cards != 2:
            return
        self.view.update_screen()
        same = self.find_pairs()
        win = self.check_win()
        time.sleep(0.7)
        if same[0]:
            same[1].card_button.destroy()
            same[2].card_button.destroy()
        else:
            same[1].turn_card()
            same[2].turn_card()
            self.view.show_cardback(same[1])
            self.view.show_cardback(same[2])
        if win:
            self.view.win()

    def check_win(self):
        """ Tarkistaa, että onko peli voitettu eli korttipakka lista on tyhjä 
        ja paluttaa True, jos peli on voitettu. 
        Lopettaa ajastimen, jos peli on loppunut. 
        Lisää repositorioon pelisuoritusajan.
        """
        if not self.get_deck():
            self.stop_time = time.time()
            start_time = self.start_time
            gamestatitics = GameStatitics(self.db_name)
            gamestatitics.add_game_score(
                self.level, self.stop_time-start_time)
            return True
        return False
