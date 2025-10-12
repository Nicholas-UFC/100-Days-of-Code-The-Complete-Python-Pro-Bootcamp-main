import json
import random
import tkinter
from tkinter import messagebox

from arquivos import letras

# ---------------------------- CONSTANTS ------------------------------- #
FONTE = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerar_senha():

    password = "".join(random.choice(letras) for i in range(16))

    senha_input.delete(0, tkinter.END)
    senha_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    ws = site_input.get()
    nu = email_input.get()
    pw = senha_input.get()
    new_data = {
        ws: {
            "email": nu,
            "senha": pw,
        }
    }

    if len(ws) == 0 or len(pw) == 0 or len(nu) == 0:
        messagebox.showinfo(
            title="ERRO!", message="Não pode deixar nenhum espaço vazio."
        )

    else:
        try:
            with open(r"Day_29\senhas.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            with open(r"Day_29\senhas.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open(r"Day_29\senhas.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            site_input.delete(0, tkinter.END)
            email_input.delete(0, tkinter.END)
            senha_input.delete(0, tkinter.END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    with open(r"Day_29\senhas.json", mode="r") as data_file:
        data = json.load(data_file)
        ws = site_input.get()

        email_input.delete(0, tkinter.END)
        senha_input.delete(0, tkinter.END)
        email_input.insert(0, data[ws]["email"])
        senha_input.insert(0, data[ws]["senha"])


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

pesquisar = tkinter.Button(text="Pesquisa", command=search)
pesquisar.grid(row=1, column=2, sticky="w")

# Entry: Site, email, senha
site_input = tkinter.Entry(width=21)
site_input.grid(row=1, column=1, sticky="we")
site_input.focus()

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="w")

senha_input = tkinter.Entry(width=21)
senha_input.grid(row=3, column=1, sticky="we")

tela.mainloop()
