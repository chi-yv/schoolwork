import turtle as t
def setting():  # 基础设置
    t.screensize(200, 200)
    t.pensize(25)
    t.pencolor("purple")
    t.speed(0)
def draw_python(x,y):   # 绘画蟒蛇主体，(x,y)是蟒蛇坐标
    t.penup()
    t.goto(-250+x, 0+y)
    t.pendown()
    t.seth(-40)
    for i in range(3):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 80 / 2)
    t.fd(10)
def put(p): # 判断输入（adsw）,并给出对应坐标调整值
    (x,y)=(0,0)
    if (p == 'a'):
        x = -30
    if (p == 'd'):
        x = 30
    if (p == 's'):
        y = -30
    if (p == 'w'):
        y = 30
    return (x,y)
def main(): # 主函数
    setting()
    draw_python(0,0)
    p='p'
    (x, y)=(0, 0)
    while(p!='q'):  # q是退出键
        p = input() # 接收输入
        (a,b)=put(p)    # 得出改变值
        x+=a
        y+=b
        t.clear()   # 清屏
        draw_python(x,y)    # 重新绘画
    t.done()    # 结束
main()  #运行主程序
