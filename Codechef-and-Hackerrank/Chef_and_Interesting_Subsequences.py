"""
Question link:
https://www.codechef.com/SEPT19B/problems/CHEFINSQ
"""

from math import factorial as fct

def noofcomb (n,r):
    res = fct(n) // ( fct(r) * fct(n-r) )
    return res

t = int ( input() )

for _ in range (t):
    n,k = map ( int, input().split() )
    A = list ( map ( int, input().split() ) )
    A.sort()
    if n != k:
        v = A [k-1]
        left = A [:k]
        right = A [k:]
        h = left.count(v)
        su = A.count(v)
        count = noofcomb(su,h)
    else:
        count = 1
    print (int(count))
