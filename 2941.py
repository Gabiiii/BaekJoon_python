inp=input()
cnt=len(inp)

cnt=cnt-(inp.count('c='))
cnt=cnt-(inp.count('c-'))
cnt=cnt-(inp.count('dz='))
cnt=cnt-(inp.count('d-'))
cnt=cnt-(inp.count('lj'))
cnt=cnt-(inp.count('nj'))
cnt=cnt-(inp.count('s='))
cnt=cnt-(inp.count('z='))

print(cnt)