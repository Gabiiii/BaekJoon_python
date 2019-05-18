# 4344 평균은 넘겠지_code.1
num = int(input())
avg = []
for i in range(num):
        sco = list(map(int,input().split()))
        stu = sco[0]
        del sco[0]
        sum = 0
        cnt = 0
        
        for j in sco:
                sum += j
        avg.append(sum/stu)

        for j in sco:
                if j > avg[i]:
                        cnt = cnt+1
        avg[i] = cnt/stu*100
        
for i in range(len(avg)):
        print("%.3f%%" %round(avg[i], 3))


# 4344 평균은 넘겠지_code.2
num = int(input())
for i in range(num):
	sco = list(map(int, input().split()))
	avg = sum(sco[1:]) / sco[0]
	cnt = 0
	for j in sco[1:]:
		if j > avg:
			cnt += 1
	print("%.3f%%" %round(cnt/sco[0]*100, 3))