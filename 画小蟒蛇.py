import turtle

'''
rad描述圆形轨迹半径的位置
angle弧度值
'''
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)                    #向前直线爬行
    turtle.circle(neckrad, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)     #窗口宽度，高度，坐标（左上角为原点）
    pythonsize = 30
    turtle.pensize(pythonsize)        #运行轨迹的宽度
    turtle.pencolor("blue")
    turtle.seth(-40)                  #运行方向，0向东，90向北，180向西，270向南
    drawSnake(40, 80, 5, pythonsize/2)

main()
