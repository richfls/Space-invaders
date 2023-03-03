import pygame
from math import *
import time
pygame.init()  
pygame.display.set_caption("space invaders")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False
px = 400
py = 750
timer = 0
direction = [False,False,False]

class alien:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1

    def move(self,time):
        if time % 800 == 0:
            self.ypos += 100
            self.direction *= -1
            return 0
        if time % 100 == 0:
            self.xpos += 50*self.direction
        return time


    def draw(self):
        pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos,40,40))

enemy = []
for i in range(4):
    for j in range(12):
        enemy.append(alien(j*60+50,i*60+50))


while gameover != True:
    #physics_______________________________
    clock.tick(60)
    
    timer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction[0] = True
            if event.key == pygame.K_RIGHT:
                direction[1] = True
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                direction[0] = False
            if event.key == K_RIGHT:
                direction[1] = False

        if direction[0] == True:
            vx = -3 
        if direction[1] == True:
            vx = 3 
        else:
            vx = 0

        px += vx

    for i in range(len(enemy)):
        timer = enemy[i].move(timer)


    #render________________________
    screen.fill((0,0,0))
    for i in range(len(enemy)):
        enemy[i].draw()
    
    pygame.draw.rect(screen,(200,200,100),(px,py, 60, 20))

    pygame.display.flip()

pygame.quit()
