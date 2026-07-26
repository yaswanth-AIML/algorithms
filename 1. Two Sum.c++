class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            re=target-nums[i]
            if re in hashmap:
                return [hashmap[re],i]
            hashmap[nums[i]]=i
