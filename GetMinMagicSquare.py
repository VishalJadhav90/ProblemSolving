from itertools import permutations

def __get_numbers_in_magic_square(size_of_matrix):
    numbers = []
    for i in range(1, size_of_matrix*size_of_matrix+1):
        numbers.append(i)
    return numbers

def __find_all_possible_matrix(size_of_matrix):
    numbers = __get_numbers_in_magic_square(size_of_matrix)
    #print(numbers)
    magic_number = int(size_of_matrix*(size_of_matrix*size_of_matrix+1)/2)
    print(magic_number)
    magix_matrix = []
    for matrix_perm in permutations(numbers):
        print(matrix_perm)
        row = [0] * size_of_matrix
        col = [0] * size_of_matrix
        left_diag, right_diag = 0, 0
        for i in range(0, len(matrix_perm)):
            col_num = i % size_of_matrix
            row_num = i // size_of_matrix
            col[col_num] = col[col_num] + matrix_perm[i]
            row[row_num] = row[row_num] + matrix_perm[i]
            if i % (size_of_matrix+1) == 0:
                left_diag = left_diag + matrix_perm[i]
            if i != 0 and i % (size_of_matrix-1) == 0 and i != len(matrix_perm)-1:
                right_diag = right_diag + matrix_perm[i]
        row_set = set(row)
        col_set = set(col)
        print(row_set, col_set, left_diag, right_diag)
        if len(row_set) == 1 and len(col_set) == 1 and \
            left_diag == magic_number and right_diag == magic_number and \
            row_set.pop() == magic_number and col_set.pop() == magic_number:
            magix_matrix.append(matrix_perm)
    return magix_matrix

print(__find_all_possible_matrix(3))
