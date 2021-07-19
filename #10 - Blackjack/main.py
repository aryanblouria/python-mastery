from replit import clear
from art import logo
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
user_cards = []
computer_cards = []
game_over = False

def setup():
  clear()
  print(logo)
  user_cards.clear()
  computer_cards.clear()
  deal_card(user_cards)
  deal_card(user_cards)
  deal_card(computer_cards)
  deal_card(computer_cards)
  score_check(user_cards, computer_cards)
  blackjack_check(user_cards, computer_cards)

def user_play():
  dac = input("\nWould you like to draw another card? (y/n): ")
  if dac == "y":
    deal_card(user_cards)
    score_check(user_cards, computer_cards)
    user_play()

def comp_play():
  while sum(computer_cards) < 17:
    deal_card(computer_cards)
  score_check(user_cards, computer_cards)

def deal_card(deck):
  deck.append(random.choice(cards))

def blackjack_check(user, computer):
  if 10 in user and 11 in user:
    final_score()
    print("Blackjack! You win.\n")
    new_game()
  elif 10 in computer and 11 in computer:
    final_score()
    print("Computer Blackjack! You lose.\n")
    new_game()
  
def score_check(user, computer):
  print(f"\nYour cards: {user}, current score: {sum(user)}")
  print(f"Computer's first card: {computer[0]}, cards: {computer}")
  if sum(user) > 21:
    if 11 not in user:
      final_score()
      print("You lose.\n")
      new_game()
    else:
      print("Changing your 11 to 1...")
      user[user.index(11)] = 1
  elif sum(computer) > 21:
    if 11 not in computer:
      final_score()
      print("You win.\n")
      new_game()
    else:
      print("Changing computer's 11 to 1...")
      computer[computer.index(11)] = 1

def final_score():
   print(f"\nYour cards: {user_cards}, final score: {sum(user_cards)}")
   print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}\n")

def final_check():
  final_score()
  if sum(user_cards) > sum(computer_cards):
    print("You win.\n")
  elif sum(computer_cards) > sum(user_cards):
    print("You lose.\n")
  else:
    print("It's a draw!\n")
  new_game()

def new_game():
  wtp = input("Would you like to play a game of Blackjack? (y/n): ").lower()
  if wtp == "y": 
    setup()
    user_play()
    comp_play()
    final_check()
  else:
    clear()
    print("We hope to see you again!")
    exit()    

new_game()

