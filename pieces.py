import pygame

class Piece:
    def __init__(self, pos, side, display):
        self.pos = pos
        self.side = side
        self.display = display
    
    def draw(self):
        pygame.draw.circle(self.display, self.getColor(), self.pos, 40)
        pygame.draw.circle(self.display, (255,255,255), self.pos, 40, 1)

    def getColor(self):
        if(self.side == 0):
            return (85,85,85)
        elif(self.side == 1):
            return (185, 185, 185)