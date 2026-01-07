class Solution(object):
    def getLeastFrequentDigit(self, n):
        s = str(n)
        ans = None
        min_count = float('inf')

        for d in s:
            c = s.count(d)

            if c < min_count or (c == min_count and int(d) < ans):
                min_count = c
                ans = int(d)

        return ans
