class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1=[]
        for i in nums2:
            if i in nums1:
                l1.append(i)
                nums1.remove(i)
        return l1
