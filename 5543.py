bp = 3000
sp = 3000

for i in range(3):
    a = int(input())
    if a < bp:
        bp = a

for i in range(2):
    a = int(input())
    if a < sp:
        sp = a

print(bp+sp-50)