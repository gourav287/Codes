"""
Question Link:
https://www.hackerrank.com/challenges/sparse-arrays/problem
"""

#Solution:

#!/bin/python3

import math
import os
import random
import re
import sys


#Here the only thing we needed to do was to send the count of each query.
#Hence we returned a list containing the same.
def matchingStrings(strings, queries):
    return [strings.count(i) for i in queries]

#The driver code
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
