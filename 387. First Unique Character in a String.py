class Solution:
    def firstUniqChar(self, s: str) -> int:
        c={}
        for i in s:
            c[i]=c.get(i,0)+1
        for j in range(len(s)):
            ch=s[j]
            if c[ch]==1:
                return j
        return -1
