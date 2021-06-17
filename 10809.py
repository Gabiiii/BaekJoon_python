alph = [-1]*26
st=input()

for i in range(len(st)):
    for j in range(26):
        if ord(st[i])==j+97 and alph[j]==-1:
            alph[j]=i
for each in alph:
    print(each, end=" ")