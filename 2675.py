case = int(input())
for i in range(case):
    co, st = input().split()
    co = int(co)
    for j in range(len(st)):
        print(st[j]*co, end="")
    print()