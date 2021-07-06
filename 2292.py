import sys

num=int(sys.stdin.readline())
cnt=1

while (num-(cnt*6))>1:
    num=num-(cnt*6)
    cnt=cnt+1

if num==1:
    print(cnt)
else:
    print(cnt+1)