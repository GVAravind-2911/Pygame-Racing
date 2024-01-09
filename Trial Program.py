import pygame
from pygame.locals import *

pygame.init()

displaywidth=852
displayheight=480

maindisplay=pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption("Game Dev")
clock=pygame.time.Clock()

bgimg=pygame.image.load("road.jpg")
bgimg=pygame.transform.scale(bgimg,(852,480))
carImg=pygame.image.load("mercedes1.png")

#def car(x,y):
    #maindisplay.blit(carImg,(x,y))

x=0
y=100

ychange=0

crashed=False
while not crashed:
    for event in pygame.event.get():
        if event.type==QUIT:
            crashed=True
        if event.type==KEYDOWN:
            if event.type==K_LEFT:
                ychange=10
            elif event.type==K_RIGHT:
                ychange=-10

        if event.type==KEYUP:
            if event.type==K_LEFT:
                ychange=0
            elif event.type==K_RIGHT:
                ychange=0
    y+=ychange
                

# maindisplay.fill("white")
    maindisplay.blit(bgimg,(0,0))
    maindisplay.blit(carImg,(x,y))
    pygame.display.flip()

    clock.tick(60)
pygame.quit()