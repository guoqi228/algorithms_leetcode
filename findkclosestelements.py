class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here
        if A is None or len(A) == 0 or k > len(A):
            return None

        closest = self.findclosest(A, target)

        ouput = self.searchkclosest(A, target, closest, closest + 1, k)

        return ouput

    def findclosest(self, A, target):
        start = 0
        end = len(A) - 1
        while (start + 1) < end:
            mid = int((start + end) / 2)
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
        if abs(A[start] - target) <= abs(A[end] - target):
            return start
        else:
            return end

    def searchkclosest(self, A, target, left, right, k):
        output = []
        for i in range(k):
            if right > len(A) - 1 and left > 0:
                output.append(A[left])
                left -= 1
            elif left < 0 and right < len(A) - 1:
                output.append(A[right])
                right += 1
            elif abs(A[left] - target) <= abs(A[right] - target):
                output.append(A[left])
                left -= 1
            elif abs(A[left] - target) > abs(A[right] - target):
                output.append(A[right])
                right += 1
        return output