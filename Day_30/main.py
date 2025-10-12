# Como lidar com erros de maneira elegante

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"A chave {error_message} não existe")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("O arquivo foi fechado!")

altura = float(input("Sua altura: "))
peso = int(input("Seu peso: "))

if altura > 3:
    raise ValueError("Um ser humano não tem como ter mais de 3 metros de altura.")

bmi = peso / altura ** 2
print(f"BMI: {bmi}")