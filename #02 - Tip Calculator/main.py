print("Welcome to the tip calculator!")
bill = input("Enter total bill: ")
tip = input("Enter tip you would like to give: ")
people = input("Enter number of people sharing the bill: ")

if "%" in tip:
  p_tip = tip[:-1]
else:
  p_tip = tip

individiual_bill = (int(bill)/int(people))*((100+int(p_tip))/100)
i_bill = "{:.2f}".format(individiual_bill)
print(f"Everyone has to pay {i_bill}")