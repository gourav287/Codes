"""
question link:
https://www.codechef.com/OCT19B/problems/SAKTAN
"""

t=int(input())
for test in range(t):
	n,m,q=map(int,input().split())
	row=[0]*n
	col=[0]*m
	for i in range(q):
		a,b=map(int,input().split())
		row[a-1]+=1
		col[b-1]+=1
	oddr,oddc=0,0
	for i in range(n):
		if row[i]%2!=0:
			oddr+=1
	for i in range(m):
		if col[i]%2!=0:
			oddc+=1
	res=oddr*(m-oddc)+oddc*(n-oddr)
	print(res)
