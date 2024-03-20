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

    # Detect collision with car 
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()







screen.exitonclick()