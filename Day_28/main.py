import time
import tkinter
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer

    if timer is not None:
        tela.after_cancel(timer)
    canvas.itemconfig(timer_texto, text="00:00")
    titulo.config(text="Timer")
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    trabalhar = WORK_MIN * 60
    descanso_curto = SHORT_BREAK_MIN * 60
    descanso_longo = LONG_BREAK_MIN * 60

    if reps > 8:
        reps = 0
    elif reps == 8:
        count_down(descanso_longo)
        titulo.config(text="Descanso longo")
    elif reps % 2 == 0:
        count_down(descanso_curto)
        titulo.config(text="Descanso curto")
    else:
        count_down(trabalhar)
        titulo.config(text="Trabalhar")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutos = floor(count / 60)
    segundos = count % 60

    if segundos < 10:
        segundos = f"0{segundos}"

    canvas.itemconfig(timer_texto, text=f"{minutos}:{segundos}")
    if count > 0:
        timer = tela.after(1000, count_down, count - 1)
    else:
        start_timer()
        titulo.config(text="Trabalhar")
        mark = ""
        for i in range(floor(reps / 2)):
            mark += "✔"
            checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
tela = tkinter.Tk()
tela.title("Pomodoro")
tela.config(padx=100, pady=50, bg=YELLOW)

# Tomate e relogio
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = tkinter.PhotoImage(file=r"Day_28\tomato.png")
canvas.create_image(100, 112, image=tomate_img)
timer_texto = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
canvas.grid(row=1, column=1)


# Titulo
titulo = tkinter.Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
titulo.grid(row=0, column=1)

# Botões
start = tkinter.Button(text="start", command=start_timer, highlightthickness=0)
start.grid(row=2, column=0)

reset = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(row=2, column=2)

# Checkmark
checkmark = tkinter.Label(font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

tela.mainloop()
