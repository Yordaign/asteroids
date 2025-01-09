from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED
from shot import Shot

white = (255, 255, 255)

class Player(CircleShape):
    def __init__(self, position):
        super().__init__(position, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position, SHOT_RADIUS)
        fired = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity += fired * PLAYER_SHOOT_SPEED