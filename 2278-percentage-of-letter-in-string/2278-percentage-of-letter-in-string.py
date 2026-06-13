class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        c = s.lower().count(letter.lower())
        res = (float(c) / len(s)) * 100 
        return int(res)
        
        