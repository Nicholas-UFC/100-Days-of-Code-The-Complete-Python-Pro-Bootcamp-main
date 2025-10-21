import smtplib
import datetime as dt
import random

EMAIL = "email"
SENHA = "senha"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open(r"Day_32\quotes.txt", encoding="utf-8") as file:
        todas_dicas = file.read().splitlines()
        dica = random.choice(todas_dicas)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, SENHA)
        connection.sendmail(from_addr=EMAIL,to_addrs="bryan_nicholas_fm@outlook.com", msg=f"Subject:Monday Motivation\n\n{dica}")