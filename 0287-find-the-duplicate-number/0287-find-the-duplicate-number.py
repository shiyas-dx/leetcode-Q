class Solution(object):
    def findDuplicate(self, nums):
        s = set()
        for x in nums:
            if x in s:
                return x
            s.add(x)
        