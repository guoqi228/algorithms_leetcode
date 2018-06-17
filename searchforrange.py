class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return [-1, -1]

        n = len(A)

        if n == 1 and A[0] == target:
            return [0, 0]
        elif n == 1 and A[0] != target:
            return [-1, -1]
        # search for start
        start = 0
        end = n - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
        if A[start] == target:
            index1 = start
        elif A[end] == target:
            index1 = end
        else:
            index1 = -1

        # search for end
        start = 0
        end = n - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
        if A[end] == target:
            index2 = end
        elif A[start] == target:
            index2 = start
        else:
            index2 = -1

        return [index1, index2]