import tkinter

def mile_to_km():
    mile = valor_mile.get()
    resultado = float(mile)*float(1.60934)
    valor_em_km.config(text=resultado)

janela = tkinter.Tk()
janela.title("Mile to Km Converter")
janela.minsize(200, 100)
janela.config(padx=20, pady=20)

# Entry
valor_mile = tkinter.Entry(width=10)
valor_mile.grid(row=1, column=1)

# Label
miles = tkinter.Label(text="Miles")
miles.grid(row=1, column=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=2, column=0)

valor_em_km = tkinter.Label(text="0")
valor_em_km.grid(row=2, column=1)

km = tkinter.Label(text="Km")
km.grid(row=2, column=3)

# Button
calcular = tkinter.Button(text="Calcular", command=mile_to_km)
calcular.grid(row=3, column=2)

janela.mainloop()
