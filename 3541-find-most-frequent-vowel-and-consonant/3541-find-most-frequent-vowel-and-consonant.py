class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel = "aeiou"

        v_count = 0

        nv_count = 0

        for i in s:
            if i in vowel:
                if s.count(i) > v_count:
                    v_count = s.count(i)
            elif s.count(i) > nv_count:
                nv_count = s.count(i)
                
        return v_count + nv_count