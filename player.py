import pygame
from pygame.locals import *
from animated_texture import*
from settings import MAX_WEAPON_COOLDOWN, MAX_WEAPON_CHARGE, MAX_WEAPON_POWER
from settings import IMMORTAL_TIME


class Player:
    def __init__(self, vec_pos, texture):
        """Creates player with a sprite sheet for animation and position"""
        self.texture = AnimatedTexture(texture, 5, 15)
        self.initialize(vec_pos)

    def move(self, window_size):
        """Moves the player with certain keys and doenst allow going
        out of the screen"""
        if self.immortal is not False:
            self.immortal -= 1

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            self.position.y -= self.speed
            if(self.position.y < 0):
                self.position.y = 0
        elif key_pressed[K_DOWN]:
            self.position.y += self.speed
            if(self.position.y > window_size.y - self.texture.frame_height):
                self.position.y = window_size.y - self.texture.frame_height
        if key_pressed[K_LEFT]:
            self.position.x -= self.speed
            if(self.position.x < 0):
                self.position.x = 0
        elif key_pressed[K_RIGHT]:
            self.position.x += self.speed
            if(self.position.x > window_size.x - self.texture.frame_width):
                self.position.x = window_size.x - self.texture.frame_width

        self.rect = Rect((self.position.x, self.position.y),
                         (self.texture.frame_width, self.texture.frame_height))
        is_shooting = False
        if self.cooldown > 0:
            self.cooldown -= 1
            self.key_pressed_old = key_pressed
            return is_shooting

        if self.key_pressed_old[K_SPACE] and not key_pressed[K_SPACE]:
            self.charge = 0
            self.cooldown = MAX_WEAPON_COOLDOWN
            is_shooting = True

        if key_pressed[K_SPACE]:
            if self.weapon_power > 0:
                self.charge += 1
                if self.charge == MAX_WEAPON_CHARGE:
                    self.charge = 0
                    self.weapon_power -= 1
                isShooting = False

        if not self.key_pressed_old[K_SPACE] and not key_pressed[K_SPACE]:
            self.weapon_power = MAX_WEAPON_POWER
            is_shooting = False

        self.key_pressed_old = key_pressed
        return is_shooting

    def draw(self, surface):
        """Draws teh player on given surface"""
        self.texture.draw(surface, self.position)

    def add_score(self, score):

        self.score += score

    def get_world_rect(self, camera):
        """Player's position are on screen position. This function
        retrun player's rectangle with position on the level"""
        return Rect(camera.x + self.position.x, self.position.y,
                    self.rect.width, self.rect.height)

    def get_onscr_pos(self, camera):
        return self.position

    def get_onscr_rect(self, camera):
        return self.rect

    def reset_charge(self):
        self.charge = 0
        self.cooldown = MAX_WEAPON_COOLDOWN
        self.weapon_power = MAX_WEAPON_POWER

    def get_charge(self):
        max_charge = MAX_WEAPON_POWER * MAX_WEAPON_CHARGE
        cur_charge = (MAX_WEAPON_POWER - self.weapon_power)*MAX_WEAPON_CHARGE
        cur_charge += self.charge
        return cur_charge*100 / max_charge

    def kill(self, respawn_pos):
        if self.immortal < 0:
            self.lives -= 1
            self.position = Vector2(respawn_pos)
            self.immortal = IMMORTAL_TIME

    def initialize(self, vec_pos):
        self.position = Vector2(vec_pos)
        self.speed = 8
        self.lives = 3
        self.immortal = IMMORTAL_TIME
        self.score = 0
        self.weapon_power = MAX_WEAPON_POWER
        self.charge = 0
        self.cooldown = 0
        self.key_pressed_old = pygame.key.get_pressed()
        self.rect = Rect((self.position.x, self.position.y),
                         (self.texture.frame_width, self.texture.frame_height))
