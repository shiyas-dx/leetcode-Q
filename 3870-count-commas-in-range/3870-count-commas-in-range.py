class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """

        c = 0

        for i in range(1,n+1):
            c += (len(str(i))-1) // 3
        return (c)


        # c = 0
        # l = 0
        # for i in range(len(str(n))):
        #     if i <= 3:
        #         l += 1
        
        # for x in str(n):
        #     if l <= 3:
        #         c += 0
        #     elif l >= 4:
        #         c = int(x[0:]) + 1
        #     else:
        #         pass

        # return (c)