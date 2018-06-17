class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row_size = len(matrix)
        col_size = len(matrix[0])

        start = 0
        end = row_size * col_size - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            row_index, col_index = int(mid / col_size), int(mid % col_size)
            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] > target:
                end = mid
            elif matrix[row_index][col_index] < target:
                start = mid

        row_index, col_index = int(start / col_size), int(start % col_size)
        if matrix[row_index][col_index] == target:
            return True

        row_index, col_index = int(end / col_size), int(end % col_size)
        if matrix[row_index][col_index] == target:
            return True

        return False