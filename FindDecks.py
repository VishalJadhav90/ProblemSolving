import bisect
class Solution:
    def findNumberOfLIS(self, nums):
        if not nums: return 0

        decks, ends_decks, paths = [], [], []
        for num in nums:
            deck_idx = bisect.bisect_left(ends_decks, num)
            print("num", num, "deck_idx", deck_idx)
            n_paths = 1
            if deck_idx > 0:
                l = bisect.bisect(decks[deck_idx - 1], -num)
                n_paths = paths[deck_idx - 1][-1] - paths[deck_idx - 1][l]

            if deck_idx == len(decks):
                decks.append([-num])
                ends_decks.append(num)
                paths.append([0, n_paths])
            else:
                decks[deck_idx].append(-num)
                ends_decks[deck_idx] = num
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])

        for deck in decks:
            print(deck)

        return paths[-1][-1]

sol = Solution()
print("result", sol.findNumberOfLIS([1,3,5,4,7,10,8,2,8]))