import tkinter


def submit():
    input = input_var.get()
    all_inputs.append(input)
    input_var.set("")

    display()


def display():
    inputs = 3
    for value in all_inputs:
        display_label = tkinter.Label(win, text="Here are your words/phrases:",
                                      font=('calibre', 10))
        display_entry = tkinter.Label(win, text=value, font=('calibre', 10))

        display_label.grid(row=2, column=1)
        display_entry.grid(row=inputs, column=1)
        inputs += 1


win = tkinter.Tk()
win.title("Fishbowl")
win.geometry("500x500")

input_var = tkinter.StringVar()
all_inputs = []

input_label = tkinter.Label(win, text="Input words or phrases here",
                            font=('calibre', 10, 'bold'))
input_entry = tkinter.Entry(win, textvariable=input_var,
                            font=('calibre', 10))
submit_button = tkinter.Button(win, text="Submit", command=submit)

input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
submit_button.grid(row=1, column=1)

win.mainloop()
