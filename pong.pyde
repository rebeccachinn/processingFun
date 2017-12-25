#Rebecca Chinn
#A+B, pong game, user can slide mouse back and forth to keep balls from falling
#note, every so often a ball falls through the paddle, not sure why

from ball import Ball

# list of global variables
balls = []
def setup():
    ellipseMode(RADIUS)
    global c
    size(800,800)
    c = color(0)


def draw():
    background(0)
    fill(255)
    rect(mouseX,700,100,10)
    for i in balls:
        i.render()
        i.move()
        i.update()
        if i.isStale():
            balls.remove(i)

                    
def mouseClicked():
    global balls
    c=color(random(255),random(255),random(255))
    balls.append(Ball(random(width/2,width),random(0,height/2),c,random(40,50),2,random(-2,0),.05,0)) 

