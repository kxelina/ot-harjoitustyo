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
        self.label()
        self.button()
        self.textbox()

    def pack(self):
        self._frame.pack(fill=tk.constants.X)

    def destroy(self):
        self._frame.destroy()

    def frame(self):
        self._frame = tk.Frame(self._root, bg='white', bd=100)
        self._frame.pack(expand=True, fill=tk.BOTH)

    def label(self):
        title = tk.Label(master=self._frame, text="How to play",
                         font=("Helvetica", 20))
        title.pack()

    def button(self):
        back = tk.Button(master=self._frame, text="back",
                         bg="pink", fg="white", command=self._handle_welcome)
        back.pack()

    def textbox(self):
        text = ''' Easy Mode: 
        - There are 40 cards in total
        - You have to find the pairs that have the same number
        - You can click on two cards at a time and memorise them 
        '''
        textBox = tk.Text(master=self._frame, height=100, width=100)
        textBox.insert("end", text)
        textBox.config(state='disabled')
        textBox.pack(expand=True)
