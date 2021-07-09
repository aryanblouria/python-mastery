from replit import clear
from art import logo
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def blackjack():
  
  want_to_play = input("Would you like to play a game of Blackjack?(y/n) ")

  if want_to_play == "y":
    clear()
    print(logo)
    you = []
    dealer = []
    you.append(11)
    you.append(11)
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))
    if sum(you) > 21 and 11 in you:
      you.remove(11)
      you.append(1)
    print(f"Your cards: {you}, current score: {sum(you)}")
    print(f"Dealer's first card: {dealer[0]}")

    game_over = False
    if 10 in dealer and 11 in dealer:
      print(f"\nYour final hand: {you}, final score: {sum(you)}")
      print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")
      print("Dealer Blackjack. You lose.")
      game_over = True
      blackjack()
    elif 10 in you and 11 in you:
      print(f"\nYour final hand: {you}, final score: {sum(you)}")
      print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")
      print("Blackjack. You win.")
      game_over = True
      blackjack()
    else:
      while not game_over: 
        dac = input("\nPress 'y' to draw another card, press 'n' to pass: ")
        if dac == "y":
          you.append(random.choice(cards))
          if 11 in you and sum(you) > 21:
            you.remove(11)
            you.append(1)
          if sum(you) > 21:
            print(f"\nYour final hand: {you}, final score: {sum(you)}")
            print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")
            print("You lose.")
            game_over = True
          else:
            print(f"\nYour cards: {you}, current score: {sum(you)}")
            print(f"Dealer's first card: {dealer[0]}")
        else:
          while sum(dealer) < 17: 
            dealer.append(random.choice(cards))
          print(f"\nYour final hand: {you}, final score: {sum(you)}")
          print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")
          if sum(dealer) > 21:
            print("You win.")
          else:
            if sum(you) > sum(dealer):
              print("You win.")
            elif sum(you) == sum(dealer):
              print("It's a draw.")
            else:
              print("You lose.")
          game_over = True
      else:
        print("")
        blackjack()
  else: 
    clear()
    print("Come play Blackjack with us again!")

blackjack()
