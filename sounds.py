from pygame.mixer import Sound
from settings import SOUNDS_PATH
from pygame.math import Vector2


class SoundManager:
    def __init__(self):
        """Creates sound manager with some sounds"""
        self.is_sound_on = True
        self.enemy_explosion = Sound(SOUNDS_PATH + "explosion.wav")
        self.player_explosion = Sound(SOUNDS_PATH + "explosion.wav")
        self.player_blast = Sound(SOUNDS_PATH + "player_blast1.wav")
        self.enemy_blast = Sound(SOUNDS_PATH + "enemy_blast.wav")
        self.max_dist = 2000

    def volume(self, source_pos, dest_pos):
        """Return number from 0 to 1 depending on
        source position(where sound comes from) and
        destination position(whre the soudn is heard.
        This number is used for changing the
        volume of a sound"""
        distance = Vector2(source_pos - dest_pos).length()
        if distance >= self.max_dist:
            return 0
        return (self.max_dist - distance) / self.max_dist
