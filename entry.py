from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from team import TeamWindow

class EntryWindow:
    def __init__(self):
        win = Tk()
        win.title("Fishbowl Entries")
        win.geometry("750x500")

        self.all_inputs = []
        self.all_labels = []

        def submit(): 
            input = input_entry.get()
            multiple_inputs = input.split("/")
            if len(multiple_inputs) > 0:
                for every_input in multiple_inputs:
                    self.all_inputs.append(every_input)
                    self.all_labels.append(Label(win, text=every_input, font=('calibre', 10)))
            else:
                self.all_inputs.append(input)
                self.all_labels.append(Label(win, text=input, font=('calibre', 10)))

            display_label.pack()
            for value in self.all_labels:
                value.pack()

            input_entry.delete(0, 'end')

        def clear():
            self.popup = Tk()
            label = Label(self.popup, text="Are you sure you want to clear all inputs?")
            label.pack()
            yes_button = Button(self.popup, text="Yes", command=clear_inputs)
            yes_button.pack(padx=50, pady=50, side='left')
            no_button = Button(self.popup, text="No", command=self.popup.destroy)
            no_button.pack(padx=50, pady=50, side='right')
            self.popup.mainloop()

        def clear_inputs():
            for value in self.all_labels:
                value.destroy()

            self.popup.destroy()

            self.all_inputs = []
            self.all_labels = []

            display_label.pack()

        def done():
            team = TeamWindow(self.all_inputs)
            win.destroy()
            team.start()

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
            save_inputs()
            self.popup.destroy()
            win.destroy()

        def save_inputs():
            f = open("./states/inputs.txt", "w")

            for input in self.all_inputs:
                f.write(input)

            f.close()

        def load_inputs():
            f = open("./states/inputs.txt", "r")

            for line in f:
                self.all_inputs.append(line)
                self.all_labels.append(Label(win, text=line, font=('calibre', 10)))

            display_label.pack()

            for value in self.all_labels:
                value.pack()

            f.close()

        input1_label = Label(win, text="Step 1: Input the words or phrases that you want to play with here:", font=('calibre', 10, 'bold'))
        input2_label = Label(win, text="You can input them in one at a time OR input them divided by a '/' (ex: apple/carrot/potato)", font=('calibre', 10, 'bold'))
        input_entry = Entry(win, font=('calibre', 10))
        display_label = Label(win, text="Here are your words/phrases:", font=('calibre', 10, 'bold'))
        submit_button = Button(win, text="Submit", command=submit)
        clear_button = Button(win, text="Clear the list of inputs", command=clear)
        load_button = Button(win, text="Load words/phrases from a previous game", command=load_inputs)
        done_button = Button(win, text="Done inputting words and phrases", command=done)
        exit_button = Button(win, text="Exit the game", font=('bold'), command=exitGame)

        input1_label.pack()
        input2_label.pack()
        input_entry.pack()
        load_button.pack()
        submit_button.pack()
        done_button.pack()
        clear_button.pack()
        exit_button.pack()

    def start(self):
        self.win.mainloop()
