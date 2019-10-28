#!/bin/python3

import math
import os
import random
import re
import sys

'''
2
3
1 3 1
2 1 2
3 3 3
3
[0, 2, 1], [1, 1, 1], [2, 0, 0]

Your Output (stdout)
Impossible
Impossible

Expected Output
Impossible
Possible
'''

def __get_pos(cntno, containers):
    pos = []
    for i in range(len(containers)):
        if containers[cntno][i] != 0:
            pos.append(i)
    #print("__get_pos: ", pos)
    return pos

def __reduce_from_increase_in(cntno, red, pos, containers):
    #print("__reduce_from_increase_in", red, pos)
    for i in range(len(containers)):
        if i == cntno:
            continue
        if containers[i][pos] and containers[i][pos] <= containers[cntno][red]:
            containers[cntno][pos] += containers[i][pos]
            containers[i][red] += containers[i][pos]
            containers[cntno][red] -= containers[i][pos]
            containers[i][pos] = 0
        #print("containers: ", containers)

def __incorrect_results(cntno, pos, containers):
    #print("__incorrect_results:", containers, cntno)
    for j in range(len(containers)):
        if containers[cntno][j] != 0 and j != pos:
            #print("__incorrect_results: ", True)
            return True
        if containers[j][pos] != 0 and j != cntno:
            #print("__incorrect_results: ", True)
            return True
    #print("__incorrect_results: ", False)
    return False

def __get_rid_of_others(cntno, pos, containers):
    correct = True
    orig_containers = containers[:]
    for j in range(len(containers)):
        if j == pos or containers[cntno][j] == 0: continue
        correct = True
        __reduce_from_increase_in(cntno, j, pos, containers)
        if __incorrect_results(cntno, pos, containers):
            containers = orig_containers[:]
            correct = False
        else:
            return True
    return correct

def __organize(cntno, baltyp, containers):
    if not containers[cntno][baltyp]:
        return True
    correct = True
    for pos in __get_pos(cntno, containers):
        correct = True
        orig_containers = containers[:]
        if not __get_rid_of_others(cntno, pos, containers):
            correct = False
            containers = orig_containers[:]
    return correct

# Complete the organizingContainers function below.
def organizingContainers(containers):
    correct = True
    #print(containers)
    for cntno in range(len(containers)):
        for baltyp in range(len(containers)):
            correct = True
            orig_containers = containers
            if not __organize(cntno, baltyp, containers):
                correct = False
                containers = orig_containers
    return correct

if __name__ == '__main__':
    result = organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]])
    #result = organizingContainers([[0, 2, 1], [1, 1, 1], [2, 0, 0]])
    print(result)