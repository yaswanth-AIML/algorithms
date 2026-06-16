class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uni=list(set(nums))
        uni.sort()
        if len(uni)<3:
            return uni[-1]
        else:
            return uni[-3]
