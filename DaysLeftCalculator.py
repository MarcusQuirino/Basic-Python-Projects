age = input("What is your current age?")
#transformar age de str pra int
a = int(age)
#calcular os dias, semanas e meses do usuário
user_days = int(a*365)
user_weeks = int(a*52)
user_months = int(a*12)
#calcular dia, semanas e meses em 90 anos
days = 90*365
weeks = 90*52
months = 90*12
#diferença entre todas dos valores e os valores do usuário
days_left = int(days-user_days)
weeks_left = int(weeks-user_weeks)
months_left = int(months-user_months)
#output final
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")