class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list1=[]
        list2=[]
        for i in nums:
            if i not in list1:
                list1.append(i)
            else:
                list2.append(i)
        h=set(list1)-set(list2)
        h1=h.pop()
        return h1
