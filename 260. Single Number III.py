class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in nums:
            if i not in l1:
                l1.append(i)
            else:
                l2.append(i)
        return list(set(l1)-set(l2))
