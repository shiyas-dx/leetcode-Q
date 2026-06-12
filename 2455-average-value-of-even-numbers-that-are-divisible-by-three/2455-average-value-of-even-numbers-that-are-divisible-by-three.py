class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        count = 0
        for i in nums:
            if i % 6 == 0:
                s += i
                count += 1

        return 0 if count == 0 else s // count