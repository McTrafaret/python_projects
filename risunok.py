from turtle import *
from time import sleep



up()
setx(-1000)
down()
forward(2000)
up()
setx(0)
sety(1000)
right(90)
down()
forward(2000)



x = -10
up()
setx(x)
sety(x**2)
down()

for x  in range(x, abs(x)):
    goto(x, x**2)

up()
bgpic('shufa.gif')
home()

sleep(5)
