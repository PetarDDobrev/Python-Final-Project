import pygame
import sys
from pygame.locals import K_RETURN, K_UP, K_DOWN
from pygame.math import Vector2
from pygame import Rect
from settings import MAIN_TEXTURE, CONTROLS_TEXTURE, NG_TEXTURE, NG_TEXTURE_S
from settings import C_TEXTURE, C_TEXTURE_S, E_TEXTURE, E_TEXTURE_S
from settings import B_TEXTURE, B_TEXTURE_S


class Button:
    def __init__(self, position, texture, texture_selected, goto):
        self.texture = pygame.image.load(texture)
        self.texture_selected = pygame.image.load(texture_selected)
        self.is_selected = False
        position_offset = Vector2(self.texture.get_width()/2,
                                  self.texture.get_height()/2)
        self.position = Vector2(position - position_offset)
        self.goto = goto

    def draw(self, surface):
        if self.is_selected is True:
            surface.blit(self.texture_selected, self.position)
            return
        surface.blit(self.texture, self.position)


class Menu:
    def __init__(self, texture_bg):
        self.texture = pygame.image.load(texture_bg)
        self.buttons = []
        self.position = Vector2(0, 0)
        self.buttons_number = 0
        self.selected_button = 0

    def add_button(self, button):
        self.buttons.append(button)
        self.buttons_number += 1

    def update(self, button_change):
        self.buttons[self.selected_button].is_selected = False
        self.selected_button += button_change
        if self.selected_button < 0:
            self.selected_button = 0
        if self.selected_button == self.buttons_number:
            self.selected_button -= 1
        self.buttons[self.selected_button].is_selected = True

    def get_button_goto(self):
        return self.buttons[self.selected_button].goto

    def draw(self, surface):
        surface.blit(self.texture, self.position)
        for button in self.buttons:
            button.draw(surface)


class MainMenu:
    def __init__(self):
        self.main_menu = Menu(MAIN_TEXTURE)
        self.control_menu = Menu(CONTROLS_TEXTURE)
        self.current = self.main_menu
        self.buttons_goto = {"main": self.main_menu,
                             "controls": self.control_menu}
        self.key_pressed_old = pygame.key.get_pressed()
        self.initialize()

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_RETURN] and not self.key_pressed_old[K_RETURN]:
            btn_goto = self.current.get_button_goto()
            if btn_goto == "exit":
                pygame.quit()
                sys.exit()
            elif btn_goto == "play":
                return True
            else:
                self.current = self.buttons_goto[btn_goto]
        button_change = 0
        if key_pressed[K_UP] and not self.key_pressed_old[K_UP]:
            button_change = -1
        if key_pressed[K_DOWN] and not self.key_pressed_old[K_DOWN]:
            button_change = 1

        self.current.update(button_change)
        self.key_pressed_old = key_pressed
        return False

    def draw(self, surface):
        self.current.draw(surface)

    def initialize(self):
        button = Button(Vector2(640, 280), NG_TEXTURE, NG_TEXTURE_S, "play")
        self.main_menu.add_button(button)
        button = Button(Vector2(640, 400), C_TEXTURE, C_TEXTURE_S, "controls")
        self.main_menu.add_button(button)
        button = Button(Vector2(640, 520), E_TEXTURE, E_TEXTURE_S, "exit")
        self.main_menu.add_button(button)
        button = Button(Vector2(640, 520), B_TEXTURE, B_TEXTURE_S, "main")
        self.control_menu.add_button(button)
