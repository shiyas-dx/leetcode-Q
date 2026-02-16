class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0

        for i in jewels:
            for x in stones:
                if i in x:
                    count += 1

        return count
        