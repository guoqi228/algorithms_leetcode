class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    complexity: brutal force solution N(O^3)
    """

    def longestPalindrome(self, s):
        # write your code here
        n = len(s)
        maxlength = 0
        for i in range(0, n + 1):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if self.isPalindrome(substring) and maxlength < len(substring):
                    maxlength = len(substring)
                    out = s[i:j]
        return out

    def isPalindrome(self, sub):
        n = len(sub)
        if n == 1 or n == 0:
            return sub
        if n == 2:
            return sub[0] == sub[1]
        mid = int(n / 2)
        for i in range(mid):
            if sub[i] == sub[(-i - 1)]:
                continue
            else:
                return False
        return True