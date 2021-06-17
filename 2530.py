ho,mi,se=map(int, input().split())
ti=int(input())

se=se+ti
mi=mi+(se//60)
ho=ho+(mi//60)

print("%d %d %d" %((ho%24),(mi%60),(se%60)))