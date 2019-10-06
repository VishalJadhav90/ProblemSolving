def toss_win_number(n):
    a = bin(n)
    print(a)
    bits = len(str(a)[str(a).find("0b") + 1:])
    previous_zero = -1
    count, frwd_count = 0, 0
    found_zero = False
    win = -1
    for p in range(0, bits):
        count = count + 1
        if ((1<<p) & n) == 0: #zero position
            if previous_zero != -1:
                if (count - 1) > win:
                    win = count - 1
                count = frwd_count
                frwd_count = 0
            previous_zero = p
            found_zero = True
            n = (1<<p) | n
        if found_zero:
            frwd_count += 1
    print(win)

toss_win_number(1775)