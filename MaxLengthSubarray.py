def find_max_subarray(array, given_sum):
    max_range_e = -1
    max_range_b = -1
    sum_dict = {0: [-1]}
    summ = 0
    for idx, ele in enumerate(array):
        summ += ele
        if summ-given_sum in sum_dict:
            pos = sum_dict[summ-given_sum]
            if (idx-pos[0]) > (max_range_e-max_range_b):
                max_range_e = idx
                max_range_b = pos[0]
        pos = sum_dict.get(summ, [])
        pos.append(idx)
        sum_dict[summ] = pos
    return max_range_b, max_range_e


max_range_b, max_range_e = find_max_subarray([2, 3, -2, 8, -6, 9, -4, -2, 0], 3)
print(max_range_b+1, max_range_e)
