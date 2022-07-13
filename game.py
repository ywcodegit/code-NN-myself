from car import car
import pygame as pg
import sys

cars = []
for i in range(100):
    cars.append(car(2 * np.random.random((178, 1)) - 1))

#game

screen = pg.set_mode((500, 500))
img = pg.image.load("car.png")
with open("map.txt", "r") as file:
    map = file.read().split("\n")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.update()
