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

class snakeClass:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        # contant value initialised
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,155,0)
        
        # display init
        display_width = 800
        display_height = 600
        
        
        # path for the image folder
        assets = path.join(path.dirname(__file__), 'assets')
        sound_folder = path.join(path.dirname(__file__), 'sounds')
        
        
        
        # image loading for both apple and snake
        self.snakeimg = pygame.image.load(path.join(assets + '/snake.png'))
        self.snakebody = pygame.image.load(path.join(assets + '/body.png'))
        self.snaketail = pygame.image.load(path.join(assets + '/tail.png'))
        self.gameicon = pygame.image.load(path.join(assets + '/gameicon.png'))
        self.appleimg = pygame.image.load(path.join(assets + '/apple.png'))
        
        # moving block size
        self.block = 20
        self.appleSize = 30
        
        # snake image direction variable
        self.direction = "right"
        
        # init font object with font size 25 
        self.smallfont = pygame.font.SysFont("comicsansms", 20)
        self.medfont = pygame.font.SysFont("comicsansms", 40)
        self.largefont = pygame.font.SysFont("comicsansms", 70)
        
        self.paused = False

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass



    # function to print score
    def score(score):
        text = smallfont.render("Score : " + str(score), True, black)
        gameDisplay.blit(text, [2,2])
    
    
    # function for random apple generation
    def randomAppleGen():
        randomFruitX = round(random.randrange(0, display_width - appleSize) / 10.0) * 10.0
        randomFruitY = round(random.randrange(0, display_height - appleSize) / 10.0) * 10.0
    
        return randomFruitX, randomFruitY
    
    # to generate and update snake :P
    def snake(block, snakeList):
        # At some point, we may want to rotate the snake's body when it reaches
        # a part where the snake turns
        body = pygame.transform.rotate(snakebody, 0)
        tail = pygame.transform.rotate(snaketail, 0)
        
        if direction == "right":
            head = pygame.transform.rotate(snakeimg, 270)
    
        if direction == "left":
            head = pygame.transform.rotate(snakeimg, 90)
    
        if direction == "up":
            head = snakeimg
    
        if direction == "down":
            head = pygame.transform.rotate(snakeimg, 180)
    
    
        # This method is just working, but not good.
        # Will have to hamake it better and add the snake tail as well.
        gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
        for XnY in snakeList[:-1]:
            # gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
            pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block, block])
    
    
    def text_object(msg, color,size):
        if size == "small": 
            textSurface = smallfont.render(msg, True, color)
            return textSurface, textSurface.get_rect()
    
        if size == "medium":
            textSurface = medfont.render(msg, True, color)
            return textSurface, textSurface.get_rect()
    
        if size == "large":
            textSurface = largefont.render(msg, True, color)
            return textSurface, textSurface.get_rect()
    
    # func to print message on game display
    def message_to_display(msg, color, y_displace = 0, size = "small"):
        textSurf , textRect = text_object(msg, color, size)
        textRect.center = (display_width/2), (display_height/2) + y_displace
        gameDisplay.blit(textSurf, textRect)
    
    
    # game starts here
    def run():
        # global variable direction
        global direction
        global isDead
    
        # menu sound stops
        pygame.mixer.music.fadeout(600)
        
        direction = "right"
    
        # variable init 
        gameExit = False
        gameOver = False
        isDead = False
    
        # snake variables
        snakeList = []
        snakeLength = 1
    
        randomFruitX, randomFruitY = randomAppleGen()
    
        start_x = display_width/2
        start_y = display_height/2
        
        move_to_h = 10
        move_to_v = 0
    
        while not gameExit :
            if gameOver == True:
                menu_song = pygame.mixer.music.load(path.join(sound_folder, "gameover.ogg"))
                pygame.mixer.music.play(-1)
    
                while gameOver == True :
                    gameDisplay.fill(white)
                    message_to_display("Game Over", red, -70, "large")
                    text = smallfont.render("Your final score is : " + str(snakeLength), True, black)
                    gameDisplay.blit(text, [300,300])
                    
                    pygame.display.update()
    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameOver = False
                            gameExit = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                gameExit = True
                                gameOver = False
                            if event.key == pygame.K_c:
                                gameLoop()
    
            for event in pygame.event.get():
                if event.type  == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and move_to_h == 0:
                        direction = "left"
                        move_to_h = -block
                        move_to_v = 0
                    elif event.key == pygame.K_RIGHT and move_to_h == 0:
                        direction = "right"
                        move_to_h = block
                        move_to_v = 0
                    elif event.key == pygame.K_UP and move_to_v == 0:
                        direction = "up"
                        move_to_v = -block
                        move_to_h = 0
                    elif event.key == pygame.K_DOWN and move_to_v == 0:
                        direction = "down"
                        move_to_v = block
                        move_to_h = 0
                        
            if start_x >= display_width or start_x < 0 or start_y >= display_height or start_y < 0:
                gameOver = True
    
            start_x += move_to_h
            start_y += move_to_v
    
            gameDisplay.fill(white)
            gameDisplay.blit(appleimg, (randomFruitX, randomFruitY))
    
            snakeHead = []
            snakeHead.append(start_x)
            snakeHead.append(start_y)
            snakeList.append(snakeHead)
    
            if len(snakeList) > snakeLength:
                del snakeList[0]
    
            score(snakeLength - 1)
    
            snake(block, snakeList)
            pygame.display.update()
    
            # to see if snake has eaten himself or not
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    isDead = True
                    snake(block, snakeList)
                    pygame.time.delay(1000)
                    gameOver = True
    
            if start_x > randomFruitX and start_x < randomFruitX + appleSize or start_x + block > randomFruitX and start_x + block < randomFruitX + appleSize:
                if start_y > randomFruitY and start_y < randomFruitY + appleSize:
                    randomFruitX, randomFruitY = randomAppleGen()
                    snakeLength += 1 
                    menu_song = pygame.mixer.music.load(path.join(sound_folder, "wakka.ogg"))
                    pygame.mixer.music.play(0)
                if start_y + block > randomFruitY and start_y + block < randomFruitY + appleSize:
                    randomFruitX, randomFruitY = randomAppleGen()
                    snakeLength += 1 
                    menu_song = pygame.mixer.music.load(path.join(sound_folder, "wakka.ogg"))
                    pygame.mixer.music.play(0)
    
            # initialising no. of frames per sec
            clock.tick(15)
    
    
        pygame.quit()
        # you can signoff now, everything looks good!
        quit()

# # this fuction kicks-off everything 
def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = snakeClass()
    game.run(self)

if __name__ == '__main__':
    main()

