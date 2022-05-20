number = int(input("Which number do you want to check? "))
#% mostra o resto de uma divisão
#numeros pares divididos por 2 sempre dão 0
nmbr = number % 2
if nmbr == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")