class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = len(nums)

        for i in range(0,m + 1):
            if i not in nums:
                return i