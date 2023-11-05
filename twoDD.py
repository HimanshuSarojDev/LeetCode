class Solution(object):
    def diagonalSum(self, mat):
        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]  
            total += mat[i][n - 1 - i]  

        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
        return total


solution = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]

result = solution.diagonalSum(mat)
if result:
    print(result)  
