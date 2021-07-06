pac=int(input())
res=1
if pac==0:
    print("1")
else:
    for i in range(1,pac+1):
        res=res*i
    print(res)