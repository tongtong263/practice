'''
#五角星
from turtle import Turtle

p=Turtle()
p.speed(3)
p.pensize(5)
p.color("black", "yellow")
#p.fillcolor("red")
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()
'''

#Tree
from turtle import Turtle

def tree(plist,l,a,f):
    '''plist is the list of pens
    l is the length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level'''
    if l>5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)
def main():
    p = Turtle()
    p.color("green")
    p.pensize(5)
    p.hideturtle()
    '''make this turtle invisible, it's good idea to do this  while
    you are in the middle of doing some complex drawing, because 
    hiding the turtle speeds up the drawing observably
    '''
    p.getscreen().tracer(30,0)
    '''return the TurtleScreen object the turtle is drawing on.
    TurtleScreen methods can then be called for that object
    '''
    p.left(90)
    p.penup()
    p.goto(0,0)
    p.pendown()
    t = tree([p],110,65,0.6375)

main()
