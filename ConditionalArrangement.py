def conditionalArrangment(a):
    for i in range(1, len(a), 2):
        if a[i-1] > a[i]:
            a[i], a[i-1] = a[i-1], a[i]
        if a[i+1] > a[i]:
            a[i], a[i + 1] = a[i + 1], a[i]

a = [6,4,5,7,9,1,8]
conditionalArrangment(a)
print(a)