import pygame
from animated_texture import*
from settings import*


class Bar():
    def __init__(self):
        """Creates a bar with backgound texture from settings,
        position from settings, a beam object and font for
        displaying text"""
        self.background = pygame.image.load(BAR_BG_TEXTURE)
        self.position = Vector2(BAR_POS)
        self.beam = Beam()
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)

    def draw(self, surface, weapon_charge, player_score, player_lives):
        """Draws the bar on given surface. player's score is for displaying
        the score and weapon charge is for the beam diplaying"""
        surface.blit(self.background, self.position)
        self.beam.draw(surface, self.position, weapon_charge)
        score_text = self.font.render("SCORE: "+str(player_score), 1,
                                      FONT_COLOR)
        surface.blit(score_text, SCORE_POS + self.position)
        lives_text = self.font.render("LIVES: "+str(player_lives), 1,
                                      FONT_COLOR)
        surface.blit(lives_text, LIVES_POS + self.position)


class Beam():
    def __init__(self):
        """Creates a beam(progress bar)"""
        self.texture = pygame.image.load(BEAM_TEXTURE)
        self.texture_fill = pygame.image.load(BEAM_FILL_TEXTURE)
        self.position = Vector2(BEAM_POS)

    def draw(self, surface, bar_pos, fill_perc):
        """Draws the beam on given surface and postion on it, fill_perc is
        for displaying the filled part of the beam"""
        fill_rect = Rect(0, 0, self.texture_fill.get_width()*fill_perc/100,
                         self.texture_fill.get_height())
        surface.blit(self.texture_fill, self.position + bar_pos, fill_rect)
        surface.blit(self.texture, self.position + bar_pos)
