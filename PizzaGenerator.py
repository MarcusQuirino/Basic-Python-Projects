#infos do usuário
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#tamanho da piza
if size == "S":
    valor = 15
#peperone extra
    if add_pepperoni == "Y":
        valor += 2
#quiejo extra
        if extra_cheese == "Y":
            valor += 1
            print(f"Your final bill is: ${valor}.")
        else:
            print(f"Your final bill is: ${valor}.")
    else:
#quiejo extra
        if extra_cheese == "Y":
            valor += 1
            print(f"Your final bill is: ${valor}.")
        else:
            print(f"Your final bill is: ${valor}.")
#tamanho da piza
elif size == "M":
    valor = 20
#peperone extra
    if add_pepperoni == "Y":
        valor += 3
        if extra_cheese == "Y":
#quiejo extra
            valor += 1
            print(f"Your final bill is: ${valor}.")
        else:
            print(f"Your final bill is: ${valor}.")
    else:
        if extra_cheese == "Y":
#quiejo extra
            valor +=1
            print(f"Your final bill is: ${valor}.")
        else:
            print(f"Your final bill is: ${valor}.")
#tamanho da piza
else:
    valor = 25
#peperone extra
    if add_pepperoni == "Y":
        valor += 3
        if extra_cheese == "Y":
#quiejo extra
            valor += 1
            print(f"Your final bill is: ${valor}.")
        else:
            print(f"Your final bill is: ${valor}.")
    else:
        if extra_cheese == "Y":
#quiejo extra
            valor += 1
            print(f"Your final bill is: ${valor}.")
        else:
            print(f"Your final bill is: ${valor}.")