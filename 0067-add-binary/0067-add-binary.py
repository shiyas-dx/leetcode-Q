class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = int(a, 2) + int(b, 2)
        
        b_s = bin(s)
        
        return b_s[2:]