import math

def getMid(s, e) :
    return s + (e -s) // 2

def constructSTUtil(ss, se, st, si):
    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if (ss == se):
        st[si] = 1
        return 1

    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the sum of values in this node
    mid = getMid(ss, se)

    st[si] = constructSTUtil(ss, mid, st, si * 2 + 1) + constructSTUtil(mid + 1, se, st, si * 2 + 2)

    return st[si]

""" Function to construct segment tree
from given array. This function allocates memory
for segment tree and calls constructSTUtil() to
fill the allocated memory """
def constructST(arr, n):
    # Allocate memory for the segment tree

    # Height of segment tree
    x = (int)(math.ceil(math.log2(n)))

    # Maximum size of segment tree
    max_size = 2 * (int)(2 ** x) - 1

    # Allocate memory
    st = [0] * max_size

    # Fill the allocated memory st
    constructSTUtil(0, n - 1, st, 0)

    # Return the constructed segment tree
    return st


# Driver Code
if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1, 1]
    n = len(arr)

    # Build segment tree from given array
    st = constructST(arr, n)
    print("st", st)

