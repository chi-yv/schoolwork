import random
li=[]
n=10
for i in range(1,n+1):  # 随机生成k只股票
    # 股票名、编号、当前价格、三个月前价格
    li.append([1000+i,i,int(random.uniform(100,200)),int(random.uniform(120,200))])
print(li)
for i in range(n):  # 计算股票涨跌值、涨跌幅
    k=100   # 股票涨跌幅精度
    li[i].append(li[i][2]-li[i][3]) # 增加股票涨跌值
    li[i].append(int(k*(li[i][2]-li[i][3])/li[i][3])/k) # 增加股票涨跌幅
m=5 # 冒泡排序，4代表依据股票涨跌值，5代表依据股票涨跌幅
for i in range(n-1):
    for j in range(n-i-1):
        if(li[j][m]>li[j+1][m]):
            t=li[j]
            li[j]=li[j+1]
            li[j+1]=t
for i in li:
    print(i)
