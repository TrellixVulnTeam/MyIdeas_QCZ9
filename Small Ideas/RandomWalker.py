import pygame
import math
import sys

pygame.init()

field = pygame.display.set_mode((1200,800))
pygame.display.set_caption('randomwalker')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    field.fill((0,44,44))
    pygame.display.update()

