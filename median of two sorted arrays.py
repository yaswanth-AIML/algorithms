def findMedianSortedArrays(nums1,nums2):
  merge=nums1+nums2
  merge1=merge.sort()
  n=len(merge)
  if n%2==1:
    return merge[n//2]
  else:
    mid1=merge[n//2-1]
    mid2=merge[n//2]
    return (mid1+mid2)/2
