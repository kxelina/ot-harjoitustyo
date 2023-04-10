import tkinter as tk

class Guide_view:
    def __init__(self, root, handle_welcome):
        self._root = root
        self._root.geometry("1000x550")
        self._window = None
        self._frame = None
        self._handle_welcome = handle_welcome

        self._initialize()

    def _initialize(self):
        self.frame()
        self.window()
        self.button()

    def pack(self):
        self._frame.pack(fill=tk.constants.X)

    def destroy(self):
        self._frame.destroy()

    def frame(self):
        self._frame = tk.Frame(self._root, bg='white', bd=100)
        self._frame.pack(expand=True, fill=tk.BOTH)

    def window(self):
        title = tk.Label(master=self._frame, text="How to play",
                         font=("Helvetica", 20))
        title.pack()

    def button(self):
        back = tk.Button(master=self._frame, text="back",
                         bg="pink", fg="white", command=self._handle_welcome)
        back.pack()