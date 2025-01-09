from constants import SHOT_RADIUS
from circleshape import *

white = (255, 255, 255)

class Shot(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position, radius)
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
    
