class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            max1=max(nums)
            max2=0
            nums.remove(max1)
            for i in nums:
                if i>max2:
                    max2=i
            return (max1-1)*(max2-1)
