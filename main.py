import time
from turtle import Screen
from player import Player
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = Cars()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()






screen.exitonclick()