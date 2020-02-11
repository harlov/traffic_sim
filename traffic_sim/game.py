import sys
import time

import pygame

from traffic_sim.engine import CarRenderer
from traffic_sim.domain.car import Car
from traffic_sim.domain.coordinate import Coordinate

FRAME_RATE = 40
FRAME_DELAY = 1.0 / FRAME_RATE

ROTATE_SPEED = 10


def main():
    pygame.init()
    screen_size = 1024, 768
    background_color = 0, 100, 0
    screen = pygame.display.set_mode(screen_size)

    cars = []
    car_id_gen = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                car_id_gen += 1

                cars.append(
                    Car(car_id_gen,
                        position=Coordinate(500, 50),
                        speed=5,
                        turn_speed=1,
                        direction=45,
                        renderer=CarRenderer('car_60.png',
                                             screen=screen)
                        )
                )

        screen.fill(background_color)

        for car in cars:
            car.process()

        pygame.display.flip()

        time.sleep(FRAME_DELAY)


if __name__ == '__main__':
    main()
