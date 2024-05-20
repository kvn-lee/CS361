from random import shuffle
from tkinter import Tk
from tkinter import Label
from tkinter import Button
import zmq


class GameWindow():
    def __init__(self, inputs,team_one,team_two):
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
        self.team_one_player = 0
        self.team_two_player = 0
        self.current_player = team_one[0]

        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5000")

        shuffle(self.bowl)

        def score():
            if self.team_turn == 1:
                self.team_one += 1
            else:
                self.team_two += 1

            display()

        def switch():
            if self.team_turn == 1:
                self.team_turn = 2
                self.current_player = team_two[self.team_two_player]
                self.team_two_player += 1
                if self.team_two_player >= len(team_two):
                    self.team_two_player = 0
            else:
                self.team_turn = 1
                self.current_player = team_one[self.team_one_player]
                self.team_one_player += 1
                if self.team_one_player >= len(team_one):
                    self.team_one_player = 0

            skip()

        def skip():
            self.bowl.append(self.current)
            display()

        def display():
            self.round_label.destroy()
            self.team_label.destroy()
            self.game_label.destroy()
            self.description_label.destroy()

            if len(self.bowl) == 0:
                socket.send_json([self.team_one, self.team_two])
                response = socket.recv_string()
                print(f"Received response: {response}")
                self.round += 1
                if self.round == 4:
                    self.done_label.pack()
                    self.round_label.destroy()
                    self.team_label.destroy()
                    self.game_label.destroy()
                    self.description_label.destroy()
                    self.team_one_point_label.destroy()
                    self.team_two_point_label.destroy()
                    skip_button.destroy()
                    score_button.destroy()
                    switch_player.destroy()
                    return
                self.bowl = inputs.copy()
            
            shuffle(self.bowl)
            self.current = self.bowl.pop(self.card)

            self.team_label = Label(self.win, text="It is " + self.current_player + "'s turn from Team " + str(self.team_turn) + "!")
            self.game_label = Label(self.win, text="Your word is: " + self.current)
            self.round_label = Label(self.win, text="Round " + str(self.round))

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

            skip_button.pack(side='left')
            score_button.pack(side='right')

            switch_player.pack(side='bottom')
            exit_button.pack(side='bottom')
        
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

        self.round_label = Label(self.win, text="Round " + str(self.round))
        self.description_label = Label(self.win, text="Taboo. Use words to describe the word/phrase. No acting or gestures!")
        self.game_label = Label(self.win, text="Your word is: " + self.current)
        self.done_label = Label(self.win, text="Game over!")
        self.team_label = Label(self.win, text="It is " + self.current_player + "'s turn from Team " + str(self.team_turn) + "!")

        score_button = Button(self.win, text="Score if your team guesses correctly!", command=score)
        skip_button = Button(self.win, text="Pass if your team is stuck...", command=skip)
        switch_player = Button(self.win, text="Switch to the next team", command=switch)
        exit_button = Button(self.win, text="Exit the game", font=('calibre',10,'bold'), command=exitGame)

        self.round_label.pack()
        self.team_label.pack()
        self.game_label.pack()
        self.description_label.pack()

        skip_button.pack(side='left')
        score_button.pack(side='right')

        switch_player.pack(side='bottom')
        exit_button.pack(side='bottom')

    def start(self):
        self.win.mainloop()