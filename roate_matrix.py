class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
        
        return matrix  # Return the rotated matrix

solution = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = solution.rotate(mat)
print(result)
