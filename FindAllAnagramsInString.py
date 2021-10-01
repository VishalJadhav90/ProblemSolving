class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        result = []
        pdict = {}
        for c in p:
            pdict[c] = pdict.get(c, 0) + 1

        sdict = {}
        for i in range(len(p)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1

        if sdict == pdict:
            result.append(0)

        for window_beg in range(len(s) - len(p)):
            sdict[s[window_beg]] -= 1
            if not sdict[s[window_beg]]:
                del sdict[s[window_beg]]

            window_beg = window_beg + 1
            window_end = window_beg + (len(p) - 1)
            sdict[s[window_end]] = sdict.get(s[window_end], 0) + 1
            if sdict == pdict:
                result.append(window_beg)

        return result

