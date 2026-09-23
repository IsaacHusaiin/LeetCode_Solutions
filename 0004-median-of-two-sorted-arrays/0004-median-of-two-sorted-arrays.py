class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        n=len(merged)
        mid = n//2 
        if n % 2 == 0:
            return (merged[mid-1]+merged[mid])/2 
        return merged[mid]