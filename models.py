import pygame


class Spaceship:

    image = pygame.image.load('spaceship.png')
    speed = 0.5

    def __init__(self, x, y):
        
        self.x_position = x
        self.y_position = y

        self.health = 100

    def move(self, window, keys):
        
        if keys[pygame.K_w] and self.y_position > 0:
            self.y_position -= Spaceship.speed

        if keys[pygame.K_a] and self.x_position > 0:
            self.x_position -= Spaceship.speed

        if keys[pygame.K_s] and self.y_position < window.get_height() - Spaceship.image.get_height():
            self.y_position += Spaceship.speed

        if keys[pygame.K_d] and self.x_position < window.get_width()  - Spaceship.image.get_width():
            self.x_position += Spaceship.speed

    def draw(self, window):

        coordinates = [self.x_position, self.y_position]
        window.blit(Spaceship.image, coordinates)


class Missile:
    
    image = pygame.image.load('missile.png')
    speed = 0.7

    def __init__(self, spaceship):
        
        self.x_position = spaceship.x_position + (Spaceship.image.get_width() / 2) - (Missile.image.get_width() / 2)
        self.y_position = spaceship.y_position - Missile.image.get_height()

        self.damage = 10.5

    def move(self):
        self.y_position -= Missile.speed

    def draw(self, window):

        coordinates = [self.x_position, self.y_position]
        window.blit(Missile.image, coordinates)


class Asteroid:
    
    image = pygame.image.load('asteroid.png')
    speed = 0.7

    def __init__(self, x, y):
        
        self.x_position = x
        self.y_position = y

        self.damage = 20

    def move(self):
        self.y_position += Asteroid.speed

    def draw(self, window):

        coordinates = [self.x_position, self.y_position]
        window.blit(Asteroid.image, coordinates)