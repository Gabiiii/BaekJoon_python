n,w,h,l=map(int, input().split())
res=(w//l)*(h//l)
if res>n:
    print(n)
else:
    print(res)