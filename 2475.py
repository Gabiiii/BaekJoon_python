chk=0
inp=list(map(int, input().split()))

for i in range(5):    
    chk+=(inp[i]*inp[i])
chk=chk%10

print(chk)