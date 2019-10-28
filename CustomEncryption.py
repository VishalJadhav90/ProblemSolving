#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    strlen = 0
    newarr = []
    for char in s:
        if char:
            newarr.append(char)
            strlen = strlen + 1
    sqrt = pow(strlen, 1 / 2)
    row = math.floor(sqrt)
    print(row)
    col = math.ceil(sqrt)
    print(col)
    encrypted_list = []
    for i in range(col):
        j = i
        newword = ""
        while (j < strlen):
            newword += newarr[j]
            j = j + col
        encrypted_list.append(newword)
    print(encrypted_list)
    result = " ".join(encrypted_list)
    return result


if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)