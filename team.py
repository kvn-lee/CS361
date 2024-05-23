from tkinter import Button
from tkinter import Label
from tkinter import Tk
from tkinter import Entry
from game import GameWindow
import os


class TeamWindow:
    def __init__(self, inputs):
        self.win = Tk()
        self.win.title("Fisbowl Teams")
        self.win.geometry("1000x600")

        self.team_one = []
        self.team_one_inputs = []
        self.team_two = []
        self.team_two_inputs = []
        self.team_one_grid_index = 9
        self.team_two_grid_index = 9

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

        def exit_window():
            self.win.destroy()
            game = GameWindow(inputs,self.team_one,self.team_two)
            game.start()

        def max_players():
            self.popup = Tk()
            label = Label(self.popup, text="You already have 5 players on this team!")
            label.pack()
            ok_button = Button(self.popup, text="Okay", command=self.popup.destroy)
            ok_button.pack()
            self.popup.mainloop()

        def add_team_one():
            if len(self.team_one) == 5:
                max_players()
                return

            input = team1_entry.get()
            multiple_inputs = input.split("/")
            if len(multiple_inputs) > 0:
                for every_input in multiple_inputs:
                    self.team_one.append(every_input)
                    self.team_one_inputs.append(Label(self.win, text=every_input, font=('calibre', 10)))
            else:
                self.team_one.append(input)
                self.team_one_inputs.append(Label(self.win,text=input,font=('calibre',10)))

            self.team_one_grid_index = 9
            for value in self.team_one_inputs:
                value.grid(row=self.team_one_grid_index,column=0,columnspan=1)
                self.team_one_grid_index += 1

            team1_entry.delete(0, 'end')

        def add_team_two():
            if len(self.team_two) == 5:
                max_players()
                return
            
            input = team2_entry.get()
            multiple_inputs = input.split("/")
            if len(multiple_inputs) > 0:
                for every_input in multiple_inputs:
                    self.team_two.append(every_input)
                    self.team_two_inputs.append(Label(self.win, text=every_input, font=('calibre', 10)))
            else:
                self.team_two.append(input)
                self.team_two_inputs.append(Label(self.win,text=input,font=('calibre',10)))

            self.team_two_grid_index = 9
            for value in self.team_two_inputs:
                value.grid(row=self.team_two_grid_index,column=2,columnspan=1)
                self.team_two_grid_index += 1

            team2_entry.delete(0, 'end')

        def confirm_clear_one():
            self.confirmation = Tk()
            label = Label(self.confirmation, text="Are you sure you want to clear the list of players?")
            label.pack()
            yes_button = Button(self.confirmation, text="Yes", command=clear_team_one)
            yes_button.pack(padx=50, pady=50, side='left')
            no_button = Button(self.confirmation, text="No", command=self.confirmation.destroy)
            no_button.pack(padx=50, pady=50, side='right')
            self.confirmation.mainloop()

        def confirm_clear_two():
            self.popup = Tk()
            label = Label(self.popup, text="Are you sure you want to clear the list of players?")
            label.pack()
            yes_button = Button(self.popup, text="Yes", command=clear_team_two)
            yes_button.pack(padx=50, pady=50, side='left')
            no_button = Button(self.popup, text="No", command=self.popup.destroy)
            no_button.pack(padx=50, pady=50, side='right')
            self.popup.mainloop()

        def clear_team_one():
            for value in self.team_one_inputs:
                value.destroy()

            self.team_one = []
            self.team_one_inputs = []

            self.confirmation.destroy()
        
        def clear_team_two():
            for value in self.team_two_inputs:
                value.destroy()
            self.team_two = []
            self.team_two_inputs = []

            self.popup.destroy()

        def save_team():
            f = open("./states/players.txt", "w")

            for player in self.team_one:
                f.write("Team 1:" + player + "\n")

            for player in self.team_two:
                f.write("Team 2:" + player + "\n")

            f.close()

        def load_team():
            f = open("./states/players.txt", "r")

            if os.path.getsize("./states/players.txt") > 0:
                for line in f:
                    if line.find("1") > 0:
                        self.team_one.append(line[7:])
                        self.team_one_inputs.append(Label(self.win, text=line[7:], font=('calibre', 10)))
                    if line.find("2") > 0:
                        self.team_two.append(line[7:])
                        self.team_two_inputs.append(Label(self.win, text=line[7:], font=('calibre', 10)))
                
                self.team_one_grid_index = 9
                for value in self.team_one_inputs:
                    value.grid(row=self.team_one_grid_index,column=0,columnspan=1)
                    self.team_one_grid_index += 1

                self.team_two_grid_index = 9
                for value in self.team_two_inputs:
                    value.grid(row=self.team_two_grid_index,column=2,columnspan=1)
                    self.team_two_grid_index += 1
            f.close()

        title = Label(self.win, text="Step 2: Let's make teams!")
        instruction = Label(self.win, text="Once in teams, you will alternate between players of each team!")
        team_label_entry = Label(self.win, text="You can input players' names one at a time OR input them divided by a '/' (ex: Jeremy/Alice/Fiona)", font=('calibre', 10, 'bold'))
        team_maximum = Label(self.win, text="Maximum players per team is 5", font=('calibre', 10, 'bold'))

        team1_label = Label(self.win, text="Input players for Team 1:", font=('calibre', 10, 'bold'))
        team1_entry = Entry(self.win, font=('calibre', 10))
        team1_submit = Button(self.win, text="Enter player for Team 1:", command=add_team_one)
        team1_clear = Button(self.win, text="Clear the list of players for Team 1", command=confirm_clear_one)

        display_team1 = Label(self.win, text="Team 1 players:", font=('calibre', 10, 'bold'))

        team2_label = Label(self.win, text="Input players for Team 2:", font=('calibre', 10, 'bold'))
        team2_entry = Entry(self.win, font=('calibre', 10))
        team2_submit = Button(self.win, text="Enter player for Team 2:", command=add_team_two)
        team2_clear = Button(self.win, text="Clear the list of players for Team 2", command=confirm_clear_two)

        display_team2 = Label(self.win, text="Team 2 players:", font=('calibre', 10, 'bold'))

        save_team_button = Button(self.win, text="Save players for future rounds", command=save_team)
        load_team_button = Button(self.win, text="Load players from a saved round", command=load_team)
        confirmation = Label(self.win, text="Are you ready to start?")

        title.grid(row=0,column=1)
        instruction.grid(row=1,column=1)
        team_label_entry.grid(row=2,column=1)
        team_maximum.grid(row=3,column=1)

        team1_label.grid(row=4,column=0,columnspan=1)
        team1_entry.grid(row=5,column=0,columnspan=1)
        team1_submit.grid(row=6,column=0,columnspan=1)
        display_team1.grid(row=7,column=0,columnspan=1)
        team1_clear.grid(row=8,column=0,columnspan=1)

        team2_label.grid(row=4,column=2,columnspan=1)
        team2_entry.grid(row=5,column=2,columnspan=1)
        team2_submit.grid(row=6,column=2,columnspan=1)
        display_team2.grid(row=7,column=2,columnspan=1)
        team2_clear.grid(row=8,column=2,columnspan=1)

        load_team_button.grid(row=18, column=1)
        save_team_button.grid(row=19, column=1)
        confirmation.grid(row=20,column=1)
        yes_button = Button(self.win, text="Yes", command=exit_window)
        yes_button.grid(row=21,column=1)

        exit_button = Button(self.win, text="Exit the game", font=('calibre', 10, 'bold'), command=exitGame)
        exit_button.grid(row=25,column=1)

    def start(self):
        self.win.mainloop()