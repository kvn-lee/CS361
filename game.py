from random import shuffle
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import BOTTOM
from tkinter import BOTH


class GameWindow():
    def __init__(self, inputs):
        self.win = Tk()
        self.win.title("Fishbowl Game")
        self.win.geometry("1500x500")

        self.round = 1
        round_scores = {}
        self.team_turn = 1
        self.team_one = 0
        self.team_two = 0
        self.card = 0
        self.bowl = inputs.copy()
        self.current = self.bowl.pop(self.card)

        shuffle(self.bowl)

        def score():
            if self.team_turn == 1:
                self.team_one += 1
            else:
                self.team_two += 1
            
            shuffle(self.bowl)
            if len(self.bowl) == 0:
                finish_round()
            else:
                self.current = self.bowl.pop(self.card)
                display()

        def switch():
            if self.team_turn == 1:
                self.team_turn = 2
            else:
                self.team_turn = 1

            shuffle(self.bowl)

            display()

        def skip():
            self.bowl.append(self.current)
            self.current = self.bowl.pop(self.card)
            switch()

        def display():
            self.round_label.destroy()
            self.team_label.destroy()
            self.game_label.destroy()
            self.description_label.destroy()
            self.team_one_point_label.destroy()
            self.team_two_point_label.destroy()

            self.team_label = Label(self.win, text="It is Team " + str(self.team_turn) + "'s turn!")
            self.game_label = Label(self.win, text="Your word is: " + self.current)
            self.round_label = Label(self.win, text="Round " + str(self.round))
            self.team_one_point_label = Label(self.win, text="Team 1 Points: " + str(self.team_one))
            self.team_two_point_label = Label(self.win, text="Team 2 Points: " + str(self.team_two))

            match self.round:
                case 1:
                    self.description_label = Label(self.win, text="Taboo. Use words to describe the word/phrase. No acting or gestures!")
                case 2:
                    self.description_label = Label(self.win, text="Charades. Act and use gestures to give clues. No words or sounds!")
                case 3:
                    self.description_label = Label(self.win, text="Password. Say exactly ONE word as a clue.")
                case _:
                    self.done_label.pack()

            self.round_label.pack()
            self.team_label.pack()
            self.game_label.pack()
            self.description_label.pack()
            self.team_one_point_label.pack(side=LEFT, fill=BOTH)
            self.team_two_point_label.pack(side=RIGHT, fill=BOTH)

            score_button.pack(side=RIGHT, fill=BOTH)
            skip_button.pack(side=LEFT, fill=BOTH)

            switch_player.pack(side=BOTTOM)

        def finish_round():
            display()
            self.round += 1
            if self.round == 4:
                self.done_label.pack()
                exit
            self.bowl = inputs.copy()
            shuffle(self.bowl)

        self.round_label = Label(self.win, text="Round " + str(self.round))
        self.description_label = Label(self.win, text="Taboo. Use words to describe the word/phrase. No acting or gestures!")
        self.game_label = Label(self.win, text="Your word is: " + self.current)
        self.done_label = Label(self.win, text="Game over!")
        self.team_label = Label(self.win, text="It is Team " + str(self.team_turn) + "'s turn!")

        self.team_one_point_label = Label(self.win, text="Team 1 Points: " + str(self.team_one))
        self.team_two_point_label = Label(self.win, text="Team 2 Points: " + str(self.team_two))

        score_button = Button(self.win, text="Score if your team guesses correctly!", command=score)
        skip_button = Button(self.win, text="Pass if your team is stuck...", command=skip)
        switch_player = Button(self.win, text="Switch to the next team", command=switch)

        self.round_label.pack()
        self.team_label.pack()
        self.game_label.pack()
        self.description_label.pack()
        self.team_one_point_label.pack(side=LEFT, fill=BOTH)
        self.team_two_point_label.pack(side=RIGHT, fill=BOTH)

        score_button.pack(side=RIGHT, fill=BOTH)
        skip_button.pack(side=LEFT, fill=BOTH)

        switch_player.pack(side=BOTTOM)

    def start(self):
        self.win.mainloop()
