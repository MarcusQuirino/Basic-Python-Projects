print("Welcome to the tip calculator!")
#recolhendo informações do usuário
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give?\n"))
split = int(input("How many people to split the bill?\n"))
#adicionando a porcentagem no valor final
bill_tip = tip/100*bill+bill
#divindindo valor final pelo numero de pessoas
#formatação pra duas casas decimais
pay_split = round(bill_tip/split, 2)
pay = "{:.2f}".format(pay_split)
#output final
print(f"Each person should pay: ${pay}")