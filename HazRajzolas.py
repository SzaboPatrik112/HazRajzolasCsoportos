import turtle as t
t.speed(3)
t.width(3)
t.color("blue")

#hazalja
i=0
t.left(180)
while i<4:
    t.forward(100)
    t.right(90)
    i+=1
t.left(270)
t.forward(100)

#haz teteje
t.setheading(55)
t.forward(60)
t.setheading(-55)
t.forward(60)



t.done()