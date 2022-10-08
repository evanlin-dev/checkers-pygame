import pygame

import menu
from tiles import Tile
from pieces import Piece

pygame.init()
    
display = pygame.display.set_mode((1200, 950))
bgcolor = (255,255,255)

pygame.display.set_caption("Checkers")

display.fill(bgcolor)

tilesArr = []
piecesArr = []

def generateBoard():
    #(240,167)
    startX = 1200/5
    startY = 1000/6
    for i in range(8):
        for j in range(8):
            if(i % 2 == 0):
                if(j % 2 == 0):
                    tilesArr.append(Tile((startX+(j*90), startY+(i*90)), 0, display))
                else:
                    tilesArr.append(Tile((startX+(j*90), startY+(i*90)), 1, display))
            else:
                if(j % 2 == 0):
                    tilesArr.append(Tile((startX+(j*90), startY+(i*90)), 1, display))
                else:
                    tilesArr.append(Tile((startX+(j*90), startY+(i*90)), 0, display))

def generatePieces(side):
    startX = 1200/4.2
    startY = 1000/4.7
    if(side == 0):
        #startX = 1200/4.2
        #startY = 1000/1.51
        for i in range(3):
            for j in range(4):
                if(i == 0):
                    piecesArr.append(Piece((startX+(j*180)+90, startY+(5*90)), 0, display))
                elif(i == 1):
                    piecesArr.append(Piece((startX+(j*180), startY+90+(5*90)), 0, display))
                elif(i == 2):
                    piecesArr.append(Piece((startX+(j*180)+90, startY+180+(5*90)), 0, display))
    else:
        #startX = 1200/4.2
        #startY = 1000/4.7
        for i in range(3):
            for j in range(4):
                if(i == 0):
                    piecesArr.append(Piece((startX+(j*180), startY), 1, display))
                elif(i == 1):
                    piecesArr.append(Piece((startX+(j*180)+90, startY+90), 1, display))
                elif(i == 2):
                    piecesArr.append(Piece((startX+(j*180), startY+180), 1, display))

def displayPieces():
    for piece in piecesArr:
        piece.draw()

def movePiece(piece, tile):
    index = piecesArr.index(piece)
    piecesArr[index].pos = (tile.pos[0]+45, tile.pos[1]+45)
    displayPieces()

def main():
    exit = False
    generateBoard()
    generatePieces(0)
    generatePieces(1)

    while not exit:
        for event in pygame.event.get():
            for tile in tilesArr:
                if tile.rect.collidepoint(pygame.mouse.get_pos()):
                    #print(tile.pos)
                    tile.hovered = True
                else:
                    tile.hovered = False
                #pygame.draw.rect(display, (0,0,0), (1200/5,1000/6,720,720), 2)
                tile.drawOutline()
                displayPieces();
            if event.type == pygame.QUIT:
                exit = True

        pygame.display.update()

if(__name__ == "__main__"):
    main()