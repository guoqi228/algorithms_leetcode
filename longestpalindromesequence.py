class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    dynamic programming complexity: O(n^2)
    """

    def longestPalindromeSubseq(self, s):
        # write your code here
        if s is None or s == '':
            return 0
        n = len(s)
        # maxlength = 0
        # k = length of subsequence
        # i = left   j = right
        # table n by n: length of longest palindrome subsequence
        table = [[0 for i in range(n)] for j in range(n)]

        # initialize k = 1
        for i in range(n):
            table[i][i] = 1

        # initialize k = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = 2
            else:
                table[i][i + 1] = 1

        for k in range(3, n + 1):
            for i in range(n - k + 1):
                if s[i] == s[i + k - 1]:
                    table[i][i + k - 1] = table[i + 1][i + k - 2] + 2
                else:
                    table[i][i + k - 1] = max(table[i + 1][i + k - 1], \
                                              table[i][i + k - 2])
        return table[0][n - 1]
