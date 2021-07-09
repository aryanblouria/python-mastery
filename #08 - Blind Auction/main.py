from replit import clear
from art import logo

print(logo)
more_bids = "yes"
buyers = {}
while more_bids.lower() == "yes":
  name = input("What is your name? ")
  bid = input("What is your bid? ")
  buyers[name] = int(bid)
  print(buyers)
  more_bids = input("Are there any other bidders? ")
  clear()
else:
  maxm = 0
  winner = max(buyers)
  maxm = buyers[winner] 
  print(f"The winner is {winner} with a bid of {maxm}")
    
  

