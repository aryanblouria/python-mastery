import turtle, pandas

sc = turtle.Screen()
sc.title("U.S. States Game")
img = "blank_states_img.gif"
sc.addshape(img)
turtle.shape(img)


def write_state(x, y, ans_state):
    txt = turtle.Turtle()
    txt.hideturtle()
    txt.penup()
    txt.goto(x, y)
    txt.write(ans_state, False, "center", ("Arial", 8, "normal"))


def update_score(score):
    score += 1
    return score


data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

game_over = False
score = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = sc.textinput(f"{score}/50 States Correct", "Enter a state name: ").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        f_state = data[data["state"] == answer_state]
        x_cor = int(f_state["x"])
        y_cor = int(f_state["y"])
        guessed_states.append(answer_state)
        write_state(x_cor, y_cor, answer_state)
        score = update_score(score)

missed_states = []
for state in states:
    if state not in guessed_states:
        missed_states.append(state)

state_dict = {
    "missed states": missed_states
}

df = pandas.DataFrame(state_dict)
df.to_csv("missing_states.csv")


