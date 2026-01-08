class Solution(object):
    def largestEven(self, s):
        z = ""
        
        
        if int(s[-1]) % 2 == 0:
            return s
        
        
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 0:
                z = s[:i + 1]
                break
        
        return z
