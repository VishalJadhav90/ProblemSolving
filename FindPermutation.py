from collections import Counter

class Solution:
    def sol(self, s1, s2):
        if len(s2) < len(s1):
            return False
        win_size = len(s1)
        src_c = Counter(s1)
        des_c = Counter(s2[:win_size])

        if src_c == des_c:
            return True

        for i in range(len(s2)-win_size):
            if des_c[s2[i]] == 1:
                del des_c[s2[i]]
            elif des_c[s2[i]] > 1:
                des_c[s2[i]] -= 1

            des_c[s2[i+win_size]] = des_c.get(s2[i+win_size], 0) + 1
            if src_c == des_c:
                return True
        return False

