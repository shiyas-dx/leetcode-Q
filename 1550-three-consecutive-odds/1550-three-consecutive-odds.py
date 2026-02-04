class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count = 0
        found = False

        for n in arr:
            if n % 2 != 0:
                count += 1
                if count == 3:
                    found = True
                    break
            else:
                count = 0
        return found

        # res = sum(1 for i in arr if i % 2 != 0) >= 3
        # return res
         


        # for i in arr:
        #     if i % 2 == 0:
        #         return False
        #     else:
        #         return True