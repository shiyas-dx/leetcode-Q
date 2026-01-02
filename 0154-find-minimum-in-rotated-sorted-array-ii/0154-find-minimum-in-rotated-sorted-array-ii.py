class Solution:
    def findMin(self, nums):
        mini = nums[0]

        for num in nums:
            if num < mini:
                mini = num

        return mini
