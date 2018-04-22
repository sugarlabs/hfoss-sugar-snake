# -*- coding: utf-8 -*-
# MIT License
# 
# Copyright (c) 2016 Amar Prakash Pandey
# Copyright (c) 2018 Aidan Kahrs
# Copyright (c) 2018 Regina Locicero
# Copyright (c) 2018 Calvin Wu
# Copyright (c) 2018 Quintin Reed
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# import library here
import pygame
import time
import random
from os import path
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from sugar3.graphics.style import GRID_CELL_SIZE


class gameClass:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        # contant value initialised
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,155,0)
        self.yellow = (255, 255, 0)

        self.screen = None

        # path for the image folder
        assets = path.join(path.dirname(__file__), 'assets')

        # image loading
        self.snakeimg = pygame.image.load(path.join(assets + '/snake-head.png'))
        self.snakebody = pygame.image.load(path.join(assets + '/snake-body.png'))
        self.snaketail = pygame.image.load(path.join(assets + '/snake-tail.png'))
        self.appleimg = pygame.image.load(path.join(assets + '/apple.png'))
        self.startScreen = pygame.image.load(path.join(assets + '/start-screen.png'))
        self.endScreen = pygame.image.load(path.join(assets + '/end-screen.png'))

        # moving block size
        self.block = 20
        self.appleSize = 30

        # snake image direction variable
        self.direction = "right"

        # init font object with font size 25
        pygame.font.init()
        self.smallfont = pygame.font.Font(None, 20)
        self.medfont = pygame.font.Font(None, 40)
        self.largefont = pygame.font.Font(None, 70)

        # game state variables
        self.gameStarted = False
        self.gameOver = False
        #self.paused = False

        # score
        self.gameScore = 0

    def set_paused(self, paused):
        self.paused = paused

    # function to print score
    def printScore(self,score):
        text = self.medfont.render("Score : " + str(score), True, self.black)
        self.screen.blit(text, [2,2])

    # function for random apple generation
    def randomAppleGen(self):
        randomFruitX = round(random.randrange(0, pygame.display.Info().current_h - self.appleSize) / 10.0) * 10.0
        randomFruitY = round(random.randrange(0, pygame.display.Info().current_h - self.appleSize) / 10.0) * 10.0

        return randomFruitX, randomFruitY

    # function for random multiplication numbers generation
    def randomMultGen(self):
        firstNum = random.randint(2, 12)
        secondNum = random.randint(2, 12)

        return firstNum, secondNum

    # function to print multiplication problem
    def problem(self, numberOne, numberTwo):
        text = self.medfont.render(str(numberOne) + " X " + str(numberTwo) + " = ?", True, self.black)
        self.screen.blit(text, [pygame.display.Info().current_w / 2, 2])

    # function for putting the number label on the apple
    def putNumInApple(self, num, (x, y)):
        label = self.medfont.render(str(num), True, self.black)
        self.screen.blit(label, [x, y])

    # score getter
    def get_score(self):
        return self.gameScore

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # to generate and update snake :P
    def snake(self, block, snakeList):
        # At some point, we may want to rotate the snake's body when it reaches
        # a part where the snake turns
        snakebody = pygame.transform.rotate(self.snakebody, 0)
        tail = pygame.transform.rotate(self.snaketail, 0)

        if direction == "right":
            head = pygame.transform.rotate(self.snakeimg, 270)
            snakebody = pygame.transform.rotate(self.snakebody, 270)

        if direction == "left":
            head = pygame.transform.rotate(self.snakeimg, 90)
            snakebody = pygame.transform.rotate(self.snakebody, 90)

        if direction == "up":
            head = self.snakeimg
            snakebody = self.snakebody

        if direction == "down":
            head = pygame.transform.rotate(self.snakeimg, 180)
            snakebody = pygame.transform.rotate(self.snakebody, 180)


        self.screen.blit(head, (snakeList[-1][0], snakeList[-1][1]))
        for XnY in snakeList[:-1]:
            self.screen.blit(snakebody,(XnY[0], XnY[1]))


    def text_object(self, msg, color,size):
        if size == "small":
            textSurface = self.smallfont.render(msg, True, color)
            return textSurface, textSurface.get_rect()

        if size == "medium":
            textSurface = self.medfont.render(msg, True, color)
            return textSurface, textSurface.get_rect()

        if size == "large":
            textSurface = self.largefont.render(msg, True, color)
            return textSurface, textSurface.get_rect()

    # func to print message on game display
    def message_to_display(self, msg, color, y_displace = 0, size = "small"):
        textSurf , textRect = self.text_object(msg, color, size)
        textRect.center = (pygame.display.Info().current_h/2), (pygame.display.Info().current_h/2) + y_displace
        self.screen.blit(textSurf, textRect)

    def showStartScreen(self):
        while Gtk.events_pending():
                Gtk.main_iteration()
        self.screen.blit(self.startScreen,(0,0))
        myfont=self.largefont
        nlabel=myfont.render("Sugar Snake", 1, self.white)
        dlabel=self.medfont.render("Press the play button in the top left corner to begin.", 1, self.white)
        self.screen.blit(nlabel, (200,200))
        self.screen.blit(dlabel, (400,400))
        pygame.display.update()
    
    def showGameoverScreen(self):
        while Gtk.events_pending():
                Gtk.main_iteration()
        self.screen.blit(self.endScreen,(0,0))
        self.message_to_display("Game Over", self.red, -70, "large")
        text = self.medfont.render("Your final score is : " + str(self.get_score()), True, self.red)
        self.screen.blit(text, [100,100])
        pygame.display.update()
        
    # game starts here
    def run(self):
        # global variable direction
        global direction
        self.screen = pygame.display.get_surface()

        direction = "right"

        # variable init
        running = True

        # snake variables
        snakeList = []
        snakeLength = 1

        # right apple
        randomFruitX, randomFruitY = self.randomAppleGen()

        # wrong apples
        randomFruitX1, randomFruitY1 = self.randomAppleGen()
        randomFruitX2, randomFruitY2 = self.randomAppleGen()
        randomFruitX3, randomFruitY3 = self.randomAppleGen()

        # right answer
        numberOne, numberTwo = self.randomMultGen()

        # wrong answers
        numberOne1, numberTwo1 = self.randomMultGen()
        numberOne2, numberTwo2 = self.randomMultGen()
        numberOne3, numberTwo3 = self.randomMultGen()

        start_x = pygame.display.Info().current_h/2
        start_y = pygame.display.Info().current_h/2

        move_to_h = 10
        move_to_v = 0


        while running :
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()
            if self.gameStarted == False:
                self.showStartScreen()
                continue
            elif self.gameOver == True:
                self.showGameoverScreen()
            else:
                # Pump PyGame messages
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and move_to_h == 0:
                            direction = "left"
                            move_to_h = -self.block
                            move_to_v = 0
                        elif event.key == pygame.K_RIGHT and move_to_h == 0:
                            direction = "right"
                            move_to_h = self.block
                            move_to_v = 0
                        elif event.key == pygame.K_UP and move_to_v == 0:
                            direction = "up"
                            move_to_v = -self.block
                            move_to_h = 0
                        elif event.key == pygame.K_DOWN and move_to_v == 0:
                            direction = "down"
                            move_to_v = self.block
                            move_to_h = 0
                        #elif event.key == pygame.K_SPACE and self.paused == False:
                         #   set_paused(True)
                        #elif event.key == pygame.K_SPACE and self.paused == True:
                         #   set_paused(False)

                if start_x >= pygame.display.Info().current_w or start_x < 0 or start_y >= pygame.display.Info().current_h or start_y < 0:
                    self.gameOver = True

                start_x += move_to_h
                start_y += move_to_v

                self.screen.fill(self.white)
                self.screen.blit(self.appleimg, (randomFruitX, randomFruitY))
                self.screen.blit(self.appleimg, (randomFruitX1, randomFruitY1))
                self.screen.blit(self.appleimg, (randomFruitX2, randomFruitY2))
                self.screen.blit(self.appleimg, (randomFruitX3, randomFruitY3))

                snakeHead = []
                snakeHead.append(start_x)
                snakeHead.append(start_y)
                snakeList.append(snakeHead)

                if len(snakeList) > snakeLength:
                    del snakeList[0]

                self.printScore(snakeLength - 1)

                self.problem(numberOne, numberTwo)

                self.putNumInApple(numberOne * numberTwo, (randomFruitX, randomFruitY))
                self.putNumInApple(numberOne1 * numberTwo1, (randomFruitX1, randomFruitY1))
                self.putNumInApple(numberOne2 * numberTwo2, (randomFruitX2, randomFruitY2))
                self.putNumInApple(numberOne3 * numberTwo3, (randomFruitX3, randomFruitY3))

                self.snake(self.block, snakeList)
                pygame.display.update()

                # to see if snake has eaten himself or not
                for eachSegment in snakeList[:-1]:
                    if eachSegment == snakeHead:
                        self.snake(self.block, snakeList)
                        pygame.time.delay(1000)
                        self.gameOver = True

                if start_x > randomFruitX and start_x < randomFruitX + self.appleSize or start_x + self.block > randomFruitX and start_x + self.block < randomFruitX + self.appleSize:
                    if start_y > randomFruitY and start_y < randomFruitY + self.appleSize:
                        randomFruitX, randomFruitY = self.randomAppleGen()
                        randomFruitX1, randomFruitY1 = self.randomAppleGen()
                        randomFruitX2, randomFruitY2 = self.randomAppleGen()
                        randomFruitX3, randomFruitY3 = self.randomAppleGen()
                        snakeLength += 1
                    if start_y + self.block > randomFruitY and start_y + self.block < randomFruitY + self.appleSize:
                        randomFruitX, randomFruitY = self.randomAppleGen()
                        randomFruitX1, randomFruitY1 = self.randomAppleGen()
                        randomFruitX2, randomFruitY2 = self.randomAppleGen()
                        randomFruitX3, randomFruitY3 = self.randomAppleGen()
                        snakeLength += 1

                if start_x > randomFruitX1 and start_x < randomFruitX1 + self.appleSize or start_x + self.block > randomFruitX1 and start_x + self.block < randomFruitX1 + self.appleSize:
                    if start_y > randomFruitY1 and start_y < randomFruitY1 + self.appleSize:
                        self.gameOver = True

                if start_x > randomFruitX2 and start_x < randomFruitX2 + self.appleSize or start_x + self.block > randomFruitX2 and start_x + self.block < randomFruitX2 + self.appleSize:
                    if start_y > randomFruitY2 and start_y < randomFruitY2 + self.appleSize:
                        self.gameOver = True

                if start_x > randomFruitX3 and start_x < randomFruitX3 + self.appleSize or start_x + self.block > randomFruitX3 and start_x + self.block < randomFruitX3 + self.appleSize:
                    if start_y > randomFruitY3 and start_y < randomFruitY3 + self.appleSize:
                        self.gameOver = True

                self.gameScore = snakeLength-1
            # initialising no. of frames per sec
            self.clock.tick(10)


# # this fuction kicks-off everything 
def main():
    pygame.init()
    screen=pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = gameClass()
    game.run()
    pygame.display.quit()
    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()


