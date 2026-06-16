class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1=set()
        for i in nums2:
            if i in nums1:
                l1.add(i)
        return list(l1)
