# 10817 ¼¼ ¼ö
inp = list(input().split())
for i in range(len(inp)):
        inp[i]=int(inp[i])
inp.sort(reverse=True)
print(inp[1])