class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = format(n,'032b')
        revb = b[::-1]
        res = int(revb,2)
        return res