import pygame

pygame.init()

class ToothPick():
    def __init__(self, coord1, coord2, orient, color):
        self.coord1 = coord1
        self.coord2 = coord2
        self.orient = orient
        self.color = color


screen = pygame.display.set_mode((400,600))

pick = ToothPick
pick.coord1 = (150,150)
pick.coord2 = (200,200)

pygame.draw.line(screen, (255,25,25), pick.coord1, pick.coord2, 5 )

pygame.display.update()


