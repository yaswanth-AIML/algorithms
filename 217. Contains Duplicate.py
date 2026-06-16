class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l1=set()
        for i in nums:
            if i in l1:
                return True
            l1.add(i)
        return False
