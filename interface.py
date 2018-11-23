from tkinter import  *
class Interface(Frame):


    def __init__(self, window):
        Frame.__init__(self, window, width=400, height=400)
        self.pack(fill=BOTH)

        Label(self, text="La leçon de piano".title()).pack(side=TOP)

        self.button_quit = Button(self, text='Quitter', command=self.quit)
        self.button_quit.pack(side=LEFT)