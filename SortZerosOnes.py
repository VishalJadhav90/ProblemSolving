def sortZerosOnes(arr):
    zero = 0
    ones = 0
    for i in range(len(arr)):
        #print("i", i, "zero", zero, "ones", ones)
        if arr[i]:
            zero += 1
        else:
            arr[ones], arr[zero] = arr[zero], arr[ones]
            ones += 1
            zero += 1
        #print("arr", arr)
    print(arr)

def sortColors(arr):
    zero = 0
    ones = 0
    twos = 0
    for i in range(len(arr)):
        if arr[i] != 0: #0
            ones += 1
            twos += 1
        elif arr[i] != 1: #1
            zero += 1
            twos += 1
        else: #2
            zero += 1
            ones += 1
        if zero < ones < twos:
            continue
        else:
            if zero > ones:
                arr[ones], arr[ones] = arr[zero], arr[ones]
            if ones > twos:


arr = \
[1, 1, 0, 1, 0, 0, 2, 1, 0, 0, 2]

sortZerosOnes(arr)

