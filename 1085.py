x,y,w,h=map(int,input().split())
t=h-y
r=w-x
print(min(x,y,t,r))