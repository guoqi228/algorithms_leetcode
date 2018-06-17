class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    enumeration solution complexity: O(n^2)
    """

    def longestPalindrome(self, s):
        # write your code here
        n = len(s)
        if n == 0 or n == 1:
            return s
        longest = 0
        start = 0
        for i in range(0, n - 1):
            palindromelen = self.palindromeLength(s, i, i + 1)
            if palindromelen > longest:
                longest = palindromelen
                start = i - int(longest / 2) + 1
            palindromelen = self.palindromeLength(s, i, i)
            if palindromelen > longest:
                longest = palindromelen
                start = i - int(longest / 2)
        return s[start: start + longest]

    def palindromeLength(self, s, left, right):
        n = len(s)
        palindromelen = 0
        while (left >= 0 and right < n):
            if s[left] != s[right]:
                break
            else:
                palindromelen = right - left + 1
                left = left - 1
                right = right + 1
        return palindromelen
