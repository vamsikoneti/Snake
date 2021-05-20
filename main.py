import pygame
import time
from pygame.locals import *

class Snake:
    def __init__(self, parentScreen):
        self.parentScreen = parentScreen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.direction = 'down'

    def draw(self):
        self.parentScreen.fill((230, 115, 80))

        #draw image as background
        self.parentScreen.blit(self.block, (self.x , self.y))

        pygame.display.flip()

    def moveLeft(self):
        self.direction = 'left'
    
    def moveRight(self):
        self.direction = 'right'
    
    def moveUp(self):
        self.direction = 'up'

    def moveDown(self):
        self.direction = 'down'

    def walk(self):
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y +=10

        if self.direction == 'left':
            self.x -=10
        if self.direction == 'right':
            self.x +=10
        self.draw()



class Game:
    def __init__(self):
        pygame.init()

        #initialize pygame window
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((230, 115, 80))

        #snake class is inside the Game() class
        self.snake = Snake(self.surface)
        self.snake.draw()


    def run(self):
        #event loop
        run = True
        while run:
            for ev in pygame.event.get():

                if ev.type == KEYDOWN:

                    #escape to quit
                    if(ev.key == K_ESCAPE):
                        run = False

                    if(ev.key == K_UP):
                        self.snake.moveUp()

                    if(ev.key == K_DOWN):
                        self.snake.moveDown()

                    if(ev.key == K_LEFT):
                        self.snake.moveLeft()
                        
                    if(ev.key == K_RIGHT):
                        self.snake.moveRight()
                    
                elif (ev.type == QUIT) :
                    run = False

            self.snake.walk()
            #timer to move snake automatically
            time.sleep(0.2)




    


#main routine
if __name__ == "__main__": 
    game = Game()
    game.run()

    

    pygame.display.flip()
