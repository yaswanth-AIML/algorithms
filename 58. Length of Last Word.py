class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.strip()[::-1]
        h=0
        for i in k:
            if i==' ':
                break
            h+=1
        return h
