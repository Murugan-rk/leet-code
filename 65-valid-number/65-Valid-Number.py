class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for char in s:
            if char.isalpha() and char.lower() not in ['e']:
                return False
        try:
            float(s)
            return True
        except:
            return False