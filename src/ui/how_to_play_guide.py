import tkinter as tk


class Guide_view:
    """ Peliohjeen näkymä."""

    def __init__(self, root, handle_welcome):
        """ Luokan kontruktori. Luo pelinäkymän.
        Args:
            root: Tkinter-elementti, joka alustaa peliohjeen näkymän.
            frame: Tkinter-elementti, jonka oletusarvo on None.
            handle_welcome: kutsuttava arvo, jota kutsutaan kun palataan takaisin etusivulle.
        """
        self._root = root
        self._root.geometry("1000x550")
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
        self._frame = tk.Frame(self._root, bg='pink', bd=100)
        self._frame.pack(expand=True, fill=tk.BOTH)

    def label(self):
        """ Luo näkymän otsikon. """
        title = tk.Label(master=self._frame, text="How to play",
                         font=("Times New Roman", 65), bg="pink", fg="pale violet red")
        title.pack()

    def button(self):
        """ Luo nappulan, jotta pääse takaisin etusivulle. """
        button_border = tk.Frame(self._frame, highlightbackground="pale violet red",
                                 highlightthickness=3, bd=0)
        back = tk.Button(button_border, text="Back",
                         bg="peach puff", fg="pale violet red", command=self._handle_welcome, font=("Times New Roman", 35))
        back.pack()
        button_border.pack(pady=20)

    def textbox(self):
        """ Luo teksilaatikon, jossa on pelinohjeet. """
        text = ''' Easy Mode: 
        - There are 40 cards in total
        - You have to find the pairs that have the same number
        - You can click on two cards at a time and memorise them 
        - Match the pairs of cards in as few moves as possible
        '''
        textBox = tk.Text(master=self._frame, height=100, width=100, font=(
            "Times New Roman", 40), bg="peach puff")
        textBox.insert("end", text)
        textBox.config(state='disabled')
        textBox.pack(expand=True)
