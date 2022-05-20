names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#função choice escolhe um elemento aleatorio da lista
roullet = random.choice(names)
print(f"{roullet} is going to buy the meal today!")
