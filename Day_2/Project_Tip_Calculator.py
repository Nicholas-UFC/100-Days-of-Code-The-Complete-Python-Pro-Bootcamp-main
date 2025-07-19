#Programa que calcula o valor da conta, ele pergunta quanto foi a conta, depois pergunta para quantas pessoas vai ser dividida, depois pergunta arredonda para duas casas.Pergunta o % de gorgeta.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("how many people to split the bill?"))

bill_with_tip = (bill / people) * (1+(tip/100))
bill_with_tip = round(bill_with_tip,2)

print(f"Each person should pay {bill_with_tip}")