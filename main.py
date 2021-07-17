invited_names = open("Input/Names/invited_names.txt")
starting_letter = open("Input/Letters/starting_letter.txt")
s_letter = starting_letter.read()
inv_names = invited_names.readlines()

f_inv_names = []

for name in inv_names:
    f_inv_names.append(name.strip("\n"))

for name in f_inv_names:
    send = open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w")
    send.write(s_letter.replace("[name]", name))