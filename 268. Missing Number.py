class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng=len(nums)
        for i in range(leng):
            if i not in nums:
                return i
        else:       
            return leng
