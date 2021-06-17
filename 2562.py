tmax = 0
index= 0
cnt = 0

for i in range(9):
    tmp=int(input())
    if tmp > tmax:
        tmax = tmp;
        cnt = i+1

print("%d\n%d" %(tmax,cnt))

