class Solution(object):
    def reorderSpaces(self, text):
        
        words = text.split()
        total_spaces = text.count(" ")

        
        if len(words) == 1:
            return words[0] + " " * total_spaces

        gaps = len(words) - 1
        space_each = total_spaces // gaps
        extra = total_spaces % gaps

        return (" " * space_each).join(words) + " " * extra