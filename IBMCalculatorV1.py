height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#converter heigth e weigth de str pra float e int respectivamente
h = float(height)
w = int(weight)
#formula do BMI convertida pra int
bmi = int(w/h**2)
print(bmi)