# 10817 �� ��
inp = list(input().split())
for i in range(len(inp)):
        inp[i]=int(inp[i])
inp.sort(reverse=True)
print(inp[1])