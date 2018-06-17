class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """

    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n

        temp = self.myPow(x, int(n / 2))

        if n % 2 == 1:
            return temp * temp * x
        else:
            return temp * temp