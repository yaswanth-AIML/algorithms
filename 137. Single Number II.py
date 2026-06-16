class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l1=[]
        l2=[]
        for i in nums:
            if i not in l1:
                l1.append(i)
            else:
                l2.append(i)
        for i in l1:
            if i not in l2:
                return i
