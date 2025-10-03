import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jogador = Player()
controle_carro = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(jogador.go_up, "Up")
screen.onkey(jogador.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    controle_carro.create_car()
    controle_carro.move_car()

    # Detectar colisão
    for car in controle_carro.all_cars:
        if car.distance(jogador) < 20:
            game_is_on = False
            score.game_over()

    # Detectar vitoria
    if jogador.vitoria():
        jogador.go_to_start()
        controle_carro.level_up()
        score.level_up()

        
screen.exitonclick()