class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s1 = s1.split()
        s2 = s2.split()

        res = s1+s2
        li=[]
        for x in res:
            y = res.count(x)
            if y == 1:
                li.append(x)
        return li
