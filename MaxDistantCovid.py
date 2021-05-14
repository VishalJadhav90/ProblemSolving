def isvalid(guess, positions, cow):
    prev_pos = positions[0]
    ncow = 1
    for i in range(1, len(positions)):
        if ((positions[i] - prev_pos) >= guess):
            ncow += 1
            prev_pos = positions[i]

    if (ncow >= cow):
        return True
    else:
        return False

beds, cow = 7, 3
# print(beds,cow)
positions = [1, 2, 3, 4, 5, 6, 19]

positions.sort()

left = positions[0]
right = positions[beds - 1]
ans = 0
while (left <= right):
    guess = (left + right) // 2
    if (isvalid(guess, positions, cow)):
        left = guess + 1
        ans = max(guess, ans)
    else:
        right = guess - 1

print(ans)
