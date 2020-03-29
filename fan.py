from turtle import *

start = pos()
steps = 30
size = 200
fd(size)
for x in range(steps):
  color((0,0,x/steps))
  begin_fill()
  goto(start)
  right(360/steps)
  fd(size-x)
  end_fill()

exitonclick()
