def findMaxBST(n, results):
    if n in results:
        return results.get(n)

    bsts = 0
    for i in range(n):
        prev = findMaxBST(i-0, results)
        next = findMaxBST(n-(i+1), results)
        bsts = bsts + prev*next
    results[n] = bsts
    return bsts

#1 2 3 4 5

results = {0: 1, 1: 1, 2: 2, 3: 5}
findMaxBST(5, results)
print(results)
