class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in nums:
            if i==val:
                k=k+1
        for i in range(0,k):
            nums.remove(val)
        
