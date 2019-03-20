# https://leetcode.com/problems/spiral-matrix/

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []
        row_start = column_start = 0
        row_end = len(matrix) - 1
        column_end = len(matrix[0]) - 1
        output = []
        direction = 0
        while row_start <= row_end and column_start <= column_end:
            if direction == 0: # right
                for i in range(column_start, column_end + 1):
                    r = row_start
                    c = i 
                    output.append(matrix[r][c])
                row_start += 1
            
            elif direction == 1: # down
                for i in range(row_start, row_end + 1):
                    r = i
                    c = column_end
                    output.append(matrix[r][c])
                column_end -= 1
            
            elif direction == 2: # left
                for i in range(column_end, column_start - 1, -1):
                    r = row_end
                    c = i 
                    output.append(matrix[r][c])
                row_end -= 1
            
            elif direction == 3: # up
                for i in range(row_end, row_start - 1, -1):
                    r = i
                    c = column_start 
                    output.append(matrix[r][c])
                column_start += 1
            
            direction = (direction + 1)%4
        
        return output