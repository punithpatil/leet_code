# https://leetcode.com/problems/image-smoother

# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

# Example 1:

# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:

# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row_length = len(M)
        column_length = len(M[0])

        output = []
        
        def extractor(row, column):
            nonlocal M, row_length, column_length
            if 0 <= row < row_length and 0 <= column < column_length:
                return M[row][column], 1
            else:
                return 0, 0
        
        output_row = []    
        for row in range(row_length):
            for column in range(column_length):
                points = [
                    # point itself
                    extractor(row,  column),
                    # right
                    extractor(row,  column+1),
                    # bottom right
                    extractor(row+1,column+1),
                    # bottom
                    extractor(row+1,column),
                    # bottom left
                    extractor(row+1,column-1),
                    # left
                    extractor(row,  column-1),
                    # top left
                    extractor(row-1,column-1),
                    # top
                    extractor(row-1,column),
                    # top right
                    extractor(row-1,column+1)
                ]
                
                numerator = sum([i for i, _ in points])
                denominator = sum([j for _, j in points])
                output_row.append(numerator//denominator)
            
            output.append([*output_row]) # unpack into list to avoid deletion by reference
            del output_row[:]
        
        return output
