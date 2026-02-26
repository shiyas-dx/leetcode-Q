class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=""
        for i in num:
            res+=str(i)
        res1 = int(res)+k
        res2 = list(str(res1))
        res3 = [int(s) for s in res2]
        return res3