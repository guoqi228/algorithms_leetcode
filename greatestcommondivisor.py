class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """

    def gcd(self, a, b):
        # write your code here
        if a == 0 and b == 0:
            return None

        if a == 0 and b != 0:
            return b

        if a != 0 and b == 0:
            return a

        if a > b:
            return self.gcd(a % b, b)
        else:
            return self.gcd(b % a, a)