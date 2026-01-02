class Solution(object):
    def totalMoney(self, n):
        total = 0
        current = 1

        for day in range(1, n + 1):
            total += current
            current += 1

            if day % 7 == 0:
                current = day // 7 + 1

        return total