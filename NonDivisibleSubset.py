#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    print(k)
    print(s)
    import itertools
    maxlen = 0
    for i in range(len(s)-1, 1, -1):
        for perm in itertools.permutations(s,i):
            for p in itertools.permutations(perm, 2):
                if (p[0] + p[1]) % k == 0:
                    continue
                else:
                    if len(perm) > maxlen:
                        maxlen = len(perm)
    return maxlen

if __name__ == '__main__':
    maxlen = nonDivisibleSubset(3, [1, 7, 2, 4])
    print(maxlen)