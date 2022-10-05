import pygame

pygame.init()
    
display = pygame.display.set_mode((1200, 950))
bgcolor = (255,255,255)

pygame.display.set_caption("Checkers")

display.fill(bgcolor)

class Tile:
    hovered = False

    def __init__(self, pos, side):
        self.pos = pos
        self.side = side
        self.setRect()
        self.draw()

    def draw(self):
        display.blit(display, self.rect)
        pygame.draw.rect(display, self.getColor(), self.rect)
        posX = self.pos[0]
        posY = self.pos[1]
        pygame.draw.rect(display, (0,255,0), pygame.Rect((posX-(posX%90)/(posX%90), posY-(posY%90)/(posY%90)),(90,90)),1)
        print("Side:", self.side, "|", self.pos, "(" , posX-(posX%90)/(posX%90), "," , posY-(posY%90)/(posX%90), ")")
    
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


def generateBoard():
    #(240,167)
    startX = 1200/5
    startY = 1000/6
    for i in range(8):
        for j in range(8):
            if(i % 2 == 0):
                if(j % 2 == 0):
                    Tile((startX+(j*90), startY+(i*90)), 0)
                else:
                    Tile((startX+(j*90), startY+(i*90)), 1)
            else:
                if(j % 2 == 0):
                    Tile((startX+(j*90), startY+(i*90)), 1)
                else:
                    Tile((startX+(j*90), startY+(i*90)), 0)

def generatePieces():
    blackPiece = pygame.image.load("blackPiece.png")
    whitePiece = pygame.image.load("whitePiece.png")
    pieceW = blackPiece.get_rect().width
    pieceH = blackPiece.get_rect().height
    blackPiece = pygame.transform.scale(blackPiece, (pieceW/4, pieceH/4))
    whitePiece = pygame.transform.scale(whitePiece, (pieceW/4, pieceH/4))

    displayPieces(blackPiece, 0)
    displayPieces(whitePiece, 1)

def displayPieces(piece, side):
    if(side == 0):
        startX = 1200/5.45
        startY = 1000/1.68
        for i in range(3):
            for j in range(4):
                if(i == 0):
                    display.blit(piece, (startX+(j*180)+90, startY))
                elif(i == 1):
                    display.blit(piece, (startX+(j*180), startY+90))
                elif(i == 2):
                    display.blit(piece, (startX+(j*180)+90, startY+180))
    else:
        startX = 1200/5.45
        startY = 1000/6.8
        for i in range(3):
            for j in range(4):
                if(i == 0):
                    display.blit(piece, (startX+(j*180), startY))
                elif(i == 1):
                    display.blit(piece, (startX+(j*180)+90, startY+90))
                elif(i == 2):
                    display.blit(piece, (startX+(j*180), startY+180))

def onHover(pos, object):
    posX = pos[0]
    posY = pos[1]
    #pygame.draw.rect(display, (0,255,0), (1200/5,1000/6,90,90), 2)      
    hitbox = (posX-(posX%90)/(posX%90), posY-(posY%90)/(posY%90))
    #object.rect.collidepoint(pygame.mouse.get_pos())



def main():
    exit = False
    generateBoard()
    generatePieces()
    pygame.draw.rect(display, (0,0,0), (1200/5,1000/6,720,720), 2)

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        pygame.display.update()

if(__name__ == "__main__"):
    main()