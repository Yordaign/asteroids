from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

white = (255, 255, 255)

class Asteroid(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius, 2)
        
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):  
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        pos_split = self.velocity.rotate(split_angle)
        neg_split = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position, new_radius)
        asteroid_1.velocity = pos_split * 1.2
        asteroid_2 = Asteroid(self.position, new_radius)
        asteroid_2.velocity = neg_split * 1.2
        for group in self.groups():
            group.add(asteroid_1)
            group.add(asteroid_2)
                