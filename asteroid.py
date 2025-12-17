from circleshape import CircleShape
import pygame
import random
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_high_angle = self.velocity.rotate(new_angle)
        new_low_angle = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast1.velocity = new_high_angle * 1.2
        new_ast2.velocity = new_low_angle * 1.2
