from tkinter import Tk
from tkinter import Label
from tkinter import Button
from entry import EntryWindow
# from entry import all_inputs


class FishBowlWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title("Fishbowl")
        self.win.geometry("500x500")

        def startEntry():
            self.win.destroy
            entryWindow = EntryWindow()
            entryWindow.start

        start_text = Label(self.win, text="Welcome to Fishbowl!",
                           font=('calibre', 10))
        help_button = Button(self.win, text="Need help?",
                             font=('calibre', 10))
        play_button = Button(self.win, text="Ready to play?",
                             font=('calibre', 10), command=startEntry)

        start_text.pack()
        play_button.pack(side='left')
        help_button.pack(side='right')

    def start(self):
        self.win.mainloop()
