class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums[::-1]
        result = nums + res
        return result
        