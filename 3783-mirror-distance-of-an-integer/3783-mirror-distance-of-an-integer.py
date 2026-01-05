class Solution(object):
    def mirrorDistance(self, n):
        revers = str(n)
        num = revers[::-1]
        nums = int(num)
        return abs(n - nums)