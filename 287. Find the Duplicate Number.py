class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        li=set()
        for i in nums:
            if i not in li:
                li.add(i)
            else:
                return i
        else:
            return -1
