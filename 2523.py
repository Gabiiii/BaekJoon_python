a = int(input())

for i in range(a*2-1):
    if i<a:
        print("*"*(i+1))
    else:
        print("*"*((a*2)-(i+1)))