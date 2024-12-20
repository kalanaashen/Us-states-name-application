from turtle import Turtle,Screen
from cursor import Cursor
from scoreboard import Score
import pandas
screen=Screen()
screen.title("Guess the states")
turtle=Turtle()
cus=Cursor()
score=Score()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
gueseed_states=[]
missing_list=[]
data=pandas.read_csv("50_states.csv")

temp_x=data.x.to_list()
temp_y=data.y.to_list()
temp_state=data.state.to_list()

game_on=True
while game_on:
    choice = (screen.textinput("Guess the state", "Enter your State")).title()
    for state in range (len(temp_state)-1):
        if choice==temp_state[state]:
            gueseed_states.append(choice)
            cus.travel(temp_x[state],temp_y[state],temp_state[state])
            score.marks_up()
    if choice=="Exit":
        game_on=False










screen.exitonclick()

for guess in range(len(gueseed_states)-1):
    for check_stat in range(len(temp_state)-1):
        if temp_state[check_stat]!= gueseed_states[guess]:
            missing_list.append(temp_state[check_stat])



new_data=pandas.DataFrame(missing_list)
new_data.to_csv("learn_these_states.csv")


