from tkinter import Button
from tkinter import Label
from tkinter import Tk
from tkinter import Entry
from game import GameWindow


class TeamWindow:
    def __init__(self, inputs):
        self.win = Tk()
        self.win.title("Fisbowl Teams")
        self.win.geometry("1000x500")

        team_one = []
        team_one_inputs = []
        team_two = []
        team_two_inputs = []
        team_one_grid_index = 8
        team_two_grid_index = 8

        def exit_window():
            self.win.destroy()
            game = GameWindow(inputs)
            game.start()

        def add_team_one():
            input = team1_entry.get()
            multiple_inputs = input.split("/")
            if len(multiple_inputs) > 0:
                for every_input in multiple_inputs:
                    team_one.append(every_input)
                    team_one_inputs.append(Label(self.win, text=every_input, font=('calibre', 10)))
            else:
                team_one.append(input)
                team_one_inputs.append(Label(self.win,text=input,font=('calibre',10)))

            for value in team_one_inputs:
                value.grid(row=team_one_grid_index,column=0,columnspan=1)
                team_one_grid_index += 1

            team1_entry.delete(0, 'end')

        def add_team_two():
            input = team2_entry.get()
            multiple_inputs = input.split("/")
            if len(multiple_inputs) > 0:
                for every_input in multiple_inputs:
                    team_two.append(every_input)
                    team_two_inputs.append(Label(self.win, text=every_input, font=('calibre', 10)))
            else:
                team_two.append(input)
                team_two_inputs.append(Label(self.win,text=input,font=('calibre',10)))

            for value in team_two_inputs:
                value.grid(row=team_two_grid_index,column=2,columnspan=1)
                team_two_grid_index += 1

            team2_entry.delete(0, 'end')

        title = Label(self.win, text="Step 2: Let's make teams!")
        instruction = Label(self.win, text="Once in teams, you will alternate between players of each team!")
        team_label_entry = Label(self.win, text="You can input players' names one at a time OR input them divided by a '/' (ex: Jeremy/Alice/Fiona)", font=('calibre', 10, 'bold'))
        team_maximum = Label(self.win, text="Maximum players per team is 5", font=('calibre', 10, 'bold'))

        team1_label = Label(self.win, text="Input players for Team 1:", font=('calibre', 10, 'bold'))
        team1_entry = Entry(self.win, font=('calibre', 10))
        team1_submit = Button(self.win, text="Enter player for Team 1:", command=add_team_one)

        display_team1 = Label(self.win, text="Team 1 players:", font=('calibre', 10, 'bold'))

        team2_label = Label(self.win, text="Input players for Team 2:", font=('calibre', 10, 'bold'))
        team2_entry = Entry(self.win, font=('calibre', 10))
        team2_submit = Button(self.win, text="Enter player for Team 2:", command=add_team_two)

        display_team2 = Label(self.win, text="Team 2 players:", font=('calibre', 10, 'bold'))

        confirmation = Label(self.win, text="Are you ready to start?")

        title.grid(row=0,column=1)
        instruction.grid(row=1,column=1)
        team_label_entry.grid(row=2,column=1)
        team_maximum.grid(row=3,column=1)

        team1_label.grid(row=4,column=0,columnspan=1)
        team1_entry.grid(row=5,column=0,columnspan=1)
        team1_submit.grid(row=6,column=0,columnspan=1)
        display_team1.grid(row=7,column=0,columnspan=1)

        team2_label.grid(row=4,column=2,columnspan=1)
        team2_entry.grid(row=5,column=2,columnspan=1)
        team2_submit.grid(row=6,column=2,columnspan=1)
        display_team2.grid(row=7,column=2,columnspan=1)

        confirmation.grid(row=20,column=1)
        yes_button = Button(self.win, text="Yes", command=exit_window)
        yes_button.grid(row=21,column=0)
        no_button = Button(self.win, text="No")
        no_button.grid(row=21,column=2)

    def start(self):
        self.win.mainloop()

teamwindow = TeamWindow([])
teamwindow.start()