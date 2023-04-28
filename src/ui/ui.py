from ui.welcome_view import Welcome_view
from ui.game_view import Game_view
from ui.how_to_play_guide import Guide_view
from repositories.game_statitics_repository import GameStatitics



class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root, db):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.
        Args:
            root: TKinter-elementti, joka alustaa käyttöliittymän näkymän.
            current_view: nykyinen ikkuna, oletusarvoltaan None
            gamestatitics: class GameStatitics, yhdistyy repositorioon
        """
        self._root = root
        self._current_view = None
        self.gamestatitics = GameStatitics(db)

    def start(self):
        self._show_welcome_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_welcome_view(self):
        self._hide_current_view()

        self._current_view = Welcome_view(
            self._root,
            self._handle_game_instruction,
            self

        )
        self._current_view.pack()


    def _handle_welcome(self):
        self._show_welcome_view()

    def _handle_game_instruction(self):
        self._show_how_to_play_guide_view()

    def _show_game_view(self, level):
        self._hide_current_view()

        self._current_view = Game_view(
            self._root,
            self._handle_welcome,
            level,
            self

        )

        # self._current_view.pack()

    def _show_how_to_play_guide_view(self):
        self._hide_current_view()

        self._current_view = Guide_view(
            self._root,
            self._handle_welcome
        )

      #  self._current_view.pack()
