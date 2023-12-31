from turtle import Screen, Turtle
from random import randint
from time import sleep


display_surface = Screen()
display_surface.bgcolor('black')
display_surface.setup(600, 600)
display_surface.title("~~Snake Game~~~")


def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_position(object):
    x = randint(-270, 270)
    y = randint(-270, 230)
    object.goto(x, y)


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)


def go_up():
    snake_head.direction = "up"


snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)

display_surface.listen()
display_surface.onkeypress(go_up, "Up")


running = True
while running:
    display_surface.update()
    move_snake()
    sleep(0.2)
