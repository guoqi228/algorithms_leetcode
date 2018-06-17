class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    filter out all the invalid letter then use two pointers left -->mid<--rgiht
    complexity: O(n)
    """

    def isPalindrome(self, s):
        # write your code here
        if s == '':
            return True
        valid_s = self.getvalid(s)
        print(valid_s)
        n = len(valid_s)
        for i in range(int(n / 2)):
            if valid_s[i] == valid_s[-i - 1]:
                continue
            else:
                return False
        return True

    def getvalid(self, s):
        valids = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                valids.append(s[i].lower())
        return valids