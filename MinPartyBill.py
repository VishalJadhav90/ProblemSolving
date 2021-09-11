class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        #print("A: {} B: {} C: {}".format(A, B, C))
        friend_capacity = A
        plate_capacity = B
        plate_cost = C

        plates = len(plate_capacity)

        ans = 0

        subsol = [[100000 for _ in range(1001)] for _ in range(plates+1)]
        for j in range(plates+1):
            subsol[j][0] = 0
        for j in range(1001):
            subsol[0][j] = 999999
            subsol[0][0] = 0
        for i in range(1, plates+1):
            for j in range(1, 1001):
                if plate_capacity[i-1] <= j:
                    subsol[i][j] = min(plate_cost[i-1]+subsol[i][j-plate_capacity[i-1]], subsol[i-1][j])
                else:
                    subsol[i][j] = subsol[i-1][j]
        #print("*"*20)
        # for l in subsol:
        # 	print(l)
        #print("----->", subsol[plates][each_friend_capacity])
        for each_friend_capacity in friend_capacity:
            ans = ans+subsol[plates][each_friend_capacity]

        return ans

A = [ 501, 148, 502, 34, 596, 451, 382, 83, 164, 991, 716, 415, 645, 646, 790, 845, 206, 9, 827, 907, 497, 556, 297,
      380, 321, 309, 459, 425, 913, 829, 344, 133, 696, 846, 885, 292, 16, 267, 374, 179, 976, 808, 312, 622, 173, 102, 467, 97, 828, 13, 722, 44, 568, 19, 424 ]
B = [ 1, 328, 882, 33, 959, 431, 95, 93, 127, 659, 977, 137, 394, 962, 229, 572, 939, 37, 884, 280, 209, 704, 465,
      24, 533, 477, 745, 576, 764, 764, 718, 91, 810, 320, 841, 769, 750, 935, 861, 595, 314, 557, 731, 707, 239, 959, 997, 896, 714, 881, 176, 641, 305, 640, 664, 837, 835, 409, 413, 599, 891, 850, 408, 701, 170, 249, 471, 919, 185, 51, 514, 217, 327, 963, 923, 565, 922, 920, 461, 355, 521, 355, 995, 825, 713, 378 ]
C = [ 381, 548, 786, 512, 866, 397, 362, 274, 98, 531, 523, 568, 169, 426, 338, 401, 642, 664, 364, 284, 229, 5, 922,
      408, 359, 162, 762, 73, 705, 475, 450, 86, 23, 955, 317, 607, 352, 678, 881, 449, 928, 123, 736, 97, 267, 74, 498, 908, 737, 861, 910, 684, 585, 832, 92, 943, 994, 853, 735, 699, 328, 185, 504, 69, 858, 820, 676, 210, 498, 276, 378, 426, 398, 114, 242, 383, 187, 739, 10, 642, 319, 919, 326, 903, 470, 417 ]

sol = Solution()
result = sol.solve(A, B, C)
print(result)
