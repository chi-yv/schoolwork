import turtle as t
def setting():  # 基础设置
    t.screensize(200, 200)
    t.pensize(15)
    t.pencolor("purple")
    t.speed(0)
def draw_python():   # 绘画蟒蛇主体
    t.penup()
    t.goto(-250, 0)
    t.pendown()
    t.seth(-40)
    for i in range(3):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 80 / 2)
    t.fd(10)
def put(p): # 判断输入（adsw）,并给出对应行动
    if (p == 'w'):# 前进
        t.fd(30)
    if (p == 's'):# 后退（不动）
        t.fd(-30)
    if (p == 'a'):# 左转
        t.circle(60,30)
    if (p == 'd'):# 右转
        t.circle(-60,30)
def main(): # 主函数
    setting()
    draw_python()
    p='p'
    while(p!='q'):  # q是退出键
        p = input() # 接收输入
        put(p)    # 行动
    t.done()    # 结束
main()  #运行主程序
