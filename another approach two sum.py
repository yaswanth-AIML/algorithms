class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new=target-nums[i]
            if new in nums and nums.index(new)!=i:
                return [i,nums.index(new)]
