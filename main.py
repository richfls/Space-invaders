import pygame
from math import *
import time
import random
pygame.init()  
pygame.display.set_caption("space invaders")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False
px = 450
py = 750
timer = 0
LEFT= False
RIGHT= False
UP = False
shoot = False
lives = 3
direction = [LEFT,RIGHT,UP]


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
    def collide(self, bulletx, bullety):
        if self.isAlive:
            if (bulletx > self.xpos and 
                    bulletx < self.xpos + 40 and 
                        bullety > self.ypos and 
                            bullety < self.ypos + 40):
                print("hit!")
                self.isAlive = False
                return False
        return True

    def draw(self):
        if self.isAlive == True:
            pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos,40,40))


class bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False

    def move(self, xpos, ypos):
        if self.isAlive == True:
            self.ypos -= 5
        if self.ypos < 0: 
            self.isAlive = False
            self.xpos = xpos
            self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))

class wall:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.numhit = 0
        self.wallcolor = [250,250,20]

    def collide(self, bulletx, bullety):
        if self.numhit < 3:
            if (bulletx > self.xpos and 
                    bulletx < self.xpos + 30 and 
                        bullety > self.ypos and 
                            bullety < self.ypos + 30):
                print("hit!")
                self.numhit += 1
                self.wallcolor[0] -= 100
                self.wallcolor[1] -= 100
                self.wallcolor[2] -= 10
                return False
        return True


    def draw(self):
        if self.numhit < 3:
            pygame.draw.rect(screen,(self.wallcolor[0],self.wallcolor[1],self.wallcolor[2]),(self.xpos,self.ypos, 30,30))

class missile:
    def __init__(self):
        self.xpos = -10
        self.ypos = -10
        self.isAlive = False

    def move(self):
        if self.isAlive == True:
            self.ypos += 5
        if self.ypos > 800: 
            self.isAlive = False
            self.xpos = -10
            self.ypos = -10
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))
bullet = bullet(px+28, py)
missilelist = []
for missiles in range(10):
    missilelist.append(missile())
enemy = []
walls = []
for i in range(4):
    for j in range(12):
        enemy.append(alien(j*60+50,i*60+50))
for i in range(4):
    for j in range(2):
        for l in range(3):
            walls.append(wall(l*30+200*i+150,j*30+600))


while gameover != True:
    #physics_______________________________
    clock.tick(60)
    randnum = random.randrange(100)
    timer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction[0] = True
            if event.key == pygame.K_RIGHT:
                direction[1] = True
            if event.key == pygame.K_UP:
                shoot = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction[0] = False
            if event.key == pygame.K_RIGHT:
                direction[1] = False
            if event.key == pygame.K_UP:
                shoot = False

    if direction[0] == True:
        vx = -3 
    elif direction[1] == True:
        vx = 3 

    else:
        vx = 0

    px += vx

    for i in range(len(enemy)):
        timer = enemy[i].move(timer)

    for missiles in range(len(missilelist)):
        missilelist[missiles].move()

    if shoot == True:
        bullet.isAlive = True

    if bullet.isAlive == True:
        bullet.move(px+28, py)

        if bullet.isAlive == True:
            for i in range(len(enemy)):
                bullet.isAlive = enemy[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isAlive == False:
                    break

        if bullet.isAlive == True:
            for i in range(len(walls)):
                bullet.isAlive = walls[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isAlive == False:
                    break

    else:
        bullet.xpos = px + 28
        bullet.ypos = py
    if randnum < 2:
        aliennum = random.randrange(len(enemy))
        if enemy[aliennum].isAlive == True:
            for missiles in range(len(missilelist)):
                if missilelist[missiles].isAlive == False:
                    missilelist[missiles].isAlive = True
                    missilelist[missiles].xpos = enemy[randnum].xpos+5
                    missilelist[missiles].ypos = enemy[randnum].ypos
                    break
    for wallnum in range(len(walls)):
        for missiles in range(len(missilelist)):
            if missilelist[missiles].isAlive == True:
                if walls[wallnum].collide(missilelist[missiles].xpos, missilelist[missiles].ypos) == False:
                    missilelist[missiles].isAlive = False
                    break

    for missiles in range(len(missilelist)):
        if missilelist[missiles].isAlive == True:
            if px < missilelist[missiles].xpos:
                if py < missilelist[missiles].ypos:
                    if px + 40 > missilelist[missiles].xpos:
                        if py + 40 > missilelist[missiles].ypos:
                            print("player hit")
                            lives -= 1
                            missilelist[missiles].isAlive = False
                            time.sleep(2)
                            px = 450
                            
                            

    #render________________________
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(200,200,100),(px,py, 60, 20))

    for i in range(lives):
        pygame.draw.rect(screen,(255,0,0),(50*i+40,0,30,30))
    for i in range(len(enemy)):
        enemy[i].draw()
    for i in range(len(walls)):
        walls[i].draw()
    for i in range(len(missilelist)):
        missilelist[i].draw()
    bullet.draw()
    
    pygame.display.flip()

pygame.quit()
