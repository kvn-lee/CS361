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
        self.team_one_grid_index = 8
        self.team_two_grid_index = 8

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
            game = GameWindow(inputs,team_one,team_two)
            game.start()

        def max_players():
            self.popup = Tk()
            label = Label(self.popup, text="You already have 5 players on this team!")
            label.pack()
            ok_button = Button(self.popup, text="Okay", command=self.popup.destroy)
            ok_button.pack()
            self.popup.mainloop()

        def add_team_one():
            if len(team_one) == 5:
                max_players()
                return

            input = team1_entry.get()
            multiple_inputs = input.split("/")
            if len(multiple_inputs) > 0:
                for every_input in multiple_inputs:
                    team_one.append(every_input)
                    team_one_inputs.append(Label(self.win, text=every_input, font=('calibre', 10)))
            else:
                team_one.append(input)
                team_one_inputs.append(Label(self.win,text=input,font=('calibre',10)))

            self.team_one_grid_index = 8
            for value in team_one_inputs:
                value.grid(row=self.team_one_grid_index,column=0,columnspan=1)
                self.team_one_grid_index += 1

            team1_entry.delete(0, 'end')

        def add_team_two():
            if len(team_two) == 5:
                max_players()
                return
            
            input = team2_entry.get()
            multiple_inputs = input.split("/")
            if len(multiple_inputs) > 0:
                for every_input in multiple_inputs:
                    team_two.append(every_input)
                    team_two_inputs.append(Label(self.win, text=every_input, font=('calibre', 10)))
            else:
                team_two.append(input)
                team_two_inputs.append(Label(self.win,text=input,font=('calibre',10)))

            self.team_two_grid_index = 8
            for value in team_two_inputs:
                value.grid(row=self.team_two_grid_index,column=2,columnspan=1)
                self.team_two_grid_index += 1

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
        yes_button.grid(row=21,column=1)

        exit_button = Button(self.win, text="Exit the game", font=('calibre', 10, 'bold'), command=exitGame)
        exit_button.grid(row=25,column=1)

    def start(self):
        self.win.mainloop()

teamwindow = TeamWindow([])
teamwindow.start()