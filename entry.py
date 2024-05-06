import tkinter

win = tkinter.Tk()
win.title("Fishbowl")
win.geometry("750x250")

input_var = tkinter.StringVar()
all_inputs = []


def submit():
    input = input_var.get()
    all_inputs.append(input)
    print("You inputed " + input)

    input_var.set("")


input_label = tkinter.Label(win, text="Input words or phrases here",
                            font=('calibre', 10, 'bold'))
input_entry = tkinter.Entry(win, textvariable=input_var,
                            font=('calibre', 10, 'bold'))
submit_button = tkinter.Button(win, text="Submit", command=submit)

input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
submit_button.grid(row=1, column=1)

win.mainloop()
