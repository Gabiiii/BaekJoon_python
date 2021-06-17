lst = list()
cnt = 0

for i in range(10):
    tmp = 0
    a = int(input())
    x = a % 42
    for j in lst:
        if j==x:
            tmp += 1
    if tmp == 0:
        cnt += 1
        lst.append(x)
        
print(cnt)