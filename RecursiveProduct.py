def product(array, i, leftproduct):
    if len(array) == i:
        return 1
    ele = array[i]
    rightproduct = product(array, i+1, leftproduct*array[i])
    array[i] = leftproduct * rightproduct
    return ele*rightproduct


a = [1, 2, 3, 4, 5]
product(a, 0, 1)
print(a)
