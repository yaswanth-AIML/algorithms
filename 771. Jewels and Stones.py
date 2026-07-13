class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        k=0
        for s in stones:
            if s in jewels:
                k += 1
        return k
