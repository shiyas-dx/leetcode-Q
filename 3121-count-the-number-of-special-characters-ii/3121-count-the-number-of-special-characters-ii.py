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
                last_lower = word.rfind(x)
                first_upper = word.find(x.upper())
                if last_lower < first_upper:
                    c += 1

        return c