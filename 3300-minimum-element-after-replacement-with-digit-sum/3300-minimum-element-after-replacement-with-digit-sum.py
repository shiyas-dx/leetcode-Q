class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(sum(map(int, str(num))) for num in nums)
