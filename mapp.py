import pygame
from pygame.math import Vector2
from pygame import Rect
from settings import WINDOW_WIDTH


class Map:
    def __init__(self, texture, collision_texture):
        """Creates a map with:
        texture and collision texture"""
        self.position = Vector2(0, 0)
        self.texture = pygame.image.load(texture)
        self.collision_text = pygame.image.load(collision_texture)

    def move(self, camera):
        """Sets the position of teh map
        according to the Camera(Viewpor position)"""
        self.position = camera * (-1)

    def draw(self, surface):
        """Draws teh map on given surface"""
        map_rect = Rect(-self. position.x, -self.position.y,
                        WINDOW_WIDTH, self.texture.get_height())
        surface.blit(self.texture, (0, 0), map_rect)
