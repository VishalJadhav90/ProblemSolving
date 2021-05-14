def largestSubarray(a):
    numberMap = {}
    seqBeg = 0
    for i, ele in enumerate(a):
        if ele in numberMap:
            pos = numberMap[ele]
            seqLen = i - seqBeg
            print("{}-->{} {}".format(seqBeg, i-1, seqLen))
            seqBeg = pos + 1
        numberMap[ele] = i


'''
     0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
'''
a = [2,0,1,2,0,4,5,2,6,4,0, 8, 5, 3, 2, 9, 4, 7, 2, 9, 7]
a = [2, 0, 2, 1, 4, 3, 1, 0]
'''                                                 b
2, 18
0, 10
1, 2
4, 16
5, 12
6, 8
8, 11
3, 13
9, 15
7, 17
'''
largestSubarray(a)