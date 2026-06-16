class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        num2=nums[-1]*nums[-2]*nums[-3]
        num3=nums[0]*nums[1]*nums[-1]
        if num2>num3:
            return num2
        else:
            return num3
