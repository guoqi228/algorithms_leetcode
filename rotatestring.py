class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, string, offset):
        # write your code here
        if string is None or len(string) == 0:
            return

        offset = offset % len(string)

        self.reverse(string, 0, len(string) - offset - 1)
        self.reverse(string, len(string) - offset, len(string) - 1)
        self.reverse(string, 0, len(string) - 1)

    def reverse(self, string, start, end):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start = start + 1
            end = end - 1