ho,mi=map(int, input().split())
ti=int(input())

mi=mi+ti
ho=(ho+(mi//60))%24
mi=mi%60

print("%d %d" %(ho,mi))