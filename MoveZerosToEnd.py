def moveAllZeros(a):
    zero = 0
    for i in range(len(a)):
        #print("before", i, a[i], a, zero)
        if a[i]:
            if zero < i:
                a[zero], a[i] = a[i], a[zero]
                zero = zero + 1
            else:
                zero = zero + 1
        #print("after", i, a[i], a, zero)

'''
     0  1  2  3  4  5  6  7  8
'''
a = [6, 0, 8, 2, 3, 0, 4, 0, 1]

moveAllZeros(a)
#print(a)


b = [6, 0, 1, 0, 3, 1, 4, 0, 1, 5]

def moveAllOnes(b):
    one = len(b)-1
    for i in range(len(b)-1, -1, -1):
        if b[i] != 1:
            if one > i:
                b[i], b[one] = b[one], b[i]
            one = one-1

moveAllOnes(b)
print(b)
