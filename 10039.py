i = 1
res = 0;
while i<=5:
    a = int(input())
    if a < 40:
        a = 40
    res += a
    i += 1
print(res//5)