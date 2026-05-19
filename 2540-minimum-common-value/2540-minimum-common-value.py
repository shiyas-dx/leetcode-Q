class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set0fnums2 = set(nums2)
        
        for i in nums1:
            if i in set0fnums2:
               return i
        return -1