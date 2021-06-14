a,b=map(int, input().split())

if a>b:
    x=(a+b)//2
    y=(a-b)//2
else:
    x=(b+a)//2
    y=(b-a)//2

if x+y==a and x-y==b:
    print("%d %d" %(x,y))
else:
    print("-1")