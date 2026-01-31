class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)

        res = []

        for i in candies:
            if i + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)

        return res
        