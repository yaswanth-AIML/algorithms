class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list1=set(range(1,len(nums)+1))
        num1=set(nums)
        return list(list1-num1)
