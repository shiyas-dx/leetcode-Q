class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for x in nums:
            if x % 2 == 0:
                result |= x
        
        return result