import sys

code=[]
for i in range(8):
    code.append(i+1)
arr=list(map(int, (sys.stdin.readline().split())))

if arr==code:
    print("ascending")
elif arr==list(reversed(code)):
    print("descending")
else:
    print("mixed")