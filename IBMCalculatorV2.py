#informações do usuário
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#calculo do bmi e formatação de informação
bmi = weight/height**2
bmi_rounded = round(bmi)
output = f"{weight} ÷ ({height} x {height}) = {bmi}"
#if statment checando cada uma das categorias
if bmi < 18.5:
    print(output)
    print(f"Your BMI is {bmi_rounded}, you are underweight")
elif bmi <= 25:
    print(output)
    print(f"Your BMI is {bmi_rounded}, you have a normal weight.")
elif bmi <= 30:
    print(output)
    print(f"Your BMI is {bmi_rounded}, you are slightly overweight.")
elif bmi <= 40:
    print(output)
    print(f"Your BMI is {bmi_rounded}, you are obese")
else:
    print(output)
    print(f"Your BMI is {bmi_rounded}, you are clinically obese")