import sys

num=int(sys.stdin.readline())
inp=[]

for _ in range(num):
    inp.append(int(sys.stdin.readline()))

for i in sorted(inp):
    print(i)