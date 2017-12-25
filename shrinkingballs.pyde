#Rebecca Chinn
#additional a+b, balls shrink and disappear as you touch them with your mouse, haha I'm so entertained...
from ball import Ball

# list of global variables
balls = []
shrunk=0
def setup():
    ellipseMode(RADIUS)
    global c
    size(800,800)
    c = color(0)


def draw():
    global shrunk
    background(0)
    fill(255)
    for i in balls:
        i.render()
        i.move()
        i.update()

        textSize(32)
        text(len(balls), 10, 30)
        text(shrunk, 10, 60)
    


   

    if random(100) > 95:
        c=color(random(255),random(255),random(255))
        balls.append(Ball(random(800),random(800),c,10,random(-2,2),random(-4,2),.08,2))
        

    


