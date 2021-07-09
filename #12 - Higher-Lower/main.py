from replit import clear
import random
import art
import game_data

def check_ans(who, answer):
  if who == answer:
    return True
  else:
    return False

def new_page():
  clear()
  print(art.logo)

def game(data, score):
  correct = True
  i = random.randint(0,49)
  j = random.randint(0,49)
  while correct:
    i = j
    j = random.randint(0,49)
    while i == j:
      j = random.randint(0,49)  
    name1 = data[i]['name']
    description1 = data[i]['description']
    name2 = data[j]['name']
    description2 = data[j]['description']
    pop1 = data[i]['follower_count']
    pop2 = data[j]['follower_count']
    print(f"Compare A: {name1}, a {description1} and pop: {pop1}")
    print(art.vs)
    print(f"Against B: {name2}, a {description2} and pop: {pop2}")
    if data[i]['follower_count'] > data[j]['follower_count']:
      answer = 'A'
    else:
      answer = 'B'
    who = input("Who has more followers? Type 'A' or 'B': ")
    new_page()
    correct = check_ans(who,answer)
    if correct: 
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")

data = game_data.data
score = 0
game(data, score)

