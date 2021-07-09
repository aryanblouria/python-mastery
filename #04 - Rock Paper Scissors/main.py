import random 

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

opt = [rock, paper, scissors]
i = random.randint(0,2)
cc = opt[i]

uc = input("Enter your choice (Rock/Paper/Scissors)\n")
ucl = uc.lower()
print("You chose: ")
if ucl == "rock":
  print(rock)
elif ucl == "paper":
  print(paper)
elif ucl == "scissors":
  print(scissors)
else:
  exit(0)

print(f"The computer chose: \n{cc}\n")

if cc == rock:
  if ucl == "paper":
    print("You win!")
  elif ucl == "rock":
    print("It's a draw")
  else:
    print("You lose!")
elif cc == paper:
  if ucl == "paper":
    print("It's a draw")
  elif ucl == "rock":
    print("You lose!")
  else:
    print("You win!")
else:
  if ucl == "paper":
    print("You lose!")
  elif ucl == "rock":
    print("You win!")
  else:
    print("It's a draw")