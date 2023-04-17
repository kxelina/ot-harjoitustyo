from ui.welcome_view import Welcome_view
from ui.game_view import Game_view
from ui.how_to_play_guide import Guide_view


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

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
            self._handle_game,
            self._handle_how_to_play

        )
        self._current_view.pack()

    def _handle_game(self):
        self._show_game_view("easy")

    def _handle_welcome(self):
        self._show_welcome_view()

    def _handle_how_to_play(self):
        self._show_how_to_play_guide_view()

    def _show_game_view(self, mode):
        self._hide_current_view()

        self._current_view = Game_view(
            self._root,
            self._handle_welcome,
            mode

        )

        # self._current_view.pack()

    def _show_how_to_play_guide_view(self):
        self._hide_current_view()

        self._current_view = Guide_view(
            self._root,
            self._handle_welcome
        )

      #  self._current_view.pack()
