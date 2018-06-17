class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        # write your code here
        i = 2
        output = []
        while i * i <= num and num > 1:
            if num % i == 0:
                num = num / i
                output.append(i)
            else:
                i = i + 1

        if num > 1:
            output.append(int(num))

        return output