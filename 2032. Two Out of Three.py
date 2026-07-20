class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ki=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                ki.append(i)
        for j in nums2:
            if j in nums3:
                ki.append(j)
        return list(set(ki))
