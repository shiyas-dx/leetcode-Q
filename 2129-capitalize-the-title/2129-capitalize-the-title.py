class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        word = title.split()
        res = []

        for i in word:
            if len(i) > 2:
                res.append(i.capitalize())
            else:
                res.append(i.lower())
        return " ".join(res)
        