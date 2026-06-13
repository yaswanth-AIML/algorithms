class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        num=max(arr)
        index=arr.index(num)
        return index
