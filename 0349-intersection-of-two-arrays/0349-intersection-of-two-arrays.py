class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res = []

        # for i in nums1:
        #     if str(i) in str(nums2):
        #        res.append(i)
        #     else:
        #         pass
        
        # resu = set(res)
        # return list(resu)
        result = list(set(nums1) & set(nums2))

        return result