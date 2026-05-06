class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = -1

        for num in arr:
            if arr.count(num) == num:
                result = max(result, num)

        return result