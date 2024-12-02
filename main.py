import sys
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    # add groups to Player object
    Player.containers = (updatable, drawable)
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if obj.collide(player):
                print("Game over!")
                sys.exit(1)
            for bullet in shots:
                if bullet.collide(obj):
                    obj.split()
                    bullet.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        # player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(50) / 1000


if __name__ == "__main__":
    main()
