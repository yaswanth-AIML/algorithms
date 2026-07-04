class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i not in s:
                return i
            else:
                idx = s.index(i)
                s = s[:idx] + s[idx+1:]
