import turtle as trtl
r = 10
trtl.screensize(10000)
trtl.tracer(0)
for i in range(9):
    trtl.forward(22*r)
    trtl.right(90)
    trtl.forward(6*r)
    trtl.right(90)
trtl.up()
trtl.forward(1*r)
trtl.right(90)
trtl.forward(5*r)
trtl.left(90)
trtl.down()
for i in range(9):
    trtl.forward(53*r)
    trtl.right(90)
    trtl.forward(75*r)
    trtl.right(90)
trtl.up()
for x in range(-50,50):
    for y in range(-50,50):
        trtl.goto(x*r,y*r)
        trtl.dot(3,'red')
trtl.update()
x = input()