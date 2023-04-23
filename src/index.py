from tkinter import Tk
from ui.ui import UI
from database_initialize import initialize_database


def main():
    database = initialize_database()
    window = Tk()
    window.title("Memory game")

    ui_view = UI(window, database)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
