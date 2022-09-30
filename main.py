import pygame

pygame.init()
    
# CREATING CANVAS
display = pygame.display.set_mode((1200, 1000))
bgcolor = (255,255,255)
# TITLE OF CANVAS
pygame.display.set_caption("Checkers")

#bg = pygame.image.load("background.png")
#width = bg.get_rect().width
#height = bg.get_rect().height
#bg = pygame.transform.scale(bg, (width/2, height/2))
display.fill(bgcolor)
#display.blit(bg, (1200/5,1000/6))

def generateBoard():
    startX = 1200/5
    startY = 1000/6
    for i in range(8):
        for j in range(8):
            if(i % 2 == 0):
                if(j % 2 == 0):
                    pygame.draw.rect(display, (0,0,0), (startX+(j*90), startY+(i*90), 90, 90))
                else:
                    pygame.draw.rect(display, (255,0,0), (startX+(j*90), startY+(i*90), 90, 90))
            else:
                if(j % 2 == 0):
                    pygame.draw.rect(display, (255,0,0), (startX+(j*90), startY+(i*90), 90, 90))
                else:
                    pygame.draw.rect(display, (0,0,0), (startX+(j*90), startY+(i*90), 90, 90))

def generatePieces():
    blackPieces = []
    whitePieces = []
    blackPieceImg = pygame.image.load("blackPiece.png")
    whitePieceImg = pygame.image.load("whitePiece.png")
    pieceW = blackPieceImg.get_rect().width
    pieceH = blackPieceImg.get_rect().height
    blackPieceImg = pygame.transform.scale(blackPieceImg, (pieceW/4, pieceH/4))
    whitePieceImg = pygame.transform.scale(whitePieceImg, (pieceW/4, pieceH/4))
    for i in range(12):
        blackPieces.append(blackPieceImg)
        whitePieces.append(whitePieceImg)

    displayPieces(blackPieces, 0)
    displayPieces(whitePieces, 1)

def displayPieces(pieceList, side):
    startX = 1200/5.45
    startY = 1000/6.8
    if(side == 0):
        for i in range(8):
            for j in range(8):
                if(i < 3):
                    display.blit(pieceList[i], (startX+(i*5), startY+(i*5)))
                if(i > 4):
                    display.blit(pieceList[i], (startX+(i*3), startY+(i*3)))
    else:
        for i in range(8):
            for j in range(8):
                if(i < 3):
                    display.blit(pieceList[i], (startX+(i*5), startY+(i*5)))
                if(i > 4):
                    display.blit(pieceList[i], (startX+(i*3), startY+(i*3)))
                

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