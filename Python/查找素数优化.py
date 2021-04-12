li=[2]

k=int(input('上限：'))

for i in range(3,k+1):

    n=0

    for j in li:

        if i%j==0:

            n+=1

    if n==0:

        li.append(i)

print(k,'之内的所有素数为',li)
