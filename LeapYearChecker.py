#input do usuário
year = int(input("Which year do you want to check? "))
#o ano é divisivel por 4? sim, bissexto. não, não bissexto
if year % 4 == 0:
		#o ano é divisivel por 100? sim, não bissexto. não, bissexto
    if year % 100 == 0:
				#mas é divisivel por 400? sim, bissexto. não, não bissexto
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("leap year.")   
else:
    print("Not leap year.")