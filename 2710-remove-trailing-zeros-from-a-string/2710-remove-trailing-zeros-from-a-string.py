class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        s = num[::-1]
        res = int(s)
        return str(res)[::-1]
       
        
        