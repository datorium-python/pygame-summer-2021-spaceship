import pygame
import constants

from models import (
    Spaceship,
    Missile,
    Asteroid,
)

from random import randint

pygame.init()

window = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption('spaceship pew pew')
pygame.display.set_icon(constants.ICON_IMAGE)

def render(spaceship, missiles):

    window.blit(constants.BACKGROUND_IMAGE, [0, 0])

    spaceship.draw(window)
    
    for missile in missiles:
        missile.draw(window)

    pygame.display.update()

spaceship = Spaceship(
    x=randint(0, window.get_width() - Spaceship.image.get_width()),
    y=randint(0, window.get_height() - Spaceship.image.get_height()),
)

missiles = []

pygame.time.set_timer(pygame.USEREVENT, 375)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                missile = Missile(spaceship)
                missiles.append(missile)

        if event.type == pygame.USEREVENT:
            print('THIS IS USER EVENT')

    for missile in missiles:

        missile.move()

        if missile.y_position <= -missile.image.get_height():
            missiles.remove(missile)

    keys = pygame.key.get_pressed()
    spaceship.move(window, keys)
    
    render(spaceship, missiles)