import pygame
from pieces import Piece

class Tile:
    hovered = False

    def __init__(self, pos, side, display):
        self.pos = pos
        self.side = side
        self.display = display
        self.setRect()
        self.draw()

    def draw(self):
        pygame.draw.rect(self.display, self.getColor(), self.rect)

    def drawOutline(self):
        if(self.hovered):
            pygame.draw.rect(self.display, self.getColor(), self.rect, 1)
            pygame.draw.rect(self.display, (0,255,0), self.rect, 1)
        else:
            self.draw()
    
    def getColor(self):
        if (self.side == 0):
            return (0,0,0)
        elif (self.side == 1):
            return (150, 150, 150)

    def hover(self):
        if(self.hovered):
            return pygame.Rect((1200/5,1000/6),(90,90))

    def setRect(self):
        self.rect = pygame.Rect(self.pos, (90, 90))
        self.rect.topleft = self.pos