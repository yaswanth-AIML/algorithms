class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list1=[]
        list2=[]
        for i in nums:
            if i not in list1:
                list1.append(i)
            elif i in list1 and i not in list2:
                list1.append(i)
                list2.append(i)
            else:
                pass
        nums[:]=list1
