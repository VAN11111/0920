import turtle
import math

#Define the function of radians to angle
def trans(rad):
    angle=180*rad/math.pi
    return angle

#四个小星与大星的中心连线 与 水平方向 的夹角
a=trans(math.atan(3/5))
b=trans(math.atan(1/7))
c=trans(math.atan(2/7))
d=trans(math.atan(4/5))

#画红色旗面  288*192px
turtle.pensize(1)
turtle.color("red","red")
turtle.begin_fill()
turtle.forward(288)
turtle.right(90)
turtle.forward(192)
turtle.right(90)
turtle.forward(288)
turtle.right(90)
turtle.forward(192)
turtle.end_fill()


#x，y分别表示星的中心点横纵坐标
#d表示星的中心点到顶点的距离
#l表示五角星的边长
#a1表示规范画笔使其从星中心到达星顶点的角度
#a2表示规范画笔使其开始画星的第一条线的角度

#大五角星的长为2*3*9.6*sin72=54.78(像素)
#小五角星的长为2*1*9.6*sin72=18.26(像素)


def star(x,y,d,l,a1,a2):
    turtle.penup()
    turtle.goto(x,y)#将画笔移动到星中心
    turtle.left(a1)
    turtle.forward(d)#将画笔移动到星顶点
    turtle.right(a2)#转变画笔方向准备绘画
    turtle.pendown()
    turtle.pensize(1)
    turtle.color("yellow","yellow")

    turtle.begin_fill()#一笔画五角星
    for _ in range(5):
        turtle.forward(l)
        turtle.right(144)
    turtle.end_fill()


#画大五角星
star(5*9.6,-5*9.6,3*9.6,54.78,72,162)

#画第一个小五角星
star(10*9.6,-2*9.6,9.6,18.26,144,162)
turtle.right(18)

#画第二个小五角星
star(12*9.6,-4*9.6,9.6,18.26,180-a+b,162)
turtle.right(18)

#画第三个小五角星
star(12*9.6,-7*9.6,9.6,18.26,180-b-c,180-c)
turtle.right(18)

#画第四个小五角星
star(10*9.6,-9*9.6,9.6,18.26,180+c-d,162)
turtle.right(18)
turtle.hideturtle()
