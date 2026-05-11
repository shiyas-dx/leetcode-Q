class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        l = 0

        for x in nums:
            if len(str(x)) == 1:
                s += x
            else:
                l += x

        if s != l:
            return True
        else:
            return False