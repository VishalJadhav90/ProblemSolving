def count_toggle_bits(n, m):
    n_m = n ^ m
    count = 1
    while True:
        n_m = n_m & (n_m - 1)
        if not n_m:
            break
        count = count + 1
    return count

print(count_toggle_bits(13, 8)) #10001 00111