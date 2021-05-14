def findSeqBeg(a):
    zero = -1
    prevZero = -1
    prevSum = -1
    sum1 = -1
    lastzero = -1
    for i in range(len(a)-1):
        if not a[i]:
            if a[i+1] > 0:
                lastzero = i
                prevZero = zero if zero != -1 else -1
                zero = i
                print(prevZero, zero)
            if a[i-1] == 1:
                if prevZero != -1:
                    print("----------", prevZero, zero, prevSum, sum1)
                    if sum1 != -1:
                        prevSum = sum1
                    sum1 = zero - prevZero - 1
                    print("-s--------", prevSum, sum1)
                    if sum1 != -1 and prevSum != -1:
                        print("$$$$$$$ {}".format(sum1+prevSum+1))

    if a[-1] == 1 and lastzero == zero:
        print("---------->", prevSum+len(a)-prevZero)


a = [1,0,1,1,1,1,0,1,1,0,1,0,1]
a = [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
a = [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1]
a = [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
findSeqBeg(a)