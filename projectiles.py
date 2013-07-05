from animated_texture import*
from settings import BULLET_SPEED, B_RIGHT_BORDER, B_LEFT_BORDER


class Bullet:
    def __init__(self, texture, frame_num, vec_pos, vec_dir, power):
        """Creates a bullet with texture(spite shteet),
        numbers of frame the texture has, position on the screen, direction
        and power of teh bullet(damage)"""
        self.texture = AnimatedTexture(texture, frame_num, 0)
        self.texture.paused = True
        self.texture.frame = power
        self.position = vec_pos
        self.direction = vec_dir
        self.speed = BULLET_SPEED
        self.active = True

    def draw(self, surface):
        """Draws bullet on given surface"""
        self.texture.draw(surface, self.position)

    def kill(self):
        """Deactivates bullet"""
        self.active = False

    def get_onscr_pos(self, camera):
        """Return the position of the buller according
        to the screen position on teh map(CAMERA)"""
        return self.position

    def get_onscr_rect(self, camera):
        """Return bullet rectangle according to the
        screen position on teh map(CAMERA)"""
        onscr_pos = self.get_onscr_pos(camera)
        return Rect(onscr_pos.x, onscr_pos.y, self.texture.frame_width,
                    self.texture.frame_height)

    def get_world_rect(self, camera):
        position = self.position + camera
        return Rect(position.x, position.y, self.texture.frame_width,
                    self.texture.frame_height)


class PlayerBullet(Bullet):
    def move(self):
        """Moves the player bullet in its direction"""
        self.position.x += self.direction.x * self.speed
        if self.position.x > B_RIGHT_BORDER:
            self.kill()

    def is_max_power(self):
        """Return if the bullet is max powered"""
        return self.texture.frame == 0


class EnemyBullet(Bullet):
    def move(self):
        """Moves the enemy bullet in its direction"""
        self.position.x += self.direction.x * self.speed
        self.position.y += self.direction.y * self.speed
        if self.position.x < B_LEFT_BORDER or self.position.x > B_RIGHT_BORDER:
            self.kill()
