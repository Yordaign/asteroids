import pygame
from constants import *

def main():
    pygame.init(),
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    colour = (0,140,0)
    fps = pygame.time.Clock()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill(colour)
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            dt = fps / 1000

if __name__ == "__main__":
    main()
