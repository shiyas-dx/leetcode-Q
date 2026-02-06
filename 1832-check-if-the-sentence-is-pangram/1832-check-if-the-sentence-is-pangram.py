class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        res = set()
        for i in sentence:
            i = i.lower()
            if 'a' <= i <= 'z':
                res.add(i)
        return len(res) == 26