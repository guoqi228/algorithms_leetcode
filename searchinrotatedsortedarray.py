class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here

        if A is None or len(A) == 0:
            return -1

        n = len(A)

        if n == 1 and A[0] != target:
            return -1
        elif n == 1 and A[0] == target:
            return 0

        start = 0
        end = n - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            if A[mid] == target:
                return mid
            elif A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[start]:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1