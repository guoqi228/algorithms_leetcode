class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    dynamic programming solution complexity: O(n^2)
    """

    def longestPalindrome(self, s):
        # write your code here
        n = len(s)
        if n == 1 or n == 0:
            return s
        # initialize start position and maxlength of palindrome
        start = 0
        maxlength = 1
        # boolean table n by n: false or true
        ispalindrome = [[0 for i in range(n)] for j in range(n)]
        # k = substring length
        # when k = 1, every letter is s is a palindrome
        for i in range(n):
            ispalindrome[i][i] = True

        # k = 2, every adjacent letter
        for i in range(n - 1):
            ispalindrome[i][i + 1] = s[i] == s[i + 1]
            if ispalindrome[i][i + 1]:
                start = i
                maxlength = 2

        # k >= 3, substring length [3, n]
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                ispalindrome[i][i + k - 1] = \
                    ispalindrome[i + 1][i + k - 2] and \
                    s[i] == s[i + k - 1]

                if ispalindrome[i][i + k - 1] and k > maxlength:
                    start = i
                    maxlength = k

        return s[start:start + maxlength]








