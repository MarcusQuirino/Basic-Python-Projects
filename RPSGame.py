#ascii art pro jogo
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#lista com opções
rps = [rock, paper, scissors]
#input do usuário
user = int(input("insert 0 for rock, 1 for paper or 2 for scissors> "))
user_rps = rps[user]
#randomizador do cpu
cpu_rps = random.choice(rps)
#template de output grafico
output = f"YOU:\n{user_rps}\nCPU:\n{cpu_rps}"
#logica por traz do jogo
if user_rps == rock and cpu_rps == rock:
  print(output)
  print("We have a TIE")
elif user_rps == rock and cpu_rps == paper:
  print(output)
  print("You LOSE")
elif user_rps == rock and cpu_rps == scissors:
  print(output)
  print("You WIN")
elif user_rps == paper and cpu_rps == rock:
  print(output)
  print("You WIN")
elif user_rps == paper and cpu_rps == paper:
  print(output)
  print("We have a TIE")
elif user_rps == paper and cpu_rps == scissors:
  print(output)
  print("You LOSE")
elif user_rps == scissors and cpu_rps == rock:
  print(output)
  print("You LOSE")
elif user_rps == scissors and cpu_rps == paper:
  print(output)
  print("You WIN")
elif user_rps == scissors and cpu_rps == scissors:
  print(output)
  print("We have a TIE")
