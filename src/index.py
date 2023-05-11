from tkinter import Tk
from ui.ui import UI
from database_initialize import initialize_database
from services.game import Game


def main():
    initialize_database(Game.get_db_name())
    window = Tk()
    window.title("Memory game")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
