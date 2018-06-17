class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b

        if n == 1:
            return a % b

        if n % 2 == 1:
            temp = self.fastPower(a, b, int(n / 2))
            # print(temp)
            return ((temp % b) * (temp % b) * a) % b
        else:
            temp = self.fastPower(a, b, int(n / 2))
            # print(temp)
            return (temp % b) * (temp % b) % b