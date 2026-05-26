class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        c = 0
        up = []
        low = []

        for i in word:
            if i.isupper():
                up.append(i)
            elif i.islower():
                low.append(i)
            else:
                pass

        up = set(up)
        low = set(low)

        
        for x in low:
            if x.upper() in up:
                c += 1
            else:
                pass

        return c