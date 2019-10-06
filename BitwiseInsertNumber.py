def insert_number(n, m, j, i):
    a = bin(n)
    bits = len(str(a)[str(a).find("0b")+1:])
    allonces = ~0
    part1 = allonces << (j+1)
    part2 = allonces >> (bits-i-1)
    part = part1 | part2
    n = n & part
    m = m << (i-1)
    n = n | m
    print(bin(n))
    return n

insert_number(128, 5, 4, 2)
