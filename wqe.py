from turtle import *
tracer(0)
screensize(10000,10000)
r = 10
pd()
for i in range(11):
    fd(111*r)
    rt(120)
pu()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*r,y*r)
        dot(3,'red')
exitonclick()