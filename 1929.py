import sys
import math

def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

min,max=map(int,sys.stdin.readline().split())
for i in range(min,max+1):
    if prime(i):
        print(i)