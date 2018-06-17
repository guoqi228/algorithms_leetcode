class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = 0
        row, col = len(matrix), len(matrix[0])
        row_p, col_p = 0, len(matrix[0]) - 1

        while row_p < row and col_p >= 0:
            if matrix[row_p][col_p] == target:
                n += 1
                row_p += 1
                col_p -= 1
            elif matrix[row_p][col_p] > target:
                col_p -= 1
            elif matrix[row_p][col_p] < target:
                row_p += 1

        return n