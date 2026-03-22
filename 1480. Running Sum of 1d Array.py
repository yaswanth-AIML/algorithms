class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list1=[]
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            list1.append(total)
        return list1
