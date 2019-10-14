def swap_odd_even(n):
    a = bin(n)
    print(a)
    bits = len(str(a)[str(a).find("0b") + 1:])
    print(bits)

    for i in range(0, bits):
        if i%2 == 1:
            if n & (1 << i) != 0:
                now = 1
            else:
                now = 0
            if previous == 0:
                n = n & ~(1<<i)
            if previous == 1:
                n = n | (1<<i)
            if now == 0:
                n = n & ~(1 << (i-1))
            if now == 1:
                n = n | (1 << i-1)
        else:
            previous = n & (1 << i)
    return n

print(bin(swap_odd_even(10)))