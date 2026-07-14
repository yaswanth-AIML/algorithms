class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        su=[]
        for i in accounts:
            ki=0
            for j in i:
                ki+=j
            su.append(ki)
        return max(su)
