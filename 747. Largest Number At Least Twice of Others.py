class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_=max(nums)
        idx=nums.index(max_)
        nums.sort()
        if 2*(nums[-2])<=max_:
            return idx
        else:
            return -1
