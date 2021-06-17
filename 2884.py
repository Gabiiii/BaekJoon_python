hour, min = map(int, input().split())

if(min >= 45):
        min -= 45;
else:
        if(hour == 0):
                hour = 23
        else:
                hour -= 1
        min += 15

print(hour, min)