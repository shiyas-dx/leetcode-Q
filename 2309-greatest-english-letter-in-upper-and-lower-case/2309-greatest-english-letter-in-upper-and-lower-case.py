class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        up = []
        lw = []

        for i in s:
            if i.isupper():
                up.append(i)
            elif i.islower():
                lw.append(i)

        up.sort(reverse=True)   
        lw = set(lw)           

        for x in up:
            if x.lower() in lw:  
                return x     
                break
        else:
            return ""
        

