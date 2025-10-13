import random
import tkinter

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
carta_atual = {}

# ---------------------------- Dataset ------------------------------- #
try:
    df = pd.read_csv(r"Day_31\data\words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv(r"Day_31\data\french_words.csv")
finally:
    aprender = df.to_dict(orient="records")


# ---------------------------- Funções ------------------------------- #
def next_card():
    global carta_atual, flip_timer
    tela.after_cancel(flip_timer)
    carta_atual = random.choice(aprender)
    canvas.itemconfig(card_titulo, text="French", fill="black")
    canvas.itemconfig(card_palavra, text=carta_atual["French"], fill="black")
    canvas.itemconfig(card_fundo, image=imagem_frente)
    flip_timer = tela.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_titulo, text="English", fill="white")
    canvas.itemconfig(card_palavra, text=carta_atual["English"], fill="white")
    canvas.itemconfig(card_fundo, image=imagem_fundo)


def remove_card():
    aprender.remove(carta_atual)
    next_card()

    data = pd.DataFrame(aprender)
    data.to_csv(r"Day_31\data\words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
tela = tkinter.Tk()
tela.title("Frances pro Ingles")
tela.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = tela.after(3000, func=flip_card)

# Canvas
canvas = tkinter.Canvas(width=800, height=526)
imagem_fundo = tkinter.PhotoImage(file=r"Day_31\images\card_back.png")
imagem_frente = tkinter.PhotoImage(file=r"Day_31\images\card_front.png")
card_fundo = canvas.create_image(400, 263, image=imagem_frente)
card_titulo = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_palavra = canvas.create_text(400, 263, text="mot", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
imagem_sim = tkinter.PhotoImage(file=r"Day_31\images\right.png")
imagem_nao = tkinter.PhotoImage(file=r"Day_31\images\wrong.png")

sim = tkinter.Button(image=imagem_sim, highlightthickness=0, command=next_card)
sim.grid(row=1, column=0)

nao = tkinter.Button(image=imagem_nao, highlightthickness=0, command=remove_card)
nao.grid(row=1, column=1)

next_card()

tela.mainloop()
