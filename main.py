import pygame
import time
from pygame.locals import *

def drawBlock():
    surface.fill((230, 115, 80))
    surface.blit(block, (blx, bly))
    pygame.display.flip()

#main routine
if __name__ == "__main__": 
    pygame.init()

    #initialize pygame window
    surface = pygame.display.set_mode((1000, 1000))
    surface.fill((230, 115, 80))

    block = pygame.image.load("resources/block.png").convert()

    blx = 100
    bly = 100
    #draw image as background
    surface.blit(block, (blx, bly))

    pygame.display.flip()

    #event loop
    run = True
    while run:
        for ev in pygame.event.get():

            if ev.type == KEYDOWN:

                #escape to quit
                if(ev.key == K_ESCAPE):
                    run = False

                if(ev.key == K_UP):
                    bly -= 10
                    drawBlock()
                if(ev.key == K_DOWN):
                    bly +=10
                    drawBlock()
                if(ev.key == K_LEFT):
                    blx -=10
                    drawBlock()
                if(ev.key == K_RIGHT):
                    blx +=10
                    drawBlock()
                
            elif (ev.type == QUIT) :
                run = False


    
