from replit import clear
from art import logo

def add(a, b):
  return a + b

def sub(a,b):
  return a - b

def mul(a,b):
  return a * b

def div(a, b):
  return a / b

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}

def calc():
  print(logo)
  ip = "y"
  n1 = float(input("Enter first number: "))
  for key in operations:
    print(key)
  while ip == "y":
    op = input("Choose operation to perform: ")
    n2 = float(input("Enter second number: "))
    function = operations[op]
    output = function(n1,n2)
    print(f"{n1} {op} {n2} = {output}")
    n1 = output
    ip = input("Would you like to continue?(y/n) ")
  else:
    clear()
    calc()

calc()