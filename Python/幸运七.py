from random import*
for j in range(4,10):   # 从赢钱数额4~9中依次尝试
    v = 0    # 赢钱次数统计变量
    for i in range(10000):  # 10000次赌局
        m = 10  # 初始金钱
        while m > 0:
            k = randint(1, 6) + randint(1, 6)   # 骰子总点数
            if (k == 7):
                m += j
            else:
                m -= 1
            if (m >= 20):   # 赢钱则退出
                v += 1
                break
    if(v/10000>0.5):    # 计算胜率
        print('用户赢钱额度为{}时，保证总体赢钱'.format(j))
        break
