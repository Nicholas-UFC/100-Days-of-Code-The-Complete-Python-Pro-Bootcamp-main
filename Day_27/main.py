import tkinter


# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("Meu primeiro GUI programa")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# New Button
new_label = tkinter.Label(text="I am a new Label", font=("Arial", 24, "bold"))
new_label.grid(column=2, row=0)


window.mainloop()
