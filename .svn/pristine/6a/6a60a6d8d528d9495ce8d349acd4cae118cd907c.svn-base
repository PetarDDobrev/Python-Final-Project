import pygame
from animated_texture import*
from settings import*
from random import randint


class Enemy:
    def __init__(self, vec_pos, vec_dir, move_speed, texture,
                 frame_num, anim_speed):
        self.position = vec_pos
        self.texture = AnimatedTexture(texture, frame_num, anim_speed)
        self.direction = vec_dir
        self.speed = move_speed
        self.cooldown = 0
        self.active = True
        self.rect = Rect((self.position.x, self.position.y),
                         (self.texture.frame_width, self.texture.frame_height))

    def draw(self, surface, camera):
        if not self.is_on_screen(camera):
            return
        self.update_rect()
        self.texture.draw(surface, self.position - camera)

    def is_on_screen(self, camera):
        left_border = self.position.x - camera.x > - 100
        right_border = self.position.x - camera.x < WINDOW_WIDTH
        if left_border and right_border:
            return True
        return False

    def update_rect(self):
        self.rect = Rect((self.position.x, self.position.y),
                         (self.texture.frame_width, self.texture.frame_height))

    def get_onscr_pos(self, camera):
        return self.position - camera

    def get_onscr_rect(self, camera):
        onscr_pos = self.get_onscr_pos(camera)
        return Rect(onscr_pos.x, onscr_pos.y, self.texture.frame_width,
                    self.texture.frame_height)

    def kill(self):
        self.active = False


class FlyingSoucer(Enemy):
    def move(self, camera):
        self.position.y += self.direction.y*self.speed
        if self.position.y < FS_TOP_BORDER:
            self.position.y = FS_TOP_BORDER
            self.direction.y *= -1
        if self.position.y > FS_BOTTOM_BORDER:
            self.position.y = FS_BOTTOM_BORDER
            self.direction.y *= -1

        #self.position.x -= 1

        is_shooting = False
        self.cooldown -= 1
        if self.is_on_screen(camera) and self.cooldown < 1:
            is_shooting = True
            self.cooldown = FS_MAX_COOLDOWN
        return is_shooting

    def get_type(self):
        return FLYING_SOUCER

    def get_points(self):
        return FS_POINTS


class Walker(Enemy):
    def move(self, camera):
        is_shooting = False
        self.cooldown -= 1
        if self.is_on_screen(camera) and self.cooldown < 1:
            is_shooting = True
            self.cooldown = W_MAX_COOLDOWN
        return is_shooting

    def get_type(self):
        return WALKER

    def get_dir(self, player_center, camera):
        return (player_center + camera - Vector2(self.rect.center)).normalize()

    def get_points(self):
        return W_POINTS


class Turret(Enemy):
    def move(self, camera):
        is_shooting = False
        self.cooldown -= 1
        if self.is_on_screen(camera) and self.cooldown < 1:
            is_shooting = True
            self.cooldown = T_MAX_COOLDOWN

        return is_shooting

    def get_type(self):
        return TURRET

    def get_dir(self, player_center, camera):
        return (player_center + camera - Vector2(self.rect.center)).normalize()

    def get_points(self):
        return T_POINTS


class Suicide(Enemy):
    def move(self, camera):
        if self.texture.frame != self.texture.max_frame:
            self.position.x += self.direction.x * self.speed
            self.position.y += self.direction.y * self.speed
        self.direction = Vector2(randint(-10, 10), randint(-5, 5))
        if self.direction.length() == 0:
            return False
        self.direction = self.direction.normalize()
        self.position.x += self.direction.x * self.speed
        if self.position.y > S_BOTTOM_BORDER:
            self.direction.y = randint(-5, -1)
            self.direction = self.direction.normalize()
        if self.position.y < S_TOP_BORDER:
            self.direction.y = randint(1, 5)
            self.direction = self.direction.normalize()
        self.position.y += self.direction.y * self.speed
        return False

    def get_points(self):
        return S_POINTS

    def get_type(self):
        return SUICIDE
