def min_number(n):
    a = bin(n)
    print(a)
    bits = len(str(a)[str(a).find("0b")+1:])
    print(bits)
    prev_zero = 0

    for i in range(0, bits):
        if 1<<i & n == 0:
            if not prev_zero:
                prev_zero = i
        if 1<<i & n != 0:
            if prev_zero:
                print("before:", prev_zero)
                n = n | (1<<prev_zero)
                n = n & (~(1<<i))
                prev_zero = i
                print("after:", prev_zero)
                print(bin(n))
    return n

def max_number(n):
    a = bin(n)
    print(a)
    bits = len(str(a)[str(a).find("0b") + 1:])
    print(bits)
    prev_zero = 0

    for i in range(bits-1, -1, -1):
        if 1 << i & n == 0:
            if not prev_zero:
                prev_zero = i
        if 1 << i & n != 0:
            if prev_zero:
                print("before:", prev_zero)
                n = n | (1 << prev_zero)
                n = n & (~(1 << i))
                prev_zero = i
                print("after:", prev_zero)
                print(bin(n))
    return n

n = min_number(69)
print(bin(n))
n = max_number(69)
print(bin(n))