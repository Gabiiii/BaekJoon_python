input=int(input())
res=(input*0.01)+25
if res<100:
    res=100
elif res>2000:
    res=2000
print(round(res,2))