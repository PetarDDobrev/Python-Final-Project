from animated_texture import*
from settings import *


class Particle:
    def __init__(self, texture, frame_num, vec_pos, vec_dir, move_speed):
        """Creates a particle with texutre(sprite sheet),
        numbers of frame the texture has, position on the screen,
        direction and movement speed"""
        self.texture = AnimatedTexture(texture, frame_num, EXP_ANIM_SPEED)
        self.position = vec_pos
        self.direction = vec_dir
        self.speed = move_speed
        self.active = True

    def draw(self, surface):
        """Draws particle on given surface"""
        self.texture.draw(surface, self.position)

    def kill(self):
        """Deactivates the particle"""
        self.active = False


class Explosion(Particle):
    def move(self):
        """Moves the explosion in its direction"""
        self.position.x += self.direction.x * self.speed
        if self.speed < 0:
            self.speed = 0

    def draw(self, surface):
        """Draws the explosion on given surface and
        kills it when teh animation is finished."""
        self.texture.draw(surface, self.position)
        if self.texture.frame == self.texture.max_frame:
            self.kill()


class ParticleManager:
    def __init__(self):
        """Creates a particle manager"""
        self.particles = []

    def add_particle(self, particle):
        """Adds particle to the manager"""
        self.particles.append(particle)

    def update(self):
        """Updates particles state"""
        self.move()

        dead_particles = []
        dead_index = 0
        for particle in self.particles:
            if not particle.active:
                dead_particles.insert(0, dead_index)
            dead_index += 1

        for index in dead_particles:
            self.particles.pop(index)

    def move(self):
        """Moves all particles"""
        for particle in self.particles:
            particle.move()

    def draw(self, surface):
        """Draws all particles"""
        for particle in self.particles:
            particle.draw(surface)

    def restart(self):
        """Removes all particles"""
        del self.particles[0:len(self.particles)]
