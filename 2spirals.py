from turtle import *

speed('fast')
width(2)

for a in range(-100, 100):
  r = (a + 100) / 200
  b = (100 - a) / 200
  pencolor(r,0,b)
  forward(20)
  right(a)

exitonclick()
