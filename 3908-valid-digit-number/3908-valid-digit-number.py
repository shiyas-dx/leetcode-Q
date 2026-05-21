class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        n = str(n)
        x = str(x)
        if n[0] == x:
            return False
        elif x in n[1:]:
            return True
        else:
            return False
        