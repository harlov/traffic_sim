import abc
import dataclasses
import math

from .coordinate import Coordinate
from .coordinate import Offset


class BaseCarRenderer(abc.ABC):
    @abc.abstractmethod
    def move(self, offset: Offset):
        pass

    @abc.abstractmethod
    def rotate(self, angle: float):
        pass


def degrees2radians(degrees: float) -> float:
    return degrees * math.pi / 180


class MoveDirector:
    _renderer: BaseCarRenderer
    speed: float
    turn_speed: int
    _direction: float
    position: Coordinate

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
        self._renderer.rotate(value)

    def __init__(self, renderer: BaseCarRenderer, speed: float, direction: float, position: Coordinate,
                 turn_speed: int):
        self._renderer = renderer
        self.speed = speed
        self.position = position

        self.direction = direction

        self.turn_speed = turn_speed

        self._move_to(self.position.x, self.position.y)

    def next(self) -> None:
        self.direction += self.turn_speed

        direction_rad = degrees2radians(self.direction)

        y_diff = round(math.sin(direction_rad) * self.speed)
        x_diff = round(math.cos(direction_rad) * self.speed)

        print('direction: ', self.direction, 'rad: ', direction_rad, 'x diff: ', x_diff, 'y_diff: ', y_diff)
        self._move_to(x_diff, y_diff)

    def _move_to(self, x_diff: int, y_diff: int) -> None:
        self._renderer.move(Offset(x=x_diff, y=y_diff))
        self.position = Coordinate(x=self.position.x + x_diff,
                                   y=self.position.y + y_diff)


class Car:
    idn: int
    renderer: BaseCarRenderer

    def __init__(
            self,
            idn: int,
            position: Coordinate,
            speed: float,
            turn_speed: int,
            direction: float,
            renderer: BaseCarRenderer
    ):
        self.renderer = renderer

        self.idn = idn

        self._move_director = MoveDirector(
            renderer=renderer,
            speed=speed,
            turn_speed=turn_speed,
            direction=direction,
            position=position,
        )

    def process(self):
        self._move_director.next()
