import pygame


class Spaceship:

    image = pygame.image.load('spaceship.png')
    speed = 0.9

    def __init__(self, x, y):
        
        self.x_position = x
        self.y_position = y

        self.health = 100

    def move(self, window, keys):
        
        if keys[pygame.K_w]:
            self.y_position -= Spaceship.speed

        if keys[pygame.K_a]:
            self.x_position -= Spaceship.speed

        if keys[pygame.K_s]:
            self.y_position += Spaceship.speed

        if keys[pygame.K_d]:
            self.x_position += Spaceship.speed

    def draw(self, window):

        coordinates = [self.x_position, self.y_position]
        window.blit(Spaceship.image, coordinates)

