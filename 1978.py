a=int(input())
pri=0
b=list(map(int, input().split()))

for each in b:
    cnt=0
    for j in range(1, each+1):
        if each%j==0:
            cnt+=1
    if cnt==2:
        pri+=1

print(pri)