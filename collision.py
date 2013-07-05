from pygame.locals import *
from pygame.math import Vector2
from pygame import Surface
from pygame import mask
from mapp import Map
from player import Player
from projectiles import*
from enemy import*
from settings import*
from pygame.sprite import Sprite


class CollisionManager:
    def __init__(self):
        """Creates collsion manager that provides way of checking
        if 2 object collides"""
        self.is_collision_on = True

    def map_collision(self, mapp, obj_rect, obj_mask):
        """Return True if map and object collide"""
        surf_map = Surface((obj_rect.width, obj_rect.height),
                           pygame.SRCALPHA)
        surf_map.blit(mapp.collision_text, (0, 0), obj_rect)
        mask_map = mask.from_surface(surf_map)
        if mask_map.overlap(obj_mask, (0, 0)) is not None:
            return True
        return False

    def are_colliding(self, object_1, object_2, camera):
        """Return True if 2 objects collide. the objects must have
        texture type AnimatedTexture and function get_onscr_rect(camera)"""
        obj_1_sprite = Sprite()
        obj_1_sprite.mask = object_1.texture.get_collision_mask()
        obj_1_sprite.rect = object_1.get_onscr_rect(camera)
        obj_2_sprite = Sprite()
        obj_2_sprite.mask = object_2.texture.get_collision_mask()
        obj_2_sprite.rect = object_2.get_onscr_rect(camera)

        colliding = pygame.sprite.collide_mask(obj_1_sprite, obj_2_sprite)
        if colliding is not None:
            return True
        return False
