"""
Question link:
https://www.codechef.com/SEPT19B/problems/FIBEASY
"""

t=int(input())
for i in range(t):
    n=int(input())
    count=0
    if n!=1 and n!=2 and n!=3:
        s=[0,9,2,3]
        while n>0:
            n=n//2
            count+=1
        count=(count-1)%4
        print(s[count])
    else:
        if n==2 or n==3:
            print("1")
        else:
            print("0")
