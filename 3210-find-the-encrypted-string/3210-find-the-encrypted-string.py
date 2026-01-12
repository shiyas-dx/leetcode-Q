class Solution(object):
    def getEncryptedString(self, s, k):
        n = len(s)
        result = []

        for i in range(n):
            result.append(s[(i + k) % n])
        
        return "".join(result)
        