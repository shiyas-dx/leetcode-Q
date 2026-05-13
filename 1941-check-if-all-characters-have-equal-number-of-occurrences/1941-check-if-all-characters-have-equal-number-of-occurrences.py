class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = set(s)
        h = s.count(s[0])
        
        for i in m:
            if s.count(i) == h:
                pass
            else:
                return False

        return True