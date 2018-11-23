from tkinter import *


class Interface(Frame):

    def __init__(self, window):
        Frame.__init__(self, window, width=400, height=400)
        self.pack(fill=BOTH)

        Label(self, text="La leçon de piano".title()).pack(side=TOP, pady=20)

        self.button_quit = Button(self, text='Quitter', command=self.quit)
        self.button_quit.pack(side=LEFT, padx=20, pady=20)

        self.button = Button(self, text='coucou', command=self.update)
        self.button.pack(side=RIGHT, padx=20, pady=20)
