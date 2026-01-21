class Solution(object):
    def sumOfUnique(self, nums):
        num = []
        for x in nums:
            if nums.count(x) == 1:
                num.append(x)
        
        return sum(num)
        