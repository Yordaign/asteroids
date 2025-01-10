import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    position = pygame.Vector2(x, y)
    player = Player(position)
    asteroidfield = AsteroidField()

    background_colour = (0,0,0)
    fps = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(background_colour)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        for sprite in updatable:
            sprite.update(dt)
        for sprite in asteroids:
            if sprite.collision(player):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.kill()
                    shot.kill()



if __name__ == "__main__":
    main()
