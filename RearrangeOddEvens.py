def swap(normal_idx, odd_idx, array):
    temp = array[odd_idx]
    array[odd_idx] = array[normal_idx]
    array[normal_idx] = temp

def rearrange_array(array):
    normal_idx = 0
    odd_idx = 0
    for normal_idx in range(len(array)):
        if array[normal_idx]%2 == 0: #even
            swap(normal_idx, odd_idx, array)
            odd_idx += 1

    print(array)

rearrange_array([15,13,10,8,7,3,4,6])