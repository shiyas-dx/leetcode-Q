class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = "".join([i for i in str(n) if i != "0"])
        
        return int(res)