import pygame as py
py.init()
py.display.set_caption("space invaders!")
screen = py.display.set_mode((800,800))
clock = py.time.Clock()
gameover = False



xpos = 400
ypos = 750
keys = [False, False, False]
LEFT=0
RIGHT=1
UP = 2

while not gameover:
    clock.tick(60)



    for event in py.event.get(): #quit game if x is pressed in top corner
        if event.type == py.QUIT:
            gameover = True
        if event.type == py.KEYDOWN: #keyboard input
            if event.key == py.K_LEFT:
                keys[LEFT]=True
            if event.key == py.K_RIGHT:
                keys[RIGHT]=True
            if event.key == py.K_UP:
                keys[UP]=True
    # Input KEYUP
        elif event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                keys[LEFT]=False
            if event.key == py.K_RIGHT:
                keys[RIGHT]=False
            if event.key == py.K_UP:
                keys[UP]=False
    #LEFT MOVEMENT
        if keys[LEFT] == True:
            vx= -3
    #RIGHT MOVEMENT
        elif keys[RIGHT]==True:
            vx= 3
        elif keys[UP]==True:
            shoot = True
        #turn off velocity
        else:
            vx = 0

        
            #update player position
        xpos+=vx 



    screen.fill((0,0,0))

    py.draw.rect(screen,(200,200,100),(xpos,ypos,60,20))

    py.display.flip()

py.quit()
