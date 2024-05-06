from tkinter import Tk
from tkinter import Text
from tkinter import Scrollbar
from tkinter import RIGHT
from tkinter import Y
from tkinter import LEFT
from tkinter import END


class HelpWindow():
    def __init__(self):
        win = Tk()
        scroll = Scrollbar(win)
        text = Text(win)
        scroll.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, fill=Y)
        win.title("Fishbowl Description")
        win.geometry("500x500")

        description = """Fishbowl is a virtual version of a fun guessing game,
                        \ndesigned for any group of all ages! You'll need at least 4
                        \nto play, but it only gets more fun with more players. There
                        \nare three rounds to play through: Taboo, Charades,
                        \nand Password.
                        \n
                        \nFirst, everyone writes down a few words or phrases in the entry box.
                        \nThe group will then be split into two teams
                        \nPlayers from each team will alternate turns,
                        \ngiving clues to their team to guess as many cards
                        \nEach player will have 1 minute to give clues to their team
                        \n
                        \nThere will be 3 rounds and cards are recycled after each round
                        \n
                        \nRound 1: Taboo. Use words to describe the word/phrase.
                        \nNo acting or gestures!
                        \nRound 2: Charades. Without words or sounds, act and use
                        \ngestures to give clues.
                        \nRound 3: Password. You can say exactly one word as a clue.
                        """

        text.insert(END, description)

    def start(self):
        self.win.mainloop()
