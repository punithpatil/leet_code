# https://leetcode.com/problems/transpose-matrix/

# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

# Example 1:

# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
 

# Note:

# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # Note: Interesting one liner with zip() exists
        output = []
        row_length = len(A)
        column_length = len(A[0])
        
        for j in range(column_length):
            row = []
            for i in range(row_length):
                row.append(A[i][j])
            output.append([*row])
            del row [:]
            
        return output