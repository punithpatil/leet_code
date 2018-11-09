# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row_length = len(grid)
        column_length = len(grid[0])
        area = 0
        def dfs(row, column):
            nonlocal area, row_length, column_length, grid 
            if 0 <= row < row_length and 0 <= column < column_length:
                if grid[row][column] == 1:
                    grid[row][column] = 0
                    area += 1
                    #go right
                    dfs(row, column+1)
                    #go down
                    dfs(row+1, column)
                    #go left
                    dfs(row, column-1)
                    #go up
                    dfs(row-1, column)
            
        output = []
        for row in range(row_length):
            for column in range(column_length):
                if grid[row][column] == 1:
                    area = 0
                    dfs(row, column)
                    output.append(area)
        
        return max(output) if output else 0
