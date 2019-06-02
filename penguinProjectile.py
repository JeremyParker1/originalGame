import pygame
import os

current_path = os.path.dirname(__file__)  # Where your .py file is located
image_path = os.path.join(current_path, 'images')  # The image folder path for penguinRun
bulletFolder = os.path.join(image_path, 'bullets')
bulletLeft = pygame.image.load(os.path.join(bulletFolder, 'bulletLeft.png'))
bulletRight = pygame.image.load(os.path.join(bulletFolder, 'bulletRight.png'))

class projectile(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 25 * facing




    def draw(self, window):
        if self.facing == 1:
            window.blit(bulletRight, (self.x, self.y))
        else:
            window.blit(bulletLeft, (self.x, self.y))
            #TODO: fix bullet release points facing left and right, crouching left and right
            #TODO: add shooting animation for crouching, implement reload animation
