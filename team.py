from tkinter import Button
from tkinter import Label
from tkinter import Tk
from game import GameWindow


class TeamWindow:
    def __init__(self, inputs):
        self.win = Tk()
        self.win.title("Fisbowl Teams")
        self.win.geometry("500x500")

        def exit_window():
            self.win.destroy()
            game = GameWindow(inputs)
            game.start()

        label = Label(self.win, text="Step 2: Separate into teams!")
        label.pack()

        instruction = Label(self.win, text="Once in teams, you will alternate between players of each team!")
        instruction.pack()

        instruction2 = Label(self.win, text="Example: Player 1 of Team 1, Player 1 of Team 2, Player 2 of Team 1, Player 2 of Team 2...")
        instruction2.pack()

        confirmation = Label(self.win, text="Are you ready to start?")
        confirmation.pack()

        yes_button = Button(self.win, text="Yes", command=exit_window)
        yes_button.pack(padx=50, pady=50, side='left')
        no_button = Button(self.win, text="No")
        no_button.pack(padx=50, pady=50, side='right')

    def start(self):
        self.win.mainloop()