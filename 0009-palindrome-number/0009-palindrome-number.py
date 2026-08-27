class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        if s[0] == '-' and s[0] == '+':
            if s[0::-1] == s:
                return True
        else:
            if s[::-1] == s:
                return True
        return False