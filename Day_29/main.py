import random
import tkinter
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
FONTE = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerar_senha():
    letras = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "!",
        "#",
        "$",
        "%",
        "&",
        "(",
        ")",
        "*",
        "+",
    ]

    password = "".join(random.choice(letras) for i in range(16))

    senha_input.delete(0, tkinter.END)
    senha_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    ws = site_input.get()
    nu = email_input.get()
    pw = senha_input.get()

    if len(ws) == 0 or len(pw) == 0 or len(nu) == 0:
        messagebox.showinfo(
            title="ERRO!", message="Não pode deixar nenhum espaço vazio."
        )

    else:
        pode = messagebox.askokcancel(
            title="Site",
            message=f"Você está tentando salvar: \nSite: {ws} \nEmail: {nu} \nSenha: {pw} \nPosso salvar? ",
        )

        if pode:
            with open(r"Day_29\senhas.txt", mode="a") as file:
                file.write(f"Site: {ws} | Email/Usuario: {nu} | Senha: {pw}\n")
                site_input.delete(0, tkinter.END)
                email_input.delete(0, tkinter.END)
                senha_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
tela = tkinter.Tk()
tela.title("Gerenciador de Senhas")
tela.config(padx=20, pady=20)

# Imagem
canvas = tkinter.Canvas(width=200, height=200)
cadeado = tkinter.PhotoImage(file=r"Day_29\logo.png")
canvas.create_image(100, 100, image=cadeado)
canvas.grid(row=0, column=1)

# Label: Site, e-mail/nome de usuaio, senha
site = tkinter.Label(text="Site")
site.grid(row=1, column=0)

email = tkinter.Label(text="Email/Nome de Usuario")
email.grid(row=2, column=0)

senha = tkinter.Label(text="Senha")
senha.grid(row=3, column=0)

# Button: Gerar senha e Adicionar
gerar = tkinter.Button(text="Gerar Senha", command=gerar_senha)
gerar.grid(row=3, column=2, sticky="w")

adicionar = tkinter.Button(text="Adicionar", command=add, width=36)
adicionar.grid(row=4, column=1, columnspan=2, sticky="w")

# Entry: Site, email, senha
site_input = tkinter.Entry(width=35)
site_input.grid(row=1, column=1, columnspan=2, sticky="w")
site_input.focus()

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="w")

senha_input = tkinter.Entry(width=21)
senha_input.grid(row=3, column=1, sticky="we")

tela.mainloop()
