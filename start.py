from tkinter import Tk
from tkinter import Label
from tkinter import Button
from entry import EntryWindow
from help import HelpWindow
# from entry import all_inputs


class FishBowlWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title("Fishbowl")
        self.win.geometry("500x500")

        def startEntry():
            entryWindow = EntryWindow()
            entryWindow.start

        def startHelp():
            helpWindow = HelpWindow()
            helpWindow.start

        def exitGame():
            self.popup = Tk()
            label = Label(self.popup, text="Are you sure you want to quit? You can not return to the game.")
            label.pack()
            yes_button = Button(self.popup, text="Yes", command=quitAll)
            yes_button.pack(padx=50, pady=50, side='left')
            no_button = Button(self.popup, text="No", command=self.popup.destroy)
            no_button.pack(padx=50, pady=50, side='right')
            self.popup.mainloop()

        def quitAll():
            self.popup.destroy()
            self.win.destroy()

        start_text = Label(self.win, text="Welcome to Fishbowl!", font=('calibre', 10))
        help_button = Button(self.win, text="Need help?", font=('calibre', 10), command=startHelp)
        play_button = Button(self.win, text="Ready to play?", font=('calibre', 10), command=startEntry)
        exit_button = Button(self.win, text="Exit the game", font=('calibre', 10, 'bold'), command=exitGame)

        start_text.pack()
        play_button.pack(padx=50, pady=25, side='left')
        help_button.pack(padx=50, pady=25, side='right')
        exit_button.pack(side='bottom')

    def start(self):
        self.win.mainloop()
