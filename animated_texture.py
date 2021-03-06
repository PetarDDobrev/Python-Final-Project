import pygame
from pygame.math import Vector2
from pygame import Rect
from pygame import Surface
from pygame import mask


class AnimatedTexture:
    def __init__(self, texture, frame_num, anim_speed):
        """Creates animation from sprite sheet. texture is teh sprite sheet.
        frame_num is number of the frames. anim_speed shows for how many
        ticks every frame is drawn during animation"""
        self.texture = pygame.image.load(texture)
        self.frame = 0
        self.max_frame = frame_num
        self.frame_height = self.texture.get_rect().bottom
        self.frame_width = self.texture.get_rect().right / self.max_frame
        self.speed = anim_speed
        self.counter = 0
        self.surf_rect = Rect(0, 0, 0, 0)
        self.paused = False
        self.set_surf_rect()

    def draw(self, surface, vec_pos):
        """Draws current frame"""
        if self.frame == self.max_frame:
                    self.frame = 0
        self.set_surf_rect()
        surface.blit(self.texture, vec_pos, self.surf_rect)
        if not self.paused:
            self.counter += 1
            if self.counter == self.speed:
                self.counter = 0
                self.frame += 1

    def set_surf_rect(self):
        """Sets the rectangle of the current frame according is position
        on the sprite sheet"""
        self.surf_rect = Rect((self.frame*self.frame_width, 0),
                              (self.frame_width, self.frame_height))

    def get_collision_mask(self):
        """Return the mask of teh current frame"""
        surface = Surface((self.surf_rect.width, self.surf_rect.height),
                          pygame.SRCALPHA)
        surface.blit(self.texture, (0, 0), self.surf_rect)
        return mask.from_surface(surface)
