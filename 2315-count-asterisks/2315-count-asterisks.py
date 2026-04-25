class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = s.split('|')
        return sum(p.count('*')for p in p[::2])