class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here

        start = 1
        end = len(A) - 2

        while start + 1 < end:
            mid = int((start + end) / 2)
            if A[mid] < A[mid + 1] or A[mid] > A[mid - 1]:
                start = mid
            elif A[mid] > A[mid + 1] or A[mid] < A[mid - 1]:
                end = mid

        if A[start] > A[end]:
            return start
        else:
            return end