import sys

num=int(sys.stdin.readline())
arr=list()
for _ in range(num):
    arr.append(int(sys.stdin.readline()))

for thg in sorted(arr):
    print(thg)