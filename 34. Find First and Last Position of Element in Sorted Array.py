class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            li=[]
            for i in range(len(nums)):
                if nums[i]==target:
                    li.append(i)
            return [li[0],li[-1]]
        else:
            return [-1,-1]
