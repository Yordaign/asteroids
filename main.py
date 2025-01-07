import pygame
from constants import *
from player import Player

def main():
    pygame.init(),
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

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

if __name__ == "__main__":
    main()
