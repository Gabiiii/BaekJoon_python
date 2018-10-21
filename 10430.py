# 10430 ³ª¸ÓÁö
# ver.1
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print((a%c*b%c)%c)
# ver.2
a,b,c=map(int,input().split())
print("%d\n%d\n%d\n%d"%(((a+b)%c), ((a%c+b%c)%c), ((a*b)%c), ((a%c*b%c)%c)))