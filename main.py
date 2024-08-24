import pygame
 
from constants import *
from player import Player
from shot import Shot
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f'Screen width: {SCREEN_WIDTH}')
  print(f'Screen height: {SCREEN_HEIGHT}')

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  fpsClock = pygame.time.Clock()
  dt = 0

  # Groups
  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatables, drawables)
  Asteroid.containers = (asteroids, updatables, drawables)
  AsteroidField.containers = (updatables)
  Shot.containers = (shots, updatables, drawables)

  player_x = SCREEN_WIDTH / 2
  player_y = SCREEN_HEIGHT / 2
  player = Player(player_x, player_y)

  asteroid_field = AsteroidField()

  # game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for updatable in updatables:
      updatable.update(dt)

    for asteroid in asteroids:
      for shot in shots:
        if(asteroid.collision(shot) == True):
          asteroid.split()
          shot.kill()

      if(asteroid.collision(player) == True):
        print('Game over!')
        return
    
    for shot in shots:
      shot.update(dt)
      
    screen.fill('black')

    for drawable in drawables:
      drawable.draw(screen) 
    
    pygame.display.flip()

    dt = fpsClock.tick(60) / 1000

if __name__ == "__main__":
    main()