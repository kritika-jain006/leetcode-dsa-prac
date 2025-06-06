class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1+nums2
        d= len(c)
        b = sorted(c)
        if d%2 != 0:
            q = d // 2 
            med = b[q]
        elif d%2 == 0:
            q = d // 2
            e = q-1
            med = (b[q]+b[e])/2
        return med


        