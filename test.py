import pygame
from pieces import Piece

pygame.init()

display = pygame.display.set_mode((1200, 950))
bgcolor = (255,255,255)

Piece((500,500), 0, display).draw()

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()