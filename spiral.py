from turtle import *

speed('fast')
width(10)
color('blue','red')
begin_fill()

for d in range(200):
  forward(d)
  right(30)

end_fill()
exitonclick()
