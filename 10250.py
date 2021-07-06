import sys

num=int(sys.stdin.readline())
for _ in range(num):
    h,w,n=map(int, (sys.stdin.readline().split()))
    
    if n%h!=0:
        y=n%h
        x=(n//h)+1
    else:
        y=h
        x=n//h
    
    if x<10:
        print("%d0%d" %(y,x))
    else:
        print("%d%d" %(y,x))