class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    double loop solution complexity: O(n^2)
    """

    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        n = len(source)
        m = len(target)
        if m > n:
            return -1
        if m == 0:
            return 0
        for i in range(n - m + 1):
            if target[0] == source[i]:
                sub_source = source[i:i + n]
                if self.check(target, sub_source):
                    return i
        return -1

    def check(self, s1, s2):
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                return False
            else:
                continue
        return True

