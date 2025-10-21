import random
import smtplib
from datetime import datetime

import pandas as pd

EMAIL = "email"
SENHA = "senha"

hoje = datetime.now()
hoje_tuple = (hoje.month, hoje.day)

data = pd.read_csv(r"Day_32\aniversario\birthdays.csv")

aniversario_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if hoje_tuple in aniversario_dict:
    aniversariante = aniversario_dict[hoje_tuple]
    file_path = (
        f"Day_32\aniversario\\letter_templates\\letter={random.randint(1,3)}.txt"
    )

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", aniversariante["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, SENHA)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=aniversariante["email"],
            msg=f"Subject:Feliz Aniversario\n\n{contents}",
        )
