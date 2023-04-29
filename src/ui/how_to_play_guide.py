import tkinter as tk


class Guide_view:
    """ Peliohjeen näkymä."""

    def __init__(self, root, handle_welcome):
        """ Luokan kontruktori. Luo pelinäkymän.
        Args:
            root: Tkinter-elementti, joka alustaa peliohjeen näkymän.
            handle_welcome: kutsuttava arvo, jota kutsutaan kun palataan takaisin etusivulle.
        """
        self._root = root
        self._frame = None
        self._handle_welcome = handle_welcome

        self._initialize()

    def _initialize(self):
        self.frame()
        self.label()
        self.button()
        self.textbox()

    def pack(self):
        """ Näyttää näkymän. """
        self._frame.pack(fill=tk.constants.X)

    def destroy(self):
        """ Poistaa näkymän."""
        self._frame.destroy()

    def frame(self):
        """ Luo näkymän taustan. """
        self._frame = tk.Frame(self._root, bg='pink', bd=80)
        self._frame.pack(expand=True, fill=tk.BOTH)

    def label(self):
        """ Luo näkymän otsikon. """
        title = tk.Label(master=self._frame, text="How to play",
                         font=("Times New Roman", 55), bg="pink", fg="pale violet red")
        title.pack()

    def button(self):
        """ Luo nappulan, jotta pääse takaisin etusivulle. """
        button_border = tk.Frame(self._frame, highlightbackground="pale violet red",
                                 highlightthickness=3, bd=0)
        back = tk.Button(button_border, text="Back",
                         bg="peach puff", fg="pale violet red", command=self._handle_welcome, font=("Times New Roman", 30))
        back.pack()
        button_border.pack(pady=20)

    def textbox(self):
        """ Luo teksilaatikon, jossa on pelinohjeet. """
        text = ''' 
        The purpose of game: 
        - Match the pairs of cards in as fast as possible
        - You can select two cards at a time
            - if you found a pair, the cards will be discarded
            - if the cards are not a pair, the cards will turn back 
        Easy Level (20 cards): 
        - You have to find the pairs that have the same number
        Medium Level (40 cards):
        - You have to find the pairs that have the same number 
        Hard Level (40 cards):
        - You have to find the pairs that have the same number and same color
        Hint:
        - Try to memorise the cards!
        '''
        textBox = tk.Text(master=self._frame, height=100, width=100, font=(
            "Times New Roman", 27), bg="peach puff")
        textBox.insert("end", text)
        textBox.config(state='disabled')
        textBox.pack(expand=True)
