import pygame
import time
from pygame.locals import *
import random

#grape has dimensions 5x5

class Grape:
    def __init__ (self, parentScreen):
        self.grape = pygame.image.load("resources/grape.png").convert()
        self.parentScreen = parentScreen
        self.x = SIZE * 10
        self.y = SIZE *10

    def draw(self):
        self.parentScreen.blit(self.grape, (self.x , self.y))

        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,20)*SIZE
        self.y = random.randint(1,20)*SIZE

SIZE = 35
class Snake:
    def __init__(self, parentScreen, length):
        self.length = length
        self.parentScreen = parentScreen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def draw(self):
        self.parentScreen.fill((230, 115, 80))

        for i in range (self.length):
            self.parentScreen.blit(self.block, (self.x[i] , self.y[i]))

        pygame.display.flip()


    def increaseLength(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)


    def moveLeft(self):
        self.direction = 'left'
    
    def moveRight(self):
        self.direction = 'right'
    
    def moveUp(self):
        self.direction = 'up'

    def moveDown(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1, 0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]



        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] +=SIZE

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        self.draw()



class Game:
    def __init__(self):
        pygame.init()
        length = 1

        #initialize pygame window
        self.surface = pygame.display.set_mode((750,750))
        self.surface.fill((230, 115, 80))

        #snake class is inside the Game() class
        self.snake = Snake(self.surface, length)
        self.snake.draw()

        #initialize grape
        self.grape = Grape(self.surface)
        self.grape.draw()

    def collision(self, x1, y1, x2, y2):
        if (x1 >= x2 and x1 < x2 + SIZE):
            if (y1 >= y2 and y1 < y2 + SIZE):
                return True
        return False


    def play(self):
        self.snake.walk()
        self.grape.draw()
        self.displayScore()
        pygame.display.flip()

        if self.collision(self.snake.x[0], self.snake.y[0], self.grape.x, self.grape.y):
            self.snake.increaseLength()
            self.grape.move()

    def displayScore(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score:  {self.snake.length}", True, (0,0,0))
        self.surface.blit(score, (800,10))

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

            self.play()
            #timer to move snake automatically
            time.sleep(0.2)




    


#main routine
if __name__ == "__main__": 
    game = Game()
    game.run()

    

    pygame.display.flip()
