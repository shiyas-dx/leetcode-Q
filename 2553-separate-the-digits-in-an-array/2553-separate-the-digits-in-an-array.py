class Solution(object):
    def separateDigits(self, nums):
        result = [int(d) for n in nums for d in str(n)]
        return result
        