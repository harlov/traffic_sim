import dataclasses
from typing import List

from .car import Car


@dataclasses.dataclass
class Track:
    cars: List[Car]

    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def process(self):
        for car in self.cars:
            car.process()
