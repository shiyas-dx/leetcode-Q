class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[str(i) for i in num]
        res1=list(str(int("".join(res))+k))
        res2 = [int(s) for s in res1]
        return res2