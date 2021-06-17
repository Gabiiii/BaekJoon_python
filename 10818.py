a = int(input())
inArr = list(map(int, input().split()))

inArr.sort()
print(inArr[0], inArr[a-1])