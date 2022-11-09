#THE MAIN! uwu
import pygame, sys
from pygame.locals import *
#main loop
def main():
    #setting vars
    PERH = (500)
    PERW = (500)
    BLUE = (184, 232, 255)
    BGCOLOR = (255, 195, 191)
    PLAYERY = (250)
    PLAYERX = (250)
    #setting the main stuff up
    pygame.display.init()
    DISPLAY=pygame.display.set_mode((PERH,PERW))
    DISPLAY.fill(BGCOLOR)
    #while the game is running...
    while True:
        #drawing character
        pygame.draw.rect(DISPLAY,BLUE,(PLAYERX,PLAYERY,10,10))
        pygame.image.load("Eio-asset.png")
        #define more stuff
        KEY = pygame.key.get_pressed()
        #Check Key Pressed
        if KEY[K_UP]:
            PLAYERY = PLAYERY - 1
        if KEY[K_LEFT]:
            PLAYERX = PLAYERX - 1
        if KEY[K_DOWN]:
            PLAYERY = PLAYERY + 1
        if KEY[K_RIGHT]:
            PLAYERX = PLAYERX + 1
        #main for
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        pygame.time.delay(2)
main()