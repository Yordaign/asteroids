import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, position, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        radius1 = self.radius
        radius2 = other.radius
        return self.position.distance_to(other.position) <= radius1 + radius2
