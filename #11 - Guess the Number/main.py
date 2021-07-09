import random 
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1,100)
print(f"Psst... the answer is {answer}")

tries = 0
def diff_choice():
  difficulty = input("Choose a difficulty (easy/hard): ").lower()
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5

def dirn(guess,answer,tries):
  if guess > answer:
    print("Too high.")
    return tries - 1
  elif guess < answer: 
    print("Too low.")
    return tries - 1
  else:
    print("You win.")
    return 0

tries = diff_choice()
while tries > 0:
  print(f"You have {tries} tries remaining to guess the answer.")
  guess = int(input("Make a guess: "))
  tries = dirn(guess,answer,tries)
else: 
  print("Game over.")


