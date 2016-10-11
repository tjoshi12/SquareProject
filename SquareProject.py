from Myro import *
init("sim") #if your simulator is not running


def makesquare():
    penDown()
    forward(2,2)
    penUp()
    turnBy(90)
    penDown()
    forward(2,2)
    penUp()
    turnBy(90)
    penDown()
    forward(2,2)
    penUp()
    turnBy(90)
    penDown()
    forward(2,2)
    penUp()
    forward(2,2)

## #making a triangle
def maketriangle():
    penDown()
    forward(2,2)
    penUp()
    turnBy(120)
    penDown()
    forward(2,2)
    penUp()
    turnBy(120)
    penDown()
    forward(2,2)
    penUp()
    forward(2,2)
 
## #making a pentagon
def makepentagon():
    penDown()
    forward(1.5,1.5)
    penUp()
    turnBy(72)
    penDown()
    forward(1.5,1.5)
    penUp()
    turnBy(72)
    penDown()
    forward(1.5,1.5)
    penUp()
    turnBy(72)
    penDown()
    forward(1.5,1.5)
    penUp()
    turnBy(72)
    penDown()
    forward(1.5,1.5)
    penUp()
    forward(2,2)
    
def makeletter():
    penDown()
    forward(1.5,1.5)
    penUp()
    turnBy(180)
    penDown()
    forward(1.5,3)
    penUp()
    turnBy(180)
    penDown()
    forward(1.5,1.5)
    penUp()
    turnBy(270)
    penDown()
    forward(2,2)
    penUp()
    turnBy(90)
    forward(1,1)
    
# Creating a letter was different than a shape
# because while shapes have the same angles
# and are uniform, letter are not symetterical
# and uniform. Therefore, you have to think quite
# a bit more to create a letter than a shape.    

