import smtplib

my_email = "email@gmail.com"
senha = "senha"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=senha)
connection.sendmail(from_addr=my_email, to_addrs=" bryan_nicholas_fm@outlook.com", msg="Subject:Oi\n\nEsse e o corpo do texto do email.")
connection.close()

import datetime as dt

now = dt.datetime.now()

data_de_nascimento = dt.datetime(year=2000, month=1, day=17)
print(data_de_nascimento)

