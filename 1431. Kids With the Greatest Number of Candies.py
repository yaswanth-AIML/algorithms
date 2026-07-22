class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li=[]
        max1=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max1:
                li.append(True)
            else:
                li.append(False)
        return li
