"""
Question link:
https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
"""

from collections import deque
def matrix_rotation(arr, n, m, r):
    result = []
    for _ in range(n):
        result.append(list(0 for _ in range(m)))
    layers = n//2
    l1 = 0
    r1, c1 = 0, 0

    while layers > 0:
        layers -= 1
        test = {}
        if c1 <m and r1 < n:
            # Down
            for i in range(l1, n-1):
                test[(r1,c1)] = arr[r1][c1]
                r1 += 1
            # Right
            for j in range(l1, m-1):
       
                test[(r1,c1)] = arr[r1][c1]
               
                c1 += 1
            # Up
            for i in range(l1, n-1):
              
                test[(r1,c1)] = arr[r1][c1]
               
                r1 -= 1
            # left
            for j in range(l1, m-1):
               
                test[(r1,c1)] = arr[r1][c1]
               
                c1 -= 1
           
            de = deque(test.values())
           
            de.rotate(r)
            temp = list(de)
           
            q = 0
            for p,s in test.keys():
                result[p][s] = temp[q]              
                q += 1

            l1 += 1
            r1 = l1
            c1 = l1
            
            n -= 1
            m -= 1
            
    for i in result:
        print(' '.join(str(j) for j in list(i)))

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    #print(n, m, r)
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    matrix_rotation(arr, n, m, r)
