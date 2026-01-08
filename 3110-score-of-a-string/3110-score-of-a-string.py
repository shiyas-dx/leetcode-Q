class Solution(object):
    def scoreOfString(self, s):
        result = []

        for x in s:
            result.append(ord(x))

        s=0 

        for i in range(len(result)-1):
            s+=abs(result[i]-result[i+1])

        return s
        