import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("U.S States Games")
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)
new_turtle = turtle.Turtle()
new_turtle.hideturtle()
correct_answer = []
score = 0
is_game_on = True
answer = my_screen.textinput(title="Guess the USA States", prompt = "What's  is another state name? ").title()
data = pandas.read_csv("50_states.csv")
while is_game_on:
    if answer == "Exit":
        break;

    for i in data["state"]:
        if i == answer:
            state = data[data["state"] == answer]
            xcor = (int(state.x))
            ycor = (int(state.y))
            new_turtle.penup()
            new_turtle.goto(xcor,ycor)
            new_turtle.write(answer, align="center", font=("courier", 8, "normal"))
            if answer not in correct_answer:
                score += 1
                correct_answer.append(answer)
                if len(correct_answer) >= 50:
                    is_game_on = False
    else:
        is_game_on = True
    answer = my_screen.textinput(title=f"{score}/{50} states correct", prompt="What's  is another state name? ").title()
missed_states = [i for i in data["state"].to_list() if i not in correct_answer]
states = {
     "states" : missed_states
}
final_data = pandas.DataFrame(states)
final_data.to_csv("state_to_learn.csv")




