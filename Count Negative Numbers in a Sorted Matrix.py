class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        sum=0
        for i in grid:
            for j in i:
                if j<0:
                    sum=sum+1
        return sum
