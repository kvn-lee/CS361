from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk


class EntryWindow:
    def __init__(self):
        win = Tk()
        win.title("Fishbowl Entries")
        win.geometry("500x500")

        all_inputs = []
        all_labels = []

        def submit():
            input = input_entry.get()
            all_inputs.append(input)
            all_labels.append(Label(win, text=input, font=('calibre',
                              10)))

            display_label.pack()
            for value in all_labels:
                value.pack()

            input_entry.delete(0, 'end')

        input_label = Label(win, text="Input words or phrases here",
                            font=('calibre', 10, 'bold'))
        input_entry = Entry(win, font=('calibre', 10))
        display_label = Label(win, text="Here are your words/phrases:",
                              font=('calibre', 10, 'bold'))
        submit_button = Button(win, text="Submit", command=submit)

        input_label.pack()
        input_entry.pack()
        submit_button.pack()

    def start(self):
        self.win.mainloop
