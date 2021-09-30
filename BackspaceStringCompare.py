class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        slist = []
        tlist = []
        for c in s:
            if c != "#":
                slist.append(c)
            else:
                if slist: slist.pop()
        for c in t:
            if c != "#":
                tlist.append(c)
            else:
                if tlist: tlist.pop()
        #print("slist", slist)
        #print("tlist", tlist)
        if len(slist) != len(tlist):
            return False
        for i in range(len(slist)):
            if slist[i] != tlist[i]:
                return False
        return True

