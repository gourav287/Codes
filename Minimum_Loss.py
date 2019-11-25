"""
Question link:
https://www.hackerrank.com/challenges/minimum-loss/problem
"""

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(prices):
    price=sorted(prices)
    cost=max(price)
    for i in range(len(price)-1):
        if(cost>price[i+1]-price[i] and prices.index(price[i+1])<prices.index(price[i])):
            cost=price[i+1]-price[i]
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
