ax,ay,az=map(int, input().split())
cx,cy,cz=map(int, input().split())

print("%d %d %d" %(cx-az,cy//ay,cz-ax))