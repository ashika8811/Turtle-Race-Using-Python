from turtle import Turtle,Screen
import random
my_screen=Screen()
my_screen.title("Turtle Race")
my_screen.bgcolor("black")
color_list=["red","yellow","white","blue","green"]
turtle_list=[]
y_cor=[160,80,0,-80,-160]


for i in range(5):

   tim=Turtle()
   tim.shape("turtle")
   tim.color(color_list[i])
   tim.penup()
   tim.goto(-300,y_cor[i])
   turtle_list.append(tim)

turtle_list[2].goto(300,-300)
turtle_list[2].pendown()
turtle_list[2].goto(300,300)
turtle_list[2].penup()
turtle_list[2].goto(-300,0)

announcer=Turtle()
announcer.color("white")
announcer.hideturtle()

user_bet=my_screen.textinput(title="Turtle Rce",prompt="which turtle will win?").lower()

game_on=True
while game_on:
  for t in turtle_list:
    a=random.randint(5,25)
    t.forward(a)
    if t.xcor()>300:
      game_on=False
      if t.pencolor()==user_bet:
        announcer.write("YOU WON",align="left",font=("Arial",25,"bold"))
      else:
        announcer.write("YOU LOST",align="left",font=("Arial",25,"bold"))

my_screen.exitonclick()