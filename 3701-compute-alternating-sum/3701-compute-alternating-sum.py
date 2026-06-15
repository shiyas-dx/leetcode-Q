class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        odd = 0
        l = len(nums)
        for i in range(0,l):
            if i % 2 == 0:
                even -= nums[i]
            else:
                odd -= nums[i]
        
        return abs(even) - abs(odd)
