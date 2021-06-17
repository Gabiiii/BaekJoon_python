s=list(input().upper())
alph = [0]*26
smax=-1

for i in s:
    alph[ord(i)-65]+=1

if alph.count(max(alph)) >= 2:
    print("?")
else:
    print(chr(alph.index(max(alph))+65))