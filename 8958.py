a = int(input())
cnt = 0
res = 0

for i in range(a):
    lst = input()
    for j in range(len(lst)):
        if lst[j]=='O':
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)
    cnt = 0
    res = 0