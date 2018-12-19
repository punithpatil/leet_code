# https://leetcode.com/problems/set-matrix-zeroes/

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_length = len(matrix)
        column_length = len(matrix[0])
        row_flag = column_flag = False
        
        # Find if first row/column have 0
        for i in range(row_length):
            if matrix[i][0] == 0:
                column_flag = True
        for j in range(column_length):
            if matrix[0][j] == 0:
                row_flag = True
        
        #Find where zeros occur in matrix except first and seond column
        for i in range(row_length):
            for j in range(column_length):
                if matrix[i][j] == 0:
                    # Mark column head to 0
                    matrix[i][0] = 0
                    # Mark row head to 0
                    matrix[0][j] = 0
        
        # Marks rows with 0
        for i in range(1, row_length):
            if matrix[i][0] == 0:
                for j in range(1, column_length):
                    matrix[i][j] = 0 
        # Mark columns with 0
        for j in range(1, column_length):
            if matrix[0][j] == 0:
                for i in range(row_length):
                    matrix[i][j] = 0
                    
        #Check is first column should be made 0            
        if column_flag:
            for i in range(1, row_length):
                matrix[i][0] = 0
                
        #Check if fist row should be made 0
        if row_flag:
            for j in range(1, column_length):
                matrix[0][j] = 0
                
        return