def printGivenSumSubsets(arr, givensum):
    sums_dict = {}
    sums_dict[0] = [-1]
    sum = 0
    for i, ele in enumerate(arr):
        sum += ele
        if (sum-givensum) in sums_dict:
            positions = sums_dict[sum-givensum]
            print(positions[-1]+1, i)
        positions = sums_dict.get(sum, [])
        positions.append(i)
        sums_dict[sum] = positions
        print(sums_dict)

printGivenSumSubsets([1,1,8,-7,5,4,-9], 0)