class Solution(object):
    def findMissingElements(self, nums):
        result = []

        start = min(nums)
        end = max(nums)
        
        for x in range(start ,end + 1):
            if x not in nums:
                result.append(x)
        return result