class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ""

        for i in s:
            if i.isalnum():
                
                res += i.lower()
        return res == res[::-1]
        