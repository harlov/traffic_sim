import pygame

from traffic_sim import config
from traffic_sim.domain.car import BaseCarRenderer
from traffic_sim.domain.coordinate import Offset

red = (255, 0, 0)


class CarRenderer(BaseCarRenderer):
    BORDER_WIDTH = 1

    _screen: pygame.Surface

    _surface: pygame.Surface
    _rect: pygame.Rect

    def _draw_border_line(self, p1, p2):
        pygame.draw.line(self._orig_surface, red, p1, p2, self.BORDER_WIDTH)

    def __init__(self, sprite_name: str, screen: pygame.Surface):
        self._screen = screen

        self._surface = pygame.image.load(str(config.RESOURCE_DIRECTORY / sprite_name))
        self._orig_surface = self._surface

        w, h = self._orig_surface.get_width(), self._orig_surface.get_height()

        self._draw_border_line((0, 0), (w, 0))
        self._draw_border_line((0, 0), (0, h))
        self._draw_border_line((w - 1, 0), (w - 1, h - 1))
        self._draw_border_line((0, h - 1), (w - 1, h - 1))
        self._rect = self._surface.get_rect()

    def move(self, offset: Offset):
        print('x move:', offset.x, 'y move:', offset.y)
        self._rect.move_ip(offset.x, offset.y)
        self._screen.blit(self._surface, self._rect)

    def rotate(self, angle: float):
        rotate_angle = angle - 90
        self._surface = pygame.transform.rotate(self._orig_surface, -rotate_angle)
        cx, cy = self._rect.center
        self._rect = self._surface.get_rect()
        self._rect.center = cx, cy
