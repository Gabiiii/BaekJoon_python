dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
inp = input()
res = 0

for i in range(len(inp)):
    for each in dial:
        if inp[i] in each:
            res += dial.index(each)+3

print(res)