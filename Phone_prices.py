"""
question link:
https://www.codechef.com/OCT19B/problems/S10E
"""

t=int(input())
for test in range(t):
	count=1
	n=int(input())
	Pr=list(map(int,input().split()))
	for i in range(1,len(Pr)):
		if i<5:
			if Pr[i]<min(Pr[0:i]):
				count+=1
		else:
			if Pr[i]<min(Pr[i-5:i]):
				count+=1
	print(count)
