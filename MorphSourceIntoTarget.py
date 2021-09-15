class Solution:
    def solve(self, source, target):
        if len(source) != len(target):
            return False

        uniq_chars = set()

        if source == target:
            uniq_chars.add(source[0])
            for char in source:
                if char not in uniq_chars:
                    return False
            return True

        diff_pairs = []
        for s, d in zip(source, target):
            if s != d:
                diff_pairs.append((s, d))
            if len(diff_pairs) >= 3:
                return False

        return len(diff_pairs) == 2 and diff_pairs[0][0] == diff_pairs[1][1] and diff_pairs[0][1] == diff_pairs[1][0]


sol = Solution()
assert sol.solve('aaaaab', 'aaaaba')
assert not sol.solve('ab', 'aaaaba')
assert not sol.solve('ab', 'aaaaba')
assert not sol.solve('ab', 'ab')
assert sol.solve('ab', 'ba')
assert sol.solve('aa', 'aa')
