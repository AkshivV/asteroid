import pygame
from constants import *
from circleshape import CircleShape
from player import Player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    game_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        
        updatable.update(dt)

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
