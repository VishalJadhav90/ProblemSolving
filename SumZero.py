def checkSumZero(A):
    beg = 0
    end = len(A)-1

    while beg < end:
        if (A[beg] + A[end]) == 0:
            return beg, end
        elif (A[beg] + A[end]) > 0:
            end -= 1
        else:
            beg += 1

    if (A[beg] + A[end]) == 0:
        return beg, end

    return -1, -1


print(checkSumZero([-8, -6, -5, 1, 5, 7, 12]))
